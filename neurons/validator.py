# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

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

import time
import random
# Bittensor
import bittensor as bt
import numpy as np

from importlib import import_module

# import base validator class which takes care of most of the boilerplate
from sylliba.base.validator import BaseValidatorNeuron
# Bittensor Validator Template:
from sylliba.utils.uids import get_miner_uids
from sylliba.protocol import TranslateRequest, HealthCheck
from modules.translation.data_models import TranslationRequest
from dotenv import load_dotenv
from sylliba.validator import reward_text, reward_speech
from neurons.utils.audio_save_load import _wav_to_tensor, _tensor_to_wav
import json
import argparse
import yaml
import os

from neurons.utils.serialization import audio_encode, audio_decode
import wandb
from datetime import datetime

load_dotenv()

TASK_STRINGS = [
    "text2text",
    "text2speech",
    "speech2text",
    "speech2speech",
]

TARGET_LANGUAGES = [
    "English",
    "French",
    "Spanish",
    "German",
    "Italian"
]

TOPICS = [
    "Time travel mishap",
    "Unexpected inheritance",
    "Last day on Earth",
    "Secret underground society",
    "Talking animal companion",
    "Mysterious recurring dream",
    "Alien first contact",
    "Memory-erasing technology",
    "Haunted antique shop",
    "Parallel universe discovery"
]

LLMS : list[str] = [
    "modules.llms.llama",
    # "modules.llms.flan_t5_large"
]

TTS : list[str] = [
    "modules.tts.seamless"
]

MODELS: dict = {
}

PROMPTS: dict = {
    "GENERATE_INPUT_DATA": """You are an expert story teller.
You can write short stories that capture the imagination, 
end readers on an adventure and complete an alegorical thought all within 100~200 words. 
Please write a short story about {topic} in {source_language}. 
Keep the story short but be sure to use an alegory and complete the idea.""",
    "GENERATE_OUTPUT_DATA": """
Provided text is written in {source_language}.
Please translate into {target_language}
Don't put any tags, description or decorators.
Write only translated text in raw text format.
"""}

class Validator(BaseValidatorNeuron):
    """
    Your validator neuron class. You should use this class to define your validator's behavior. In particular, you should replace the forward function with your own logic.

    This class inherits from the BaseValidatorNeuron class, which in turn inherits from BaseNeuron. The BaseNeuron class takes care of routine tasks such as setting up wallet, subtensor, metagraph, logging directory, parsing config, etc. You can override any of the methods in BaseNeuron if you need to customize the behavior.

    This class provides reasonable default behavior for a validator such as keeping a moving average of the scores of the miners and using them to set weights at the end of each epoch. Additionally, the scores are reset for new hotkeys at the end of each epoch.
    """
    def get_config():

        parser = argparse.ArgumentParser()

        parser.add_argument("--dev", action=argparse.BooleanOptionalAction)
        parser.add_argument("--api_port", type=int, default=8080, help="Port for the API")

        bt.subtensor.add_args(parser)
        bt.logging.add_args(parser)
        bt.wallet.add_args(parser)
        bt.axon.add_args(parser)

        config = bt.config(parser)
        bt.logging.info(config)

        dev = config.dev
        if dev:
            dev_config_path = "validator.yml"
            if os.path.exists(dev_config_path):
                with open(dev_config_path, 'r') as f:
                    dev_config = yaml.safe_load(f.read())
                config.update(dev_config)
            else:
                with open(dev_config_path, 'w') as f:
                    yaml.safe_dump(config, f)
        bt.logging.info(config)
        return config

    def __init__(self, config=None):
        super(Validator, self).__init__(config=Validator.get_config())
        self.total_miners = len(self.metagraph.uids)
        self.validated = set()
        self.batch_size = 3
        self.current_index = 0
        self.current_batch = self.get_batch(self.batch_size)
        bt.logging.info("load_state()")
        self.now = time.time()
        self.load_state()
        self.init_wandb()
        
    def __del__(self):
        if self.wandb_run is not None:
            self.wandb_run.finish()
    
    def init_wandb(self):
        self.wandb_run = None
        self.wandb_run_start = None
        if not self.config.wandb.off:
            self.new_wandb_run()
    
    def new_wandb_run(self):
        """Creates a new wandb run to save information to."""
        now = datetime.now()
        self.wandb_run_start = now
        run_id = now.strftime("%Y-%m-%d-%H-%M-%S")
        name = f"validator-{self.uid}-{run_id}"
        self.wandb_run = wandb.init(
            project=self.config.wandb.project_name,
            name=name,
            entity=self.config.wandb.entity,
            config={
                "uid": self.uid,
                "run_id": run_id,
                "hotkey": self.wallet.hotkey.ss58_address,
                "type": "validator",
            },
            reinit=True,
        )
        bt.logging.debug(f"Started a new wandb run: {name}")

    def get_batch(self, batchsize):
        batch = []
        for _ in range(batchsize):
            if len(self.validated) == self.total_miners:
                self.reset()
                
            while self.current_index in self.validated:
                self.current_index = (self.current_index + 1) % self.total_miners
            self.validated.add(self.current_index)
            batch.append(self.current_index)
            self.current_index = (self.current_index + 1) % self.total_miners
        return batch
    
    def reset(self):
        self.validated.clear()
        self.current_index = 0
    
    def get_progress(self):
        return f"{len(self.validated)}/{self.total_miners} miners validated"
                
    async def forward(self):
        source_language = "English"
        target_language = random.choice(TARGET_LANGUAGES)
        task_string = random.choice(TASK_STRINGS)
        topic = random.choice(TOPICS)

        bt.logging.info('Start forward on Validator')

        # Generating the query
        sample_request = await self.generate_query(target_language, source_language, task_string, topic)
        bt.logging.debug(f"sample_request: {str(sample_request)}")

        if task_string.startswith('speech'):
            try:
                miner_input_data = audio_encode(sample_request['input'])
            except Exception as e:
                bt.logging.error(f"Error encoding audio: {str(e)}")
                miner_input_data = None
        else:
            miner_input_data = sample_request['input']

        translation_request = TranslationRequest(data = {
                    "input": miner_input_data,
                    "task_string": task_string,
                    "source_language": source_language,
                    "target_language": target_language
                })
    
        miner_uids = get_miner_uids(self)
        miner_axons = [self.metagraph.axons[uid] for uid in miner_uids]
        bt.logging.debug(f"Miner axons are {miner_axons}")
        # healthcheck = await self.dendrite(
        #         axons=[self.metagraph.axons[uid] for uid in miner_uids],
        #         synapse=HealthCheck(),
        #         deserialize=False,
        #         timeout=30
        #     )
        # healthy_axons = [axons[i] for i, check in enumerate(healthcheck) if check.response is True]
        # healthy_axon_uids = [i for i, check in enumerate(healthcheck) if check.response is True]
        
        # bt.logging.info(f'Health Axons are {healthy_axons}')
        results = []

        synapse = TranslateRequest(
            translation_request=translation_request,
        )
        try:
            responses = await self.dendrite(
                axons=miner_axons,
                synapse=synapse,
                deserialize=False,
                timeout=300
            )
            bt.logging.debug(f"Received {len(responses)}/{len(miner_axons)} responses.")
            # Processing miner output into rewards
            for j in range(0, len(responses)):
                if responses[j].miner_response is not None:
                    if task_string.endswith('speech'):
                        miner_output_data = audio_decode(responses[j].miner_response)
                    else:
                        miner_output_data = responses[j].miner_response
                    
                    results.append(
                        float(self.process_validator_output(
                            miner_output_data,
                            sample_request['output'],
                            task_string
                        )) # 'numpy.float64' object cannot be interpreted as integer
                    )
                else:
                    results.append(
                        0
                    )
        except Exception as e:
            bt.logging.error(f"Failed to query miners with exception: {e}")
        
        # Updating the scores
        bt.logging.debug(f"Results: {results}")
        self.update_scores(np.array(results), miner_uids)    
            
        # Set weights
        self.now = time.time()
        if self.now % 10 == 0:
            self.set_weights()
        
    # ? Regardless of the type, this is the "sum" of one and divided by 1?
    # ? Is this so we can come up with more reward functions and add them?
    def process_validator_output(self, miner_response, sample_outputs, task_string):
        if task_string.endswith('text'):
            scores = [reward_text(miner_response, sample_output) for sample_output in sample_outputs]
        else:
            scores = [reward_speech(miner_response, sample_output) for sample_output in sample_outputs]
        return sum(scores) / len(scores)
    
    def generate_input_data(self, llm, topic, source_language, device):
        messages = [{"role": "system", "content": PROMPTS["GENERATE_INPUT_DATA"].format(topic=topic, source_language=source_language)}]
        bt.logging.debug(f"generate_input_data:prompt:{messages}")
        return llm.process(messages, device)

    def generate_output_data(self, llm, input_data, source_language, target_language, device):
        messages = [
            {"role": "system", "content": PROMPTS["GENERATE_OUTPUT_DATA"].format(source_language=source_language, target_language=target_language)},
            {"role": "user", "content": input_data}
        ]
        return llm.process(messages, device)
    
    def select_random_module(self, modules):
        return import_module(random.choice(modules))
    
    async def generate_query(self, target_language: str, source_language: str, task_string: str, topic: str):
        llm = import_module(LLMS[0])
        tts = self.select_random_module(TTS)

        bt.logging.debug(f"generate_query:llm:{llm}")
        bt.logging.debug(f"generate_query:tts:{tts}")
        input_data = self.generate_input_data(llm, topic, source_language, self.device)
        bt.logging.debug(f"generate_query:input_data:{input_data}")

        outputs = []

        for llm_module in LLMS:
            llm = import_module(llm_module)
            
            output_data = self.generate_output_data(llm, input_data, source_language, target_language, self.device)

            if task_string.endswith("speech"):
                output_data = tts.process(output_data, target_language)
            outputs.append(output_data)
        
        bt.logging.info(f'Generated Query Input Text: {input_data}')
        bt.logging.info(f'Generated Query Sample Output Text: {outputs}')

        bt.logging.debug(f"generate_query:outputs:{outputs}")

        bt.logging.debug(f"generate_query:outputs:{outputs}")

        if task_string.startswith("speech"):
            input_data = tts.process(input_data, source_language)
        return {
                    "input": input_data,
                    "output": outputs,
                    "task_string": task_string,
                    "source_language": source_language,
                    "target_language": target_language
                }



# The main function parses the configuration and runs the validator.
if __name__ == "__main__":
    # validator = Validator()
    # validator.run()
    
    with Validator() as validator:
        while True:
            bt.logging.info(f'validator running ... {time.time()}')
            time.sleep(5) 
