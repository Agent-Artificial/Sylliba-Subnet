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
            "path": os.getenv("BT_WALLET_PATH", '~/.bittensor/wallets'),
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
            "network": os.getenv("BT_NETWORK", 'test'),
            "chain_endpoint": "",
            "mock": False,
        },
        "netuid": int(os.getenv("BT_NETUID", 197)),
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
            "port": int(os.getenv('BT_AXON_MINER_PORT', 9197)),
            "ip": os.getenv('BT_AXON_MINER_IP', '0.0.0.0'),
            "external_port": int(os.getenv('BT_AXON_MINER_EXTERNAL_PORT', 9197)),
            "external_ip": os.getenv('BT_AXON_MINER_EXTERNAL_IP', '0.0.0.0'),
            "max_workers": int(os.getenv('BT_AXON_MAX_WORERS', 5)),
        },
    }


def validator_config():
    return {
        "netuid": int(os.getenv("BT_NETUID", 197)),
        "axon":{
            "port": int(os.getenv('BT_AXON_VALIDATOR_PORT', 9198)),
            "ip": os.getenv('BT_AXON_VALIDATOR_IP', '0.0.0.0'),
            "external_port": int(os.getenv('BT_AXON_VALIDATOR_EXTERNAL_PORT', 9198)),
            "external_ip": os.getenv('BT_AXON_VALIDATOR_EXTERNAL_IP', '0.0.0.0'),
            "max_workers": int(os.getenv('BT_AXON_MAX_WORERS', 5)),
        },
            
        "logging": {
            "logging_dir": "~/.bittensor/logs",
        },
        "wallet": {
            "name": os.getenv("BT_VALIDATOR_COLDKEY"),
            "hotkey": os.getenv("BT_VALIDATOR_HOTKEY"),
            "path": os.getenv("BT_WALLET_PATH", '~/.bittensor/wallets'),
        },
        "neuron": {
            "name": os.getenv("BT_VALIDATOR_COLDKEY"),
            "timeout": 10,
            "num_concurrent_forwards": 1,
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
            "network": os.getenv("BT_NETWORK", 'test'),
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
            "netuid": int(os.getenv("BT_NETUID", 197)),
            "mock": False,
        },
        "api_port": int(os.getenv("SUBNET_API_PORT", 8080)),
    }
