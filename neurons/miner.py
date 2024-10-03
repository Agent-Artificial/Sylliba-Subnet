# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

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
import json
import time
import typing
import os
import asyncio
from pathlib import Path
from loguru import logger
from importlib import import_module
import bittensor as bt

# Bittensor Miner Template:
import sylliba
# import base miner class which takes care of most of the boilerplate
from sylliba.base.miner import BaseMinerNeuron
from neurons.config import get_miner_config




class Miner(BaseMinerNeuron):
    """
    A specialized miner class for the Sylliba network, focusing on translation tasks.

    This class extends BaseMinerNeuron to provide specific functionality for handling
    translation requests in the Sylliba ecosystem.

    Attributes:
        module (module): The imported translation module for processing requests.
    """

    def __init__(self, config=None, module_name="translation"):
        """
        Initializes the Miner with the given configuration and translation module.

        Args:
            config (Config): Configuration for the miner. Defaults to miner_config().
            module_name (str): Name of the module to import for translation. Defaults to "translation".
        """
        if not config:
            config = get_miner_config()
        super(Miner, self).__init__(config=config)
        logger.info(config)
        logger.info(self.axon.info())
        self.module = import_module('modules.translation.translation')
        self.axon.attach(forward_fn=self.healthcheck)

    async def forward(
        self, synapse: sylliba.protocol.TranslateRequest
    ) -> sylliba.protocol.TranslateRequest:
        """
        Processes incoming translation requests.

        This method handles the core functionality of the miner, processing translation
        requests and returning the results.

        Args:
            synapse (sylliba.protocol.TranslateRequest): The incoming translation request.

        Returns:
            sylliba.protocol.TranslateRequest: The processed synapse with the translation response.
        """
        bt.logging.info(f'synapse received')
        response = await self.module.process(synapse.translation_request)
        synapse.miner_response = response
        bt.logging.info(f"synapse.miner_response : {synapse.miner_response[:100]}")
        return synapse

    async def healthcheck(self, synapse: sylliba.protocol.HealthCheck):
        """
        Performs a health check on the miner.

        This method is used to verify that the miner is operational and responsive.

        Args:
            synapse (sylliba.protocol.HealthCheck): The incoming health check request.

        Returns:
            sylliba.protocol.HealthCheck: The synapse with a positive health check response.
        """
        synapse.response = True
        return synapse

    async def blacklist(
        self, synapse: sylliba.protocol.TranslateRequest
    ) -> typing.Tuple[bool, str]:
        """
        Determines whether an incoming request should be blacklisted.

        This method implements security measures to prevent resource wastage on undesired requests.
        It checks the validity and permissions of the requesting entity before processing the request.

        Args:
            synapse (sylliba.protocol.TranslateRequest): The incoming translation request.

        Returns:
            Tuple[bool, str]: A tuple containing a boolean indicating whether the request is blacklisted,
                              and a string providing the reason for the decision.
        """
        if synapse.dendrite is None or synapse.dendrite.hotkey is None:
            bt.logging.warning("Received a request without a dendrite or hotkey.")
            return True, "Missing dendrite or hotkey"

        # TODO(developer): Define how miners should blacklist requests.
        uid = await self.metagraph.hotkeys.index(synapse.dendrite.hotkey)
        if (
            not self.config.blacklist.allow_non_registered
            and synapse.dendrite.hotkey not in self.metagraph.hotkeys
        ):
            # Ignore requests from un-registered entities.
            bt.logging.trace(
                f"Blacklisting un-registered hotkey {synapse.dendrite.hotkey}"
            )
            return True, "Unrecognized hotkey"

            # If the config is set to force validator permit, then we should only allow requests from validators.
        if not self.metagraph.validator_permit[uid]:
            if self.config.blacklist.force_validator_permit:
                bt.logging.warning(
                    f"Blacklisting a request from non-validator hotkey {synapse.dendrite.hotkey}"
                )
                return True, "Non-validator hotkey"

        bt.logging.trace(
            f"Not Blacklisting recognized hotkey {synapse.dendrite.hotkey}"
        )
        return False, "Hotkey recognized!"

    async def priority(self, synapse: sylliba.protocol.TranslateRequest) -> float:
        """
        Determines the priority of an incoming request.

        This method assigns a priority score to incoming requests based on the calling entity's
        stake in the metagraph. Higher stake results in higher priority.

        Args:
            synapse (sylliba.protocol.TranslateRequest): The incoming translation request.

        Returns:
            float: A priority score for the request, based on the caller's stake.
        """
        if synapse.dendrite is None or synapse.dendrite.hotkey is None:
            bt.logging.warning("Received a request without a dendrite or hotkey.")
            return 0.0
        logger.info(self.metagraph.hotkeys)
        
        # TODO(developer): Define how miners should prioritize requests.
        caller_uid = self.metagraph.hotkeys.index(
            synapse.dendrite.hotkey
        )  # Get the caller index.
        print(caller_uid)
        priority = float(
            self.metagraph.S[caller_uid]
        )  # Return the stake as the priority.
        bt.logging.trace(
            f"Prioritizing {synapse.dendrite.hotkey} with value: {priority}"
        )
        return priority


# This is the main function, which runs the miner.
if __name__ == "__main__":
    """
    Main entry point for running the Miner.

    This section initializes and runs the Miner when the script is executed directly.
    It uses a context manager to ensure proper setup and teardown of the miner.
    """
    with Miner() as miner:
        # [fix/validator-miner-communcation]: move the looping logic into the run function 
        # of the base/miner.py rather than running nested coniditional while loops
        miner.start_miner()
        
        miner.run()

