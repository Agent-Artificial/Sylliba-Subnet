from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import torch
import json

def process(messages):
    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,           # This flag is now part of BitsAndBytesConfig
        bnb_4bit_use_double_quant=True,  # Optional, for double quantization
        bnb_4bit_quant_type="nf4",   # Choose between 'fp4' or 'nf4' (Non-negative quantization)
    )

    # Load the model in 4-bit precision
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=quant_config,  # 4-bit Quantization config
        torch_dtype=torch.bfloat16,        # Mixed precision (optional, use bfloat16 for efficiency)
    ).to(device)

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    get_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    response = get_pipeline(messages, max_length = 1000)
    text = response[0]['generated_text'][-1]['content']
    return text

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