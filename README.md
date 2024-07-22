<div align="center">

# **Bittensor Subnet Template** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

---

## Install
You can run the setup script if you're on linux using the commands
`chmod -x setup.sh`
`bash setup.sh`

Follow the prompt and the script will walk you through setting up your environment. Make sure that the config values are filled. If you'd rather fill them out manually you can find the configs in neurons/config.py. 

## Registering
Once installed you can register the miner or validator by using the register script. Registering lets the block chain and the validator know that you are are going to be available to provide the service on the chain.
`chmod -x register.sh`
`bash register.sh`

## Serving
Finally you can serve the miner or validator with the launch script. 
`bash launch.sh`

## Manual Install

If you would like to manually install the library you can follow these steps.

### Setup your environment
You can skip these steps if you already have the required installed.
`sudo apt update && sudo apt upgrade -y`
`sudo apt install make build-essential git clang curl libssl-dev llvm libudev-dev protobuf-compiler tmux libsndfile1-dev python3 python3-dev python3-venv python3-pip python-is-python3`
`python -m venv .venv`
`source .venv/bin/activate`

`cp .env.example .env`

Fill out the .env file with the correct configuration information

### Setup pip
`python -m pip install --upgrade pip`
`pip install setuptools wheel`
`pip install -r requirements.txt`

### Install module
`rm -r modules/translation/seamless`
`python -m modules.install_module translation`

### Register Miner/Validator
`btcli subnet register --netuid "$BT_NETUID" --subtensor.network "$BT_NETUID" --wallet.name "$BT_VALIDATOR_COLDKEY" --wallet.hotkey "$BT_VALIDATOR_HOTKEY"`


### Launch Validator/Miner
sbtcli subnet register --netuid "$BT_NETUID" --subtensor.network "$BT_NETUID" --wallet.name "$BT_VALIDATOR_COLDKEY" --wallet.hotkey "$BT_VALIDATOR_HOTKEY"