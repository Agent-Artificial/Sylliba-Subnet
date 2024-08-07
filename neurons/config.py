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
            "full_path": "./neurons/miner.py",
            "events_retention_size": 2 * 1024 * 1024 * 1024,
            "epoch_length": 10,
            "device": "cuda:0",
            "dont_save_events": False,
        },
        "subtensor": {
            "network": os.getenv("BT_NETWORK"),
            "chain_endpoint": "",
            "netuid": os.getenv("BT_NETUID"),
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
            "force_validator_permit": True,
            "allow_non_registered": False,
            "mock": False,
        },
    }


def validator_config():
    return {
        "netuid": os.getenv("BT_NETUID"),
        "axon":{
            "port": os.getenv('BT_AXON_PORT'),
            "ip": os.getenv('BT_AXON_IP'),
            "external_port": os.getenv('BT_AXON_EXTERNAL_PORT'),
            "external_ip": os.getenv('BT_AXON_EXTERNAL_IP'),
            "max_workers": os.getenv('BT_AXON_MAX_WORERS'),
        },
            
        "logging": {
            "logging_dir": "~/.bittensor/logs",
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
            "full_path": "./neurons/validator.py",
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
            "netuid": os.getenv("BT_NETUID"),
            "mock": False,
        },
    }
