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
import numpy as np
import torch
from typing import List
import bittensor as bt
from sklearn.feature_extraction.text import CountVectorizer
from scipy.special import expit

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.translate.bleu_score import sentence_bleu
from difflib import SequenceMatcher
import numpy as np

def reward_text(miner_response: str, input_string: str, module) -> float:
    prompt = """Evaluate the following translation:\n\n\
Original Text: {original}\n\
Translation: {translation}\n\n\
Rate the quality of this translation on a scale from 0 to 10, floating point is possible\
where 0 means it's very poor and 10 means it's flawless. Please provide only the number."""

    score = float(module.process(prompt.format(translation=miner_response, original=input_string)))
    
    return score

from scipy.spatial.distance import euclidean
import librosa
from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio(file_path):
    client = speech.SpeechClient()
    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)
    
    # Extract transcription from the response
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

def evaluate_audio_quality_from_tensor(audio_tensor, sample_rate = 16000):
    # Calculate loudness (RMS - Root Mean Square)
    rms = np.mean(librosa.feature.rms(y=audio_tensor))

    # Calculate signal-to-noise ratio (SNR)
    noise_threshold = np.percentile(np.abs(audio_tensor), 25)  # assuming low amplitudes represent noise
    signal_power = np.mean(audio_tensor**2)
    noise_power = np.mean((audio_tensor[audio_tensor < noise_threshold])**2)
    snr = 10 * np.log10(signal_power / noise_power) if noise_power > 0 else float('inf')

    # Return quality metrics
    return rms * 0.5 + snr * 0.5

def reward_speech(miner_audio: torch.Tensor, input_string: str, module) -> float:
    # Step 1: Transcribe the audio
    transcription = transcribe_audio(miner_audio)

    # Step 2: Evaluate the transcription
    transcription_evaluation = reward_text(transcription, input_string, module)
    print("Transcription Evaluation:", transcription_evaluation)
    
    # Step 3: Evaluate the audio quality
    audio_quality = evaluate_audio_quality_from_tensor(miner_audio)
    print("Audio Quality Evaluation:", audio_quality)
    
    return transcription_evaluation * 0.5 + audio_quality * 0.5




def get_rewards(
    query: int,
    responses: List[float],
) -> np.ndarray:
    """
    Returns an array of rewards for the given query and responses.

    Args:
    - query (int): The query sent to the miner.
    - responses (List[float]): A list of responses from the miner.

    Returns:
    - np.ndarray: An array of rewards for the given query and responses.
    """
    # Get all the reward results by iteratively calling your reward() function.
    
    return np.array(
        [reward(query, response) for response in responses]
    )
