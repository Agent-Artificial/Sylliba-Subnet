#!/bin/bash

read -p "Launching a miner or a validator? (m/v) " -n 1 -r

if [[ $REPLY =~ ^[Mm]$ ]]
then
    python3 -m neurons.miner
elif [[ $REPLY =~ ^[Vv]$ ]]
then
    python3 -m neurons.validator
else
    echo "Invalid input"
fi