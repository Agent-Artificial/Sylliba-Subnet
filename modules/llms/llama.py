from llama_cpp import Llama
from neurons.validator import MODELS
from typing import List, Dict, Any
import torch
from neurons.utils.model_load import load_llama

def process(messages: List[Dict[str, Any]], device = torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """
    Process a list of messages.

    Args:
        messages (list): A list of message objects to process.

    Returns:
        The processed result.
    """
    if 'llama' not in MODELS:
        MODELS['llama'] = load_llama(device)
    model, tokenizer = MODELS['llama']
    
    input_data = '\n'.join([entry['content'] for entry in messages])
    inputs = tokenizer(input_data, return_tensors = "pt").to("cuda")

    outputs = model.generate(**inputs, max_new_tokens = 1000, use_cache = True)
    new_tokens = outputs[:, inputs['input_ids'].shape[-1]:]
    result = tokenizer.batch_decode(new_tokens, skip_special_tokens=True)

    return result[0]

if __name__ == '__main__':
    text = """Sylliba is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate many languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.
As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.
Explore Sylliba and experience the future of translation here."""
    source_language = "English"
    target_language = "French"

    topic = "Last day on Earth"

    messages = [
        {
            "role": "system",
            "content": f"""
            You are an expert story teller.
            You can write short stories that capture the imagination, 
            end readers on an adventure and complete an alegorical thought all within 100~200 words. 
            Please write a short story about {topic} in {source_language}. 
            Keep the story short but be sure to use an alegory and complete the idea.
            """
        }
    ]
    output_data = process(messages)
    print(f"output_data: {output_data}")