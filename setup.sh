#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

sudo apt install -y make build-essential git clang curl libssl-dev llvm libudev-dev protobuf-compiler tmux libsndfile1-dev

python -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install setuptools wheel
pip install -r requirements.txt

read -p "Enter your network: " BT_NETWORK
read -p "Enter your subnet netuid: " BT_NETUID
read -p "Enter your miner PORT: " BT_AXON_PORT
read -p "Enter your miner IP: " BT_AXON_IP
read -p "Enter your miner external PORT: "  BT_AXON_EXTERNAL_PORT
read -p "Enter your miner external IP: " BT_AXON_EXTERNAL_IP
read -p "Enter your miner max workers: " BT_AXON_MAX_WORERS
read -p "Enter your miner coldkey: " BT_MINER_COLDKEY
read -p "Enter your miner hotkey: " BT_MINER_HOTKEY
read -p "Enter your validator coldkey: " BT_VALIDATOR_COLDKEY
read -p "Enter your validator hotkey: " BT_VALIDATOR_HOTKEY
read -p "Enter your wallet path: " BT_WALLET_PATH
read -p "Enter your text_inference url: " INFERENCE_URL
read -p "Enter your text_inference api key: " INFERENCE_API_KEY

cat <<EOF > .env
BT_NETWORK="$BT_NETWORK"
BT_NETUID=$BT_NETUID
BT_AXON_PORT=$BT_AXON_PORT
BT_AXON_IP="$BT_AXON_IP"
BT_AXON_EXTERNAL_PORT=$BT_AXON_EXTERNAL_PORT
BT_AXON_EXTERNAL_IP="$BT_AXON_EXTERNAL_IP"
BT_AXON_MAX_WORERS=$BT_AXON_MAX_WORERS
BT_MINER_COLDKEY="$BT_MINER_COLDKEY"
BT_MINER_HOTKEY="$BT_MINER_HOTKEY"
BT_VALIDATOR_COLDKEY="$BT_VALIDATOR_COLDKEY"
BT_VALIDATOR_HOTKEY="$BT_VALIDATOR_HOTKEY"
BT_WALLET_PATH="$BT_WALLET_PATH"
INFERENCE_URL="$INFERENCE_URL"
INFERENCE_API_KEY="$INFERENCE_API_KEY"
EOF


rm -r modules/translation

python -m modules.install_module translation

