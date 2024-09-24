import os
import asyncio
import bittensor as bt
from typing import List, Dict, Tuple, Union, Any, Optional
from fastapi import FastAPI
import uvicorn
from sylliba.utils.misc import ttl_metagraph
from pydantic import BaseModel
from modules.translation.data_models import TranslationRequest
import base64
import io
import torch
from sylliba.api.subnet_api import SubnetAPI
import copy
from neurons.config import validator_config
from sylliba.utils.config import check_config, add_args, config

import random

from neurons.utils.serialization import audio_decode

class TranslationInput(BaseModel):
    input: str
    task_string: str
    source_language: str
    target_language: str


class APIServer:

    @classmethod
    def check_config(cls, config: "bt.Config"):
        check_config(cls, config)

    @classmethod
    def add_args(cls, parser):
        add_args(cls, parser)
        
    @classmethod
    def config(cls):
        return config(cls)

    subtensor: "bt.subtensor"
    wallet: "bt.wallet"
    metagraph: "bt.metagraph"
    

    def __init__(self, config = None):
        self.config = self.config()
        self.config.merge(validator_config())
        
        self.wallet = bt.wallet(config=self.config)
        self.subtensor = bt.subtensor(config=self.config)
        self.metagraph = self.subtensor.metagraph(self.config.netuid)
        
        self.app = FastAPI(title="subnet-api")
        self.subnet_api = SubnetAPI(wallet=self.wallet)


        @self.app.post("/api/translation/")
        async def get_translation(translationInput: TranslationInput):
            
            translation_request = TranslationRequest(data = {
                "input": translationInput.input,
                "task_string": translationInput.task_string,
                "source_language": translationInput.source_language,
                "target_language": translationInput.target_language
            })
            
            axons = self.metagraph.axons
            responses = await self.subnet_api(
                axons=axons,
                translation_request=translation_request,
                timeout=300
            )
            result = []
            for response in responses:
                if response.miner_response is not None:
                    if translation_request.data['task_string'].endswith('speech'):
                        miner_output_data = audio_decode(response.miner_response)
                    else:
                        miner_output_data = response.miner_response
                    bt.logging.info(f'DECODED OUTPUT DATA: {miner_output_data}')
                    result.append(response.miner_response)
            if(len(result) == 0):
                return "No miner available!"
            return random.choice(result)
            
    
    def start(self):
        # Set the default event loop policy to avoid conflicts with uvloop
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
        # Start the Uvicorn server with your app
        uvicorn.run(self.app, host="0.0.0.0", port=self.config.api_port, loop="asyncio", workers=int(os.getenv('WORKER_COUNT', 1)))
