from bittensor.axon import axon, FastAPIThreadedServer
from template.protocol import ValidatorRequest
import os
import bittensor
from dotenv import load_dotenv

load_dotenv()


class TranslationRequest(ValidatorRequest):
    def __init__(self, data: dict):
        super().__init__()
        self.data = data
        
# Define a custom request forwarding function using your synapse class
    def forward(synapse: ValidatorRequest) -> ValidatorRequest:
        # Apply custom logic to synapse and return it
        synapse.validator_request = synapse.data
        return synapse

    # Define a custom request verification function
    def verify_my_synapse(self, synapse: ValidatorRequest):
        assert synapse.validator_request

        # Define a custom request blacklist fucntion
        def blacklist_my_synapse(synapse: ValidatorRequest) -> bool:
            # Apply custom blacklist
            return False if synapse.blacklisted else True

        # Define a custom request priority fucntion
        def prioritize_my_synape(synapse: ValidatorRequest) -> float:
            # Apply custom priority
            return 1.0

        # Initialize Axon object with a custom configuration
        my_axon = bittensor.axon(
            config=self.model_config,
            wallet=self.wallet,
            port=os.getenv("BT_AXON_PORT"),
            ip=os.getenv("BT_AXON_IP"),
            external_ip=os.getenv("BT_AXON_EXTERNAL_IP"),
            external_port=os.getenv("BT_AXON_EXTERNAL_PORT"),
        )

        # Attach the endpoint with the specified verification and forward functions.
        my_axon.attach(
            forward_fn=self.forward,
            verify_fn=self.verify_my_synapse,
            blacklist_fn=blacklist_my_synapse,
            priority_fn=prioritize_my_synape
        )

        # Serve and start your axon.
        my_axon.serve(
            netuid=os.getenv("BT_NETUID"),
            subtensor=bittensor.subtensor(
                config=self.config["subtensor"]
            )
        ).start()

        return synapse