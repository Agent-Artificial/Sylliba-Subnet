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
from typing import List
import bittensor as bt
from sklearn.feature_extraction.text import CountVectorizer
from scipy.special import expit

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.translate.bleu_score import sentence_bleu
from difflib import SequenceMatcher
import numpy as np

def reward(miner_response: str, sample_output: str) -> float:
    bt.logging.info('-------------------------------- REWARD HERE ---------------------------------')
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
    bt.logging.info('------------------------------- REWARDS FINISEHD ------------------------------')
    
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
