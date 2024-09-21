from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import json

def process(messages):
    """
    Process a list of messages.

    Args:
        messages (list): A list of message objects to process.

    Returns:
        The processed result.
    """
    model_id = "google/flan-t5-large"  # Using Flan-T5 model for Seq2Seq tasks
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the model
    model = T5ForConditionalGeneration.from_pretrained(model_id).to(device)

    # Load the tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_id)

    input_text = '\n'.join([message['content'] for message in messages])
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids, max_length=1000)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)  # The output translation


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
            Please translate into {target_language}.
            Don't put any tags, description, or decorators.
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
