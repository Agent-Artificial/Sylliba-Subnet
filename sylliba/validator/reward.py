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

def reward_text(miner_response: str, module) -> float:
    bt.logging.info('-------------------------------- REWARD_TEXT HERE ---------------------------------')
    bt.logging.info(f'miner_response : {miner_response}')
    bt.logging.info(f'sample_output : {sample_output}')
    # Compute cosine similarity using TF-IDF vectorization
    vectorizer = TfidfVectorizer().fit([miner_response, sample_output])
    vectors = vectorizer.transform([miner_response, sample_output])
    cosine_sim = cosine_similarity(vectors[0], vectors[1])[0][0]
    
    # Compute BLEU score for translation evaluation
    miner_response_tokens = miner_response.split()
    sample_output_tokens = sample_output.split()
    bleu_score = sentence_bleu([sample_output_tokens], miner_response_tokens)
    
    # Compute Levenshtein similarity (as a ratio of matched characters)
    lev_sim = SequenceMatcher(None, miner_response, sample_output).ratio()
    
    # Aggregate the scores (with customizable weights)
    aggregated_score = 0.5 * cosine_sim + 0.3 * bleu_score + 0.2 * lev_sim

    bt.logging.info(f'similarity score: {aggregated_score}')
    bt.logging.info('------------------------------- REWARD_TEXT FINISEHD ------------------------------')
    
    return aggregated_score

from scipy.spatial.distance import euclidean
import librosa

def extract_mfcc_from_array(audio_data: np.ndarray, sample_rate: int, n_mfcc: int = 13) -> np.ndarray:
    """
    Extract MFCC features from audio data represented as a NumPy array.
    
    :param audio_data: Tensor or NumPy array of audio waveform data
    :param sample_rate: Sample rate of the audio data
    :param n_mfcc: Number of MFCC features to extract
    :return: MFCC features as a NumPy array
    """
    try:
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=n_mfcc)
        return np.mean(mfccs.T, axis=0)  # Take the mean of the MFCC features
    except Exception as e:
        bt.logging.error(f"Error extracting MFCCs from audio data: {e}")
        return None

def reward_speech(miner_audio: torch.Tensor, sample_audio: torch.Tensor) -> float:
    bt.logging.info('-------------------------------- REWARD_SPEECH HERE ---------------------------------')
    bt.logging.info(f'type of miner_audio : {type(miner_audio)}')
    bt.logging.info(f'type of sample_audio : {type(sample_audio)}')
    
    # Extract MFCC features from the audio tensors
    miner_audio = np.array(miner_audio.cpu())
    sample_audio = np.array(sample_audio.cpu())

    miner_mfcc = extract_mfcc_from_array(miner_audio, 16000).flatten()
    sample_mfcc = extract_mfcc_from_array(sample_audio, 16000).flatten()
    
    if miner_mfcc is None or sample_mfcc is None:
        bt.logging.error("Failed to extract MFCCs from one or both audio inputs. Returning 0 similarity score.")
        return 0.0
    
    bt.logging.info(f'miner_mfcc shape: {miner_mfcc.shape}')
    bt.logging.info(f'sample_mfcc shape: {sample_mfcc.shape}')
    
    # Compute cosine similarity between the MFCC features
    cosine_sim = cosine_similarity([miner_mfcc], [sample_mfcc])[0][0]
    
    # Compute Euclidean distance (or use another distance metric if needed)
    euclidean_dist = euclidean(miner_mfcc, sample_mfcc)
    
    # Aggregate the scores (with customizable weights)
    aggregated_score = 0.7 * cosine_sim + 0.3 * (1 / (1 + euclidean_dist))  # inverse to make it similarity
    
    bt.logging.info(f'similarity score: {aggregated_score}')
    bt.logging.info('------------------------------- REWARD_SPEECH FINISHED ------------------------------')
    
    return aggregated_score



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
