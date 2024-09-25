from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import torch
from typing import List, Dict, Any

from neurons.validator import MODELS
from neurons.utils.model_load import load_llama

def process(messages: List[Dict[str, Any]]):
    """
    Process a list of messages.

    Args:
        messages (list): A list of message objects to process.

    Returns:
        The processed result.
    """
    if 'llama' not in MODELS:
        MODELS['llama'] = load_llama()
    model, tokenizer = MODELS['llama']

    get_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    response = get_pipeline(messages, max_length = 1000)
    return response[0]['generated_text'][-1]['content']

if __name__ == '__main__':
    text = """Sylliba is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate many languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.
As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.
Explore Sylliba and experience the future of translation here."""
    source_language = "English"
    target_language = "French"

    messages = [
        {
            "role": "system",
            "content": f"""
            Provided text is written in {source_language}.
            Please translate into {target_language}
            Don't put any tags, description or decorators.
            Write only translated text in raw text format.
            """
        }, 
        {
            "role": "user",
            "content": text
        }
    ]
    output_data = process(messages)
    print(f"output_data: {output_data}")