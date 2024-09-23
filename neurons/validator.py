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

import asyncio
import time
import os
import requests
import random
# Bittensor
import bittensor as bt

import base64
import io
import torch
from importlib import import_module

# import base validator class which takes care of most of the boilerplate
from sylliba.base.validator import BaseValidatorNeuron
# Bittensor Validator Template:
from sylliba.validator import forward
from neurons.config import validator_config
from sylliba.protocol import ValidatorRequest
from sylliba.protocol import TranslateRequest
from modules.translation.translation import Translation
from modules.translation.data_models import TranslationRequest
from dotenv import load_dotenv
from sylliba.validator import reward_text, reward_speech

from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import json

from neurons.utils.serialization import audio_encode, audio_decode

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
    "modules.llms.flan_t5_large"
]
TTS : list[str] = [
    "modules.tts.seamless"
]

translation = Translation()
        

class Validator(BaseValidatorNeuron):
    """
    Your validator neuron class. You should use this class to define your validator's behavior. In particular, you should replace the forward function with your own logic.

    This class inherits from the BaseValidatorNeuron class, which in turn inherits from BaseNeuron. The BaseNeuron class takes care of routine tasks such as setting up wallet, subtensor, metagraph, logging directory, parsing config, etc. You can override any of the methods in BaseNeuron if you need to customize the behavior.

    This class provides reasonable default behavior for a validator such as keeping a moving average of the scores of the miners and using them to set weights at the end of each epoch. Additionally, the scores are reset for new hotkeys at the end of each epoch.
    """

    def __init__(self, config=None):
        super(Validator, self).__init__(config=validator_config())
        self.total_miners = len(self.metagraph.uids)
        self.validated = set()
        self.batch_size = 3
        self.current_index = 0
        self.current_batch = self.get_batch(self.batch_size)
        bt.logging.info("load_state()")
        self.now = time.time()
        self.load_state()
        
    async def process(self, synapse_query, serialize = True):
        # bt.logging.info(f"synapse_query:{synapse_query}")
        try:
            return await translation.process(synapse_query, serialize)
        except Exception as e:
            bt.logging.error(f"Error processing translation request {e}. \n{synapse_query}")
            return ""

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

        # Generating the query
        successful = []
        sample_request = await self.generate_query(target_language, source_language, task_string, topic)

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
    
        axons = self.metagraph.axons
        synapse = TranslateRequest(
            translation_request=translation_request,
        )
        try:
            # for i in range(5):
                # batch = self.get_batch(self.batch_size)
                # bt.logging.info(f"batch:{batch}")
                responses = await self.dendrite(
                    axons=axons,
                    synapse=synapse,
                    deserialize=False,
                    timeout=300
                )
                # Getting the responses
                for j in range(0, len(responses)):
                    if responses[j].miner_response is not None:
                        if task_string.endswith('speech'):
                            miner_output_data = audio_decode(responses[j].miner_response)
                        else:
                            miner_output_data = responses[j].miner_response
                            
                        bt.logging.info(f'DECODED OUTPUT DATA: {miner_output_data}')
                        
                        successful.append([miner_output_data, j])
                    else:
                        bt.logging.warning(f"Miner {j} failed to respond.")
        except Exception as e:
            bt.logging.error(f"Failed to query miners with exception: {e}")
        # Rewarding the miners
        bt.logging.info(f"successful:{successful}")
        results = []
        for i in range(len(successful)):
            results.append([successful[i][1], self.process_validator_output(successful[i][0], sample_request['output'], task_string)])
            # Updating the scores
            self.update_scores(results[i][1], results[i][0])
        # Set weights
        self.now = time.time()
        if self.now % 10 == 0:
            self.set_weights()
        
    def process_validator_output(self, miner_response, sample_outputs, task_string):
        if task_string.endswith('text'):
            scores = [reward_text(miner_response, sample_output) for sample_output in sample_outputs]
        else:
            scores = [reward_speech(miner_response, sample_output) for sample_output in sample_outputs]
        return sum(scores) / len(scores)
    
    def generate_input_data(self, llm, topic, source_language):
        messages = [{"role": "system", "content": f"""
                You are an expert story teller.
                You can write short stories that capture the imagination, 
                end readers on an adventure and complete an alegorical thought all within 100~200 words. 
                Please write a short story about {topic} in {source_language}. 
                Keep the story short but be sure to use an alegory and complete the idea."""}]
        return llm.process(messages)

    def generate_output_data(self, llm, input_data, source_language, target_language):
        messages = [
            {"role": "system", "content": f"""
                Provided text is written in {source_language}.
                Please translate into {target_language}
                Don't put any tags, description or decorators.
                Write only translated text in raw text format.
                """},
            {"role": "user", "content": input_data}
        ]
        return llm.process(messages)
    
    def select_random_module(self, modules):
        return import_module(random.choice(modules))
    
    async def generate_query(self, target_language: str, source_language: str, task_string: str, topic: str):
        llm = self.select_random_module(LLMS)
        tts = self.select_random_module(TTS)

        input_data = self.generate_input_data(llm, topic, source_language)

        outputs = []

        for llm_module in LLMS:
            llm = import_module(llm_module)
            
            output_data = self.generate_output_data(llm, input_data, source_language, target_language)

            if task_string.endswith("speech"):
                output_data = tts.process(output_data, target_language)
            outputs.append(output_data)
            
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
