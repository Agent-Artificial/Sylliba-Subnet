import os
from bittensor.axon import axon, FastAPIThreadedServer
from bittensor import config
from sylliba.protocol import ValidatorRequest
import bittensor
from dotenv import load_dotenv

load_dotenv()

config = config.axon_config()

class TranslationRequest(ValidatorRequest):
    def __init__(self, data: dict):
        super().__init__()
        self.data = data
        self.blacklisted = []
        self.fast_server = FastAPIThreadedServer(config)
        
# Define a custom request forwarding function using your synapse class
    def forward(synapse: ValidatorRequest) -> ValidatorRequest:
        # Apply custom logic to synapse and return it
        synapse.validator_request = synapse.data
        return synapse

    # Define a custom request verification function
    def verify_my_synapse(synapse: ValidatorRequest):
        # Apply custom verification logic to synapse
        # Optionally raise Exception
        assert synapse.validator_request is not None

        # Define a custom request blacklist fucntion
        def blacklist_my_synapse(synapse: ValidatorRequest) -> bool:
            # Apply custom blacklist
            if synapse.validator_request is not None:
                return False
            return True

        # Define a custom request priority fucntion
        def prioritize_my_synape(synapse: ValidatorRequest) -> float:
            # Apply custom priority
            return 1.0

        # Initialize Axon object with a custom configuration
        my_axon = bittensor.axon(
            config=config,
            wallet=bittensor.wallet(
                name=os.getenv("WALLET_NAME"),
                config=config,
                hotkey=os.getenv("WALLET_HOTKEY", "default"),
                path=os.getenv("WALLET_PATH", "default"),
            ),
            port=os.getenv("AXON_PORT", 7070),
            ip="192.0.2.0",
            external_ip="203.0.113.0",
            external_port=7070
        )

        # Attach the endpoint with the specified verification and forward functions.
        my_axon.attach(
            forward_fn=synapse.forward,
            verify_fn=synapse.verify,
            blacklist_fn=blacklist_my_synapse,
            priority_fn=prioritize_my_synape
        )

        # Serve and start your axon.
        my_axon.serve(
            netuid = int(os.getenv("BT_NETUID")),
            subtensor = bittensor.subtensor(int(os.getenv("BT_NETUID")), config=config),
            ).start()