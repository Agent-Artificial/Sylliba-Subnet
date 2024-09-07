import os
from dotenv import load_dotenv

load_dotenv()


def miner_config():
    return {
        "logging": {
            "logging_dir": "~/.bittensor/miners",
        },
        "wallet": {
            "name": os.getenv("BT_MINER_COLDKEY"),
            "hotkey": os.getenv("BT_MINER_HOTKEY"),
            "path": os.getenv("BT_WALLET_PATH"),
        },
        "neuron": {
            "name": os.getenv("BT_MINER_COLDKEY"),
            "full_path": "~/mining/bittensor/bittensor-subnet-template/neurons/miner.py",
            "events_retention_size": 2 * 1024 * 1024 * 1024,
            "epoch_length": 10,
            "device": "cuda:0",
            "dont_save_events": False,
        },
        "subtensor": {
            "network": os.getenv("BT_NETWORK"),
            "chain_endpoint": "",
            "mock": False,
        },
        "netuid": int(os.getenv("BT_NETUID")),
        "wandb": {
            "off": True,
            "offline": False,
            "notes": "",
            "project_name": "",
            "entity": "",
        },
        "blacklist": {
            "force_validator_permit": True,
            "allow_non_registered": False,
            "mock": False,
        },
        "axon":{
            "port": int(os.getenv('BT_AXON_MINER_PORT')),
            "ip": os.getenv('BT_AXON_MINER_IP'),
            "external_port": int(os.getenv('BT_AXON_MINER_EXTERNAL_PORT')),
            "external_ip": os.getenv('BT_AXON_MINER_EXTERNAL_IP'),
            "max_workers": int(os.getenv('BT_AXON_MAX_WORERS')),
        },
    }


def validator_config():
    return {
        "netuid": int(os.getenv("BT_NETUID")),
        "axon":{
            "port": int(os.getenv('BT_AXON_VALIDATOR_PORT')),
            "ip": os.getenv('BT_AXON_VALIDATOR_IP'),
            "external_port": int(os.getenv('BT_AXON_VALIDATOR_EXTERNAL_PORT')),
            "external_ip": os.getenv('BT_AXON_VALIDATOR_EXTERNAL_IP'),
            "max_workers": int(os.getenv('BT_AXON_MAX_WORERS')),
        },
            
        "logging": {
            "logging_dir": "~/.bittensor/validators",
        },
        "wallet": {
            "name": os.getenv("BT_VALIDATOR_COLDKEY"),
            "hotkey": os.getenv("BT_VALIDATOR_HOTKEY"),
            "path": os.getenv("BT_WALLET_PATH"),
        },
        "neuron": {
            "name": os.getenv("BT_VALIDATOR_COLDKEY"),
            "timeout": 10,
            "num_concurrent_forwards": 10,
            "sample_size": 50,
            "disable_set_weights": False,
            "moving_average_alpha": 0.1,
            "axon_off": False,
            "vpermit_tao_limit": 4096,
            "full_path": "~/mining/bittensor/bittensor-subnet-template/neurons/validator.py",
            "events_retention_size": 2 * 1024 * 1024 * 1024,
            "epoch_length": 10,
            "device": "cuda:0",
            "dont_save_events": False,
        },
        "subtensor": {
            "chain_endpoint": "",
            "network": os.getenv("BT_NETWORK"),
            "mock": False,
        },
        "wandb": {
            "off": True,
            "offline": False,
            "notes": "",
            "project_name": "",
            "entity": "",
        },
        "blacklist": {
            "force_validator_permit": False,
            "allow_non_registered": False,
            "netuid": int(os.getenv("BT_NETUID")),
            "mock": False,
        },
    }
