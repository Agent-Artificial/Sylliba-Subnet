import os
import asyncio
import bittensor as bt
from typing import List, Dict, Tuple, Union, Any, Optional
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import StreamingResponse
import uvicorn
from sylliba.utils.misc import ttl_metagraph
from pydantic import BaseModel
from modules.translation.data_models import TranslationRequest
import base64
import io
import torch
import time
from sylliba.api.subnet_api import SubnetAPI
import copy
from neurons.config import validator_config
from sylliba.utils.config import check_config, add_args, config

import random

from fastapi.middleware.cors import CORSMiddleware

from neurons.utils.serialization import audio_decode, audio_encode
from neurons.utils.audio_save_load import _wav_to_tensor, _tensor_to_wav

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

        # Allow CORS for frontend
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Adjust this to your frontend's domain if needed, like ['http://localhost:3000']
            allow_credentials=True,
            allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
            allow_headers=["*"],  # Allow all headers
        )

        # Middleware to measure response time
        @self.app.middleware("http")
        async def add_response_time_header(request: Request, call_next):
            start_time = time.time()
            response = await call_next(request)
            duration = time.time() - start_time
            bt.logging.info(f'Response time; {duration}s')
            response.headers['X-Response-Time'] = f"{duration:.4f} seconds"
            return response

        @self.app.post("/api/translation")
        async def get_translation(request: TranslationInput):
            bt.logging.info('request received')
            if request.task_string.startswith('speech'):
                wav_data = audio_decode(request.input)
                input, sample_rate = await _wav_to_tensor(io.BytesIO(wav_data))
                request.input = audio_encode(input)
            
            translation_request = TranslationRequest(data = {
                "input": request.input,
                "task_string": request.task_string,
                "source_language": request.source_language,
                "target_language": request.target_language
            })
            
            axons = self.metagraph.axons
            responses = await self.subnet_api(
                axons=axons,
                translation_request=translation_request,
                timeout=30
            )
            result = []
            for response in responses:
                if response.miner_response is not None:
                    if translation_request.data['task_string'].endswith('speech'):
                        miner_output_data = audio_decode(response.miner_response)
                        wav_file = _tensor_to_wav(miner_output_data)
                        miner_output_data = audio_encode(wav_file)
                    else:
                        miner_output_data = response.miner_response
                    bt.logging.info(f'DECODED OUTPUT DATA: {miner_output_data}')
                    result.append(miner_output_data)
            if(len(result) == 0):
                return "No miner available!"
            return random.choice(result)
            
    
    def start(self):
        # Set the default event loop policy to avoid conflicts with uvloop
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
        # Start the Uvicorn server with your app
        uvicorn.run(self.app, host="0.0.0.0", port=self.config.api_port, loop="asyncio", workers=int(os.getenv('WORKER_COUNT', 1)))
