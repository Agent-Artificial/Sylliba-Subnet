#!/bin/bash

source .venv/bin/activate
source .env

echo $BT_VALIDATOR_COLDKEY

read -p "Launching a miner or a validator? (m/v): " REPLY

if [[ $REPLY =~ ^[Mm]$ ]]
then 
    btcli subnet register --netuid $BT_NETUID --subtensor.network "$BT_NETWORK" --wallet.name "$BT_MINER_COLDKEY" --wallet.hotkey "$BT_MINER_HOTKEY"
elif [[ $REPLY =~ ^[Vv]$ ]]
then
    btcli subnet register --netuid $BT_NETUID --subtensor.network "$BT_NETWORK" --wallet.name "$BT_VALIDATOR_COLDKEY" --wallet.hotkey "$BT_VALIDATOR_HOTKEY"
else
    echo "Invalid input"
fi