from bittensor.axon import axon, FastAPIThreadedServer
from template.protocol import ValidatorRequest
import bittensor

class TranslationRequest(ValidatorRequest):
    def __init__(self, data: dict):
        super().__init__()
        self.data = data
        
# Define a custom request forwarding function using your synapse class
    def forward( synapse: ValidatorRequest ) -> ValidatorRequest:
        # Apply custom logic to synapse and return it
        synapse.validator_request = synapse.data
        return synapse

    # Define a custom request verification function
    def verify_my_synapse( synapse: MySyanpse ):
        # Apply custom verification logic to synapse
        # Optionally raise Exception
        assert synapse.input == 1
        ...

        # Define a custom request blacklist fucntion
        def blacklist_my_synapse( synapse: MySyanpse ) -> bool:
            # Apply custom blacklist
            return False ( if non blacklisted ) or True ( if blacklisted )

        # Define a custom request priority fucntion
        def prioritize_my_synape( synapse: MySyanpse ) -> float:
            # Apply custom priority
            return 1.0

        # Initialize Axon object with a custom configuration
        my_axon = bittensor.axon(
            config=my_config,
            wallet=my_wallet,
            port=9090,
            ip="192.0.2.0",
            external_ip="203.0.113.0",
            external_port=7070
        )

        # Attach the endpoint with the specified verification and forward functions.
        my_axon.attach(
            forward_fn = forward_my_synapse,
            verify_fn = verify_my_synapse,
            blacklist_fn = blacklist_my_synapse,
            priority_fn = prioritize_my_synape
        )

        # Serve and start your axon.
        my_axon.serve(
            netuid = ...
            subtensor = ...
        ).start()

        # If you have multiple forwarding functions, you can chain attach them.
        my_axon.attach(
            forward_fn = forward_my_synapse,
            verify_fn = verify_my_synapse,
            blacklist_fn = blacklist_my_synapse,
            priority_fn = prioritize_my_synape
        ).attach(
            forward_fn = forward_my_synapse_2,
            verify_fn = verify_my_synapse_2,
            blacklist_fn = blacklist_my_synapse_2,
            priority_fn = prioritize_my_synape_2
        ).serve(
            netuid = ...
            subtensor = ...
        ).start()