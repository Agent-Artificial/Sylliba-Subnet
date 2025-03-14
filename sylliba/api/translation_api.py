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
from sylliba.utils.config import check_config, add_args, config
from sylliba.protocol import TranslateRequest, HealthCheck
import wave

import random

from fastapi.middleware.cors import CORSMiddleware

from neurons.utils.serialization import audio_decode, audio_encode
from neurons.utils.audio_save_load import _wav_to_tensor, _tensor_to_wav, _save_raw_audio_file, _load_raw_audio_file
from neurons.validator import Validator
from sylliba.utils.uids import get_miner_uids
from sylliba.utils.config import add_validator_args

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
        add_validator_args(cls, parser)
        
    @classmethod
    def config(cls):
        return config(cls)

    subtensor: "bt.subtensor"
    wallet: "bt.wallet"
    metagraph: "bt.metagraph"
    

    def __init__(self, config = None):
        self.config = self.config()
        self.config.merge(copy.deepcopy(Validator.get_config()))
        
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
                file_path = _save_raw_audio_file(request.input)
                input, _, _, _ = await _wav_to_tensor(file_path)
                request.input = audio_encode(input)
            
            translation_request = TranslationRequest(data = {
                "input": request.input,
                "task_string": request.task_string,
                "source_language": request.source_language,
                "target_language": request.target_language
            })
            translation_synapse = TranslateRequest(translation_request = translation_request)
    
            miner_uids = get_miner_uids(self)
            miner_axons = [self.metagraph.axons[uid] for uid in miner_uids]
        
            bt.logging.info(f'Miner Axons are {miner_axons}')

            responses = await self.subnet_api(
                axons=miner_axons,
                synapse=translation_synapse,
                timeout=5
            )
            result = []
            for response in responses:
                if response.miner_response is not None:
                    if translation_request.data['task_string'].endswith('speech'):
                        miner_output_data = audio_decode(response.miner_response)
                        wav_file = _tensor_to_wav(miner_output_data)
                        if isinstance(wav_file, io.BytesIO):
                            miner_output_data = wav_file.getvalue()
                        elif isinstance(wav_file, str):
                            miner_output_data = open(wav_file, 'rb').read()
                        miner_output_data = base64.b64encode(miner_output_data).decode("utf-8")
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
        uvicorn.run(self.app, host="0.0.0.0", port=self.config.api_port, loop="asyncio")
