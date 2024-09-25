from transformers import AutoProcessor, SeamlessM4Tv2Model, pipeline
import torch

from neurons.validator import MODELS
from neurons.utils.model_load import load_seamless
from modules.translation.data_models import TARGET_LANGUAGES

def process(messages, source_language):
    """
    Process messages for text-to-speech conversion.

    Args:
        messages (list): List of messages to process.
        source_language (str): The source language of the messages.

    Returns:
        Processed data for text-to-speech conversion.
    """
    # Model ID for Seamless M4T V2 Large
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    if 'seamless' not in MODELS:
        MODELS['seamless'] = load_seamless()
    model, processor = MODELS['seamless']

    src_lang = TARGET_LANGUAGES[source_language]

    input_data = processor(text=messages, src_lang=src_lang, return_tensors="pt")

    input_data = {k: v.to(device) for k, v in input_data.items()}
    return model.generate(**input_data, tgt_lang=src_lang)[0]

if __name__ == '__main__':
    text = """Sylliba is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate many languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.
As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.
Explore Sylliba and experience the future of translation here."""
    source_language = "English"
    output_data = process(text, source_language)
    print(f"output_data: {output_data[:100]}")
