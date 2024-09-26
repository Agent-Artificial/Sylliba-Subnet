from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import json

from neurons.validator import MODELS
from neurons.utils.model_load import load_flan_t5_large

def process(messages):
    """
    Process a list of messages.

    Args:
        messages (list): A list of message objects to process.

    Returns:
        The processed result.
    """
    # Load the model
    if 'flan_t5_large' not in MODELS:
        MODELS['flan_t5_large'] = load_flan_t5_large()
    model, tokenizer = MODELS['flan_t5_large']

    input_text = '\n'.join([message['content'] for message in messages])
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids, max_length=1000)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)  # The output translation


if __name__ == '__main__':
    text = """Sylliba is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate many languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.
As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.
Explore Sylliba and experience the future of translation here."""
    
    source_language = "English"
    target_language = "English"
    topic = 'Last day on earth'

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
