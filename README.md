<div align="center">

# **Sylliba Subnet** <!-- omit in toc -->
[![Bittensor Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
</div>

# Sylliba
**Sylliba** is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate many languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.

As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.

Explore Sylliba and experience the future of translation [here](https://agentartificial.com/)

## Features

**Multi-Language Support:** Translate many languages.
Versatile Input and Output: Handles both audio and text formats.

**Bittensor Integration:** Connects to our AI-driven network for enhanced capabilities.

**User-Friendly Interface:** Designed to be easy to use for everyone.

---

## Contribution Guidelines
We welcome contributions from the community to help us improve Sylliba. Please fork this repo and create a PR with your changes for us to review.

# Installation



There are multiple ways to launch our miner or validator.  Choose what works best for you!

**MINIMUM HARDWARE REQUIREMENTS:**
Miner: 4 CPU Cores, 16GB RAM, 10GB Disk Space and at least an 8GB GPU
Validator: 4 CPU Cores, 16GB RAM, 20GB Disk Space and at least an 10GB GPU 

## Option 1: Local Python Install

This approach installs directly on your linux server.

**SOFTWARE REQUIREMENTS:** Python3, venv, git, nvidia driver

You can run the following commands in your console to install the Sylliba Subnet:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Agent-Artificial/Sylliba-Subnet.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Sylliba-Subnet
   ```

3. **Create a Python virtual environment:**
   (if you prefer to use Anaconda or Poetry use that)
   ```bash
   python3 -m venv .venv
   ```

4. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

5. **Copy the environment variables template:**
   ```bash
   cp .env.example .env
   ```

6. **Set up the environment variables**  
   Edit the `.env` file and configure the necessary values.  (You do not need to fill in the validator parts if you are only running a miner.)

7. **Install the required dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

### Serving
Finally you can serve the miner or validator with the following command. 

1. **Running a validator:**
   ```bash
   python3 neurons/validator.py --logging.debug
   ```

2. **Running a miner:**
   ```bash
   python3 neurons/miner.py --logging.debug
   ```

Continue on to the Registering section down below

## Option 2: Building a Docker Container

This approach runs a miner or validator in a container built on your server (Windows (WSL), Linux or Mac).

**SOFTWARE REQUIREMENTS:** Docker, Docker Compose, git, nvidia driver and nvidia docker runtime

You can run the following commands in your console to install the Sylliba Subnet:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Agent-Artificial/Sylliba-Subnet.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Sylliba-Subnet
   ```

3. **Copy the environment variables template:**
   ```bash
   cp .env.example .env
   ```

4. **Set up the environment variables**  
   Edit the `.env` file and configure the necessary values.  (You do not need to fill in the validator parts if you are only running a miner.)

5. **Docker Compose Build:**
   ```bash
   docker compose build
   ```

6a. **Miner - Docker Compose Up:**
   ```bash
   docker compose -f docker-compose-miner.yml up -d 
   ```

6b. **Validator - Docker Compose Up:**
   ```bash
   docker compose -f docker-compose-validator.yml up -d 
   ```

### Helpful Tips:

To view your container's log:
   ```bash
   docker container logs -f sylliba-subnet-miner-1
   ```
   or
   ```bash
   docker container logs -f sylliba-subnet-validator-1
   ```   
   Type ctrl+c to exit


## Registering
You can register a key for use with a miner or validator by executing following commands. Registering lets the block chain and the validator know that you are are going to be available to provide the service on the chain.

1. **Registering a validator:**
   Use ```--subtensor.network finney and --netuid #``` for mainnet if you wish to deploy there
   ```bash
   btcli subnet register --subtensor.network test --netuid 197 --wallet.name YOUR_VALIDATOR_COLDKEY --wallet.hotkey YOUR_VALIDATOR_HOTKEY
   ```

2. **Registering a miner:**
   Use ```--subtensor.network finney and --netuid #``` for mainnet if you wish to deploy there
   ```bash
   btcli subnet register --subtensor.network test --netuid 197 --wallet.name YOUR_MINER_COLDKEY --wallet.hotkey YOUR_MINER_HOTKEY
   ```

## Running Multiple Miners

### Using PM2
To run multiple miners without docker you can run this command multiple times, once for each miner.

```bash
pm2 start neurons/miner.py --name sylliba-miner --interpreter python3 -- --logging.debug --axon.port [port for new miner] --axon.external_port [port for new miner] --wallet.coldkey [coldkey for new miner] --wallet.hotkey [hotkey for new miner]
```

### Using Docker
Run multiple miners via Docker Compose.  

1. Step 1
Navigate to the ./docker-multi-miner folder

2. Make a .env# for every miner you want.  Example, copy .env1.example to .env1, then .env2.example to env2.  All of the .env#.example are identical so make as many as you need with the specific miner information.

3. Edit the docker-compose.yml file.  The one that is there has three miners.  To add more just copy one of them and paste below editing the name (i.e. mine4 to miner4) and the .env file (i.e. .env3 to .env4)

4. Run this command to launch all of the miners in containers: 
```bash
docker compose up -d 
```

---


## License
This repository is licensed under the MIT License.
```text
# The MIT License (MIT)
# Copyright © 2024 Opentensor Foundation

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
```
