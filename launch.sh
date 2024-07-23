#!/bin/bash

source .venv/bin/activate
source .env

read -p "Launching a miner or a validator? (m/v) " -n 1 -r

if [[ $REPLY =~ ^[Mm]$ ]]
then
    python neurons/miner.py --netuid $BT_NETUID --subtensor.network "$BT_NETWORK" --wallet.name "$BT_MINER_COLDKEY" --wallet.hotkey "$BT_MINER_HOTKEY" --logging.debug

elif [[ $REPLY =~ ^[Vv]$ ]]
then
    python neurons/validator.py --netuid $BT_NETUID --subtensor.network "$BT_NETWORK" --wallet.name "$BT_VALIDATOR_COLDKEY" --wallet.hotkey "$BT_VALIDATOR_HOTKEY" --logging.debug
else
    echo "Invalid input"
fi


