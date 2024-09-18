from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch
import json

def process(messages, source_language, target_language):
    # Model ID for Seamless M4T V2 Large
    model_id = "facebook/seamlessM4T-large"

    # Load the model for Seq2Seq (since this is for translation/multilingual tasks)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,  # Use float16 for mixed precision efficiency
        device_map="auto",          # Automatically map to available GPUs
    )

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    # Create a pipeline for translation
    translation_pipeline = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        src_lang=source_language,
        tgt_lang=target_language,
    )

    # Generate translations
    response = translation_pipeline(messages, max_length=1000)
    text = response[0]['translation_text']

    print(f'text: {text}')
    
    # Since Seamless translation is focused on multilingual, let's assume input/output as a simple JSON.
    content = json.dumps({source_language: messages, target_language: text})
    print(f'content: {content}')

    # Extracting input_data and output_data
    input_data, output_data = json.loads(content)[source_language], json.loads(content)[target_language]

    return input_data, output_data

if __name__ == 'main':
    messages = """Sylliba is a revolutionary translation module designed to bridge the gap in communication across diverse languages. With the capability to translate many languages, Sylliba supports both audio and text for inputs and outputs, making it a versatile tool for global interactions.
As our first step into the Bittensor ecosystem, Sylliba connects to the network we are building, providing AI tooling and linking various blockchain networks together. Our mission is to create a seamless and intuitive translation experience that leverages advanced AI to foster better understanding and collaboration across different languages and cultures.
Explore Sylliba and experience the future of translation here"""
    source_language = "English"
    target_language = "French"
    input_data, output_data = process(messages, source_language, target_language)
    print(f"input_data: {input_data}")
    print(f"output_data: {output_data}")
