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

load_dotenv()

TASK_STRINGS = [
    "speech2speech"
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
        target_language = "French"
        task_string = random.choice(TASK_STRINGS)
        topic = random.choice(TOPICS)
        # Generating the query
        successful = []
        sample_request = await self.generate_query(target_language, source_language, task_string, topic)
        # bt.logging.info(f"sample_request: {sample_request}")
        translation_request = TranslationRequest(data = {
                    "input": sample_request['input'],
                    "task_string": sample_request["task_string"],
                    "source_language": sample_request["source_language"],
                    "target_language": sample_request["target_language"]
                })
        # reference_set = await self.process(translation_request)
        # Querying the miners
        # axons = [axon for axon in self.metagraph.axons if axon.uid in self.validated] 
        # axons = self.metagraph.axons
        axons = self.metagraph.axons
        bt.logging.info(f"axons:{axons}")
        synapse = TranslateRequest(
            translation_request=translation_request,
        )
        try:
            for i in range(5):
                batch = self.get_batch(self.batch_size)
                bt.logging.info(f"batch:{batch}")
                responses = await self.dendrite(
                    axons=[axons[i] for i in batch],
                    synapse=synapse,
                    deserialize=False,
                    timeout=300
                )
                for j in range(0, len(responses)):
                    if responses[j].miner_response is not None:
                        bt.logging.info(f"responses from miners {batch[j]}:{responses[j].miner_response[:100]}")
                    else:
                        bt.logging.info(f"responses from miners {batch[j]}:{responses[j].miner_response}")
                # Getting the responses
                for j in range(0, len(responses)):
                    if responses[j].miner_response is not None:
        
                        decoded_data = base64.b64decode(responses[j].miner_response)
                        if translation_request.data['task_string'].endswith('speech'):
                            buffer = io.BytesIO(decoded_data)
                            decoded_data = torch.load(buffer)
                        bt.logging.info(f'DECODED OUTPUT DATA: {decoded_data}')
                        
                        successful.append([decoded_data, batch[j]])
                    else:
                        bt.logging.warning(f"Miner {batch[j]} failed to respond.")
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
        
    def process_validator_output(self, miner_response, sample_output, task_string):
        if task_string.endswith('text'):
            return reward_text(miner_response, sample_output)
        else:
            return reward_speech(miner_response, sample_output)
    
    async def generate_query(self, target_language, source_language, task_string, topic):
        messages = [
            {
                "role": "system",
                "content": f'\
                You are an expert story teller.\
                You can write short stories that capture the imagination, \
                end readers on an adventure and complete an alegorical thought all within 100 words. \
                Please write a short story about {topic}. \
                Keep the story short but be sure to use an alegory and complete the idea. \
                Write story in two languages, those are {source_language} and {target_language}.\
                Return result in JSON format only, without any tags or decoration:\
                {{"{source_language}": "TEXT IN SOURCE LANGUAGE", "{target_language}": "TEXT IN TARGET LANGUAGE"}}'
            }
        ]

        model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
        
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,           # This flag is now part of BitsAndBytesConfig
            bnb_4bit_use_double_quant=True,  # Optional, for double quantization
            bnb_4bit_quant_type="nf4",   # Choose between 'fp4' or 'nf4' (Non-negative quantization)
        )

        # Load the model in 4-bit precision
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=quant_config,  # 4-bit Quantization config
            torch_dtype=torch.bfloat16,        # Mixed precision (optional, use bfloat16 for efficiency)
            device_map="auto",                 # Automatically map to available GPUs
        )

        # Load the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        get_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
        )

        response = get_pipeline(messages, max_length = 1000)
        text = response[0]['generated_text'][1]['content']
        print(f'text: {text}')
        content = json.loads(text)
        print(f'content: {content}')
        # input_data = text.split(f"{source_language}:")[1].split(f"{target_language}:")[0]
        # output_data = text.split(f"{target_language}:")[1]
        input_data, output_data = content[source_language], content[target_language]

        if task_string.startswith("speech"):
            input_data = await self.process(TranslationRequest(data = {
                "input" : input_data,
                "task_string": "text2speech",
                "source_language": source_language,
                "target_language": source_language
            }))

        if task_string.endswith("speech"):
            output_data = await self.process(TranslationRequest(data = {
                "input" : output_data,
                "task_string": "text2speech",
                "source_language": target_language,
                "target_language": target_language
            }), serialize = False)
        
        output = {"input": input_data[:100],"output": output_data[:100],"task_string": task_string,"source_language": source_language,"target_language": target_language}
        bt.logging.info(f'Generated Trnaslation Request: {output}')
        
        return {
                    "input": input_data,
                    "output": output_data,
                    "task_string": task_string,
                    "source_language": source_language,
                    "target_language": target_language
                }
    
    async def generate_query_openai(self, target_language, source_language, task_string, topic):
        url = os.getenv("INFERENCE_URL")
        token = os.getenv("INFERENCE_API_KEY")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        body = {
            "messages": [
                {
                    "role": "system",
                    "content": f"\
                    You are an expert story teller.\
                    You can write short stories that capture the imagination, \
                    end readers on an adventure and complete an alegorical thought all within 100 words. \
                    Please write a short story about {topic}. \
                    Keep the story short but be sure to use an alegory and complete the idea. \
                    Write story in two languages, those are {source_language} and {target_language}.\
                    Don't put any descriptions, just follow below format:\
                    {source_language}: \n {target_language}:"
                }
            ],
            "model": "gpt-4o"
        }
        response = requests.post(url, headers = headers, json = body, timeout=30)
        bt.logging.info(f"openairesponse:{response.json()}")

        text = response.json()["choices"][0]["message"]["content"]
        input_data = text.split(f"{source_language}:")[1].split(f"{target_language}:")[0]
        output_data = text.split(f"{target_language}:")[1]

        if task_string.startswith("speech"):
            input_data = await self.process(TranslationRequest(data = {
                "input" : input_data,
                "task_string": "text2speech",
                "source_language": source_language,
                "target_language": source_language
            }))

        if task_string.endswith("speech"):
            output_data = await self.process(TranslationRequest(data = {
                "input" : output_data,
                "task_string": "text2speech",
                "source_language": target_language,
                "target_language": target_language
            }), serialize = False)
        
        output = {"input": input_data[:100],"output": output_data[:100],"task_string": task_string,"source_language": source_language,"target_language": target_language}
        bt.logging.info(f'Generated Trnaslation Request: {output}')
        
        return {
                    "input": input_data,
                    "output": output_data,
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
