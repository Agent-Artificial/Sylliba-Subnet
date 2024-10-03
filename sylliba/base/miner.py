# The MIT License (MIT)
# Copyright © 2023 Yuma Rao

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
import os
import time
import asyncio
import threading
import argparse
import traceback
import pickle

import bittensor as bt
import sylliba
from sylliba.base.neuron import BaseNeuron
from sylliba.utils.config import add_miner_args
from sylliba.protocol import TranslateRequest

from neurons.config import miner_config

from typing import Union
from dotenv import load_dotenv

load_dotenv()


config = miner_config()


class BaseMinerNeuron(BaseNeuron):
    """
    Base class for Bittensor miners.

    This class provides the fundamental structure and functionality for a miner neuron in the Bittensor network.
    It handles the setup, running, and management of the miner's operations.

    Attributes:
        neuron_type (str): Identifier for the neuron type, set to "MinerNeuron".
        axon (bt.axon): The axon instance for handling network requests.
        should_exit (bool): Flag to indicate if the miner should stop running.
        is_running (bool): Flag to indicate if the miner is currently running.
        thread (Union[threading.Thread, None]): Thread for running the miner in the background.
        lock (asyncio.Lock): Asynchronous lock for thread-safe operations.
    """

    neuron_type: str = "MinerNeuron"

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser):
        """
        Adds miner-specific arguments to the argument parser.

        Args:
            parser (argparse.ArgumentParser): The argument parser to add arguments to.
        """
        super().add_args(parser)
        add_miner_args(cls, parser)

    @classmethod
    def save_state(cls):
        """
        Saves the current state of the miner. Currently a placeholder method.
        """
        pass
    
    def __init__(self, config=None):
        """
        Initializes the BaseMinerNeuron with the given configuration.

        Args:
            config: Configuration for the miner. If None, uses default configuration.
        """
        super().__init__(config=config)
        
        # Warn if allowing incoming requests from anyone.
        if not self.config.blacklist.force_validator_permit:
            bt.logging.warning(
                "You are allowing non-validators to send requests to your miner. This is a security risk."
            )
        if self.config.blacklist.allow_non_registered:
            bt.logging.warning(
                "You are allowing non-registered entities to send requests to your miner. This is a security risk."
            )
        # The axon handles request processing, allowing validators to send this miner requests.
        self.axon = bt.axon(wallet=self.wallet, config=self.config() if callable(self.config) else self.config)

        # Attach determiners which functions are called when servicing a request.
        bt.logging.info(f"Attaching forward function to miner axon.")
        self.axon.attach(
            forward_fn=self.forward,
            # [fix/validator-miner-communcation]: attaching the verify function to the axon
            verify_fn=self.verify)
        bt.logging.info(f"Axon created: {self.axon}")

        # Instantiate runners
        self.should_exit: bool = False
        self.is_running: bool = True
        self.thread: Union[threading.Thread, None] = None
        self.lock = asyncio.Lock()

    def start_miner(self):
        """
        Starts the miner by setting up the axon and serving it on the network.

        This method checks for registration, serves the axon, and starts it on the network.
        """
        # [fix/validator-miner-communcation]: pulled the setup starting functionality that only needs to happen once
        # into a new method to reduce computational overhead.
        
        # Check that miner is registered on the network.
        self.sync()

        # Serve passes the axon information to the network + netuid we are hosting on.
        # This will auto-update if the axon port of external ip have changed.
        bt.logging.info(
            f"Serving miner axon {self.axon} on network: {self.config.subtensor.chain_endpoint} with netuid: {int(os.getenv('BT_NETUID'))}"
        )
        self.axon.serve(netuid=int(os.getenv("BT_NETUID")), subtensor=self.subtensor)

        # Start  starts the miner's axon, making it active on the network.
        self.axon.start()

        bt.logging.info(f"Miner starting at block: {self.block}")
    
    # [fix/validator-miner-communcation]: The parameters in this loop to be more clear and changed the 
    # logic to evaluate when the value is greater than if it starts above the update block count.    
    def run(self):
        """
        Initiates and manages the main loop for the miner on the Bittensor network.

        This method handles the miner's primary operations, including chain synchronization,
        metagraph updates, and weight setting. It continues running until intentionally stopped
        or interrupted.

        Raises:
            KeyboardInterrupt: If the miner is stopped by a manual interruption.
            Exception: For unforeseen errors during the miner's operation, which are logged for diagnosis.
        """

        # This loop maintains the miner's operations until intentionally stopped.
        blocks_since_update = self.block - self.metagraph.last_update[self.uid]
        blocks_to_wait = self.config.neuron.epoch_length
        try:
            # [fix/validator-miner-communcation]: double negative. while not self.should_exit = while on
            while not self.should_exit:
                if blocks_since_update > blocks_to_wait:
                    # Sync metagraph and potentially set weights.
                    self.sync()
                    self.step += 1
                    continue
                    # Wait before checking again.
                bt.logging.info(f"Miner running... {time.time()}")
                time.sleep(10)
                

                # Check if we should exit.
                if self.should_exit:
                    break


        # If someone intentionally stops the miner, it'll safely terminate operations.
        except KeyboardInterrupt:
            self.axon.stop()
            bt.logging.success("Miner killed by keyboard interrupt.")
            exit()

        # In case of unforeseen errors, the miner will log the error and continue operations.
        except Exception as e:
            bt.logging.error(traceback.format_exc())

    def run_in_background_thread(self):
        """
        Starts the miner's operations in a separate background thread.

        This method is useful for non-blocking operations, allowing the miner to run
        concurrently with other processes.
        """
        if not self.is_running:
            bt.logging.debug("Starting miner in background thread.")
            self.should_exit = False
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            self.is_running = True
            bt.logging.debug("Started")

    def stop_run_thread(self):
        """
        Stops the miner's operations that are running in the background thread.

        This method safely terminates the miner's background operations.
        """
        if self.is_running:
            bt.logging.debug("Stopping miner in background thread.")
            self.should_exit = True
            if self.thread is not None:
                self.thread.join(5)
            self.is_running = False
            bt.logging.debug("Stopped")

    def __enter__(self):
        """
        Starts the miner's operations in a background thread upon entering a context.

        This method facilitates the use of the miner in a 'with' statement.

        Returns:
            self: The BaseMinerNeuron instance.
        """
        self.run_in_background_thread()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stops the miner's background operations upon exiting a context.

        This method facilitates the use of the miner in a 'with' statement.

        Args:
            exc_type: The type of the exception that caused the context to be exited.
            exc_value: The instance of the exception that caused the context to be exited.
            traceback: A traceback object encoding the stack trace.
        """
        self.stop_run_thread()

    def resync_metagraph(self):
        """
        Resyncs the metagraph and updates the hotkeys and moving averages.

        This method synchronizes the local metagraph with the current state of the network.
        """
        bt.logging.info("resync_metagraph()")

        # Sync the metagraph.
        self.metagraph.sync(subtensor=self.subtensor)
    # [fix/miner-validator-communication]: Added a verify function to validate the miner 
    # is running for the health check
    async def verify(self, synapse: TranslateRequest) -> None: 
        """
        Verifies the incoming synapse request.

        This method checks if the incoming request is a valid Bittensor synapse and sets
        the response accordingly.

        Args:
            synapse (TranslateRequest): The incoming synapse request to verify.
        """     
        bt.logging.debug(f"Verifying synapse of type: {type(synapse)}") 
        if isinstance(synapse, bt.Synapse):
            synapse.response = True
    
                