# Sylliba
**Sylliba** is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate in over 76 languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.

As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.

Explore Sylliba and experience the future of translation [here](https://sylliba.agentartificial.com/)

## Features

**Multi-Language Support:** Translate over 76 languages.
Versatile Input and Output: Handles both audio and text formats.

**Bittensor Integration:** Connects to our AI-driven network for enhanced capabilities.

**User-Friendly Interface:** Designed to be easy to use for everyone.

---

## Contribution Guidelines
We welcome contributions from the community to help us improve Sylliba. Here’s how you can get involved:

### Install
You can run the setup script if you're on linux using the commands
`chmod -x setup.sh`
`bash setup.sh`

Follow the prompt and the script will walk you through setting up your environment. Make sure that the config values are filled. If you'd rather fill them out manually you can find the configs in neurons/config.py. 

### Registering
Once installed you can register the miner or validator by using the register script. Registering lets the block chain and the validator know that you are are going to be available to provide the service on the chain.
`chmod -x register.sh`
`bash register.sh`

### Serving
Finally you can serve the miner or validator with the launch script. 
`bash launch.sh`

## Manual Install

If you would like to manually install the library you can follow these steps.

### Setup your environment
You can skip these steps if you already have the required installed.
```
sudo apt update && sudo apt upgrade -y
```
```
sudo apt install make build-essential git clang curl libssl-dev llvm libudev-dev protobuf-compiler libsndfile1-dev python3 python3-dev python3-venv python3-pip python-is-python3
```
```
python -m venv .venv
```
```
source .venv/bin/activate
```

```
cp .env.example .env
```

Fill out the .env file with the correct configuration information

### Setup pip
```
python -m pip install --upgrade pip
```
```
pip install setuptools wheel
```
```
pip install -r requirements.txt
```

### Install module
```
rm -r modules/translation/seamless
```
```
python -m modules.install_module translation
```

### Register Miner/Validator
```
btcli subnet register --netuid "$BT_NETUID" --subtensor.network "$BT_NETUID" --wallet.name "$BT_VALIDATOR_COLDKEY" --wallet.hotkey "$BT_VALIDATOR_HOTKEY"
```


### Launch Validator/Miner
```
btcli subnet register --netuid "$BT_NETUID" --subtensor.network "$BT_NETUID" --wallet.name "$BT_VALIDATOR_COLDKEY" --wallet.hotkey "$BT_VALIDATOR_HOTKEY"
```

----

## Contribution Guidelines

**Fork the Repository:** Click the "Fork" button on the upper right corner of the repository page.
**Clone Your Fork:** Clone your forked repository to your local machine.

```
git clone https://github.com/agent-artificial/sylliba-subnet.git
```
**Create a Branch:** Create a new branch for your feature or bug fix.
```
git checkout -b feature/your-feature-name
```
**Make Your Changes:** Implement your feature or bug fix.


**Commit Your Changes:** Commit your changes with a descriptive commit message.
```
git commit -m "Add feature: your-feature-name"
```
**Push to Your Fork:** Push your changes to your forked repository.

```
git push origin feature/your-feature-name
```
**Create a Pull Request:** Open a pull request to the main repository. Provide a clear description of your changes and any related issue numbers.

----

## Bug Report Guidelines
Encounter any issues or bugs? Here’s how to report them:

**Check for Duplicates:** Before reporting a bug, check the issues to see if it has already been reported.

**Create a New Issue:** If the bug hasn't been reported, create a new issue with the following details:

- **Title:** A concise title for the bug.

- **Description:** A detailed description, including steps to reproduce, expected behavior, and actual behavior.

- **Screenshots/Logs:** Any relevant screenshots or log files to help diagnose the issue.

**Submit:** Submit the issue, and our team will review it as soon as possible.
