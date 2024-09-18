from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import torch
import json

def process(messages, source_language, target_language):
    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    
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
        device_map="auto",                 # Automatically map to available GPUs
    )

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    get_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    response = get_pipeline(messages, max_length = 1000)
    text = response[0]['generated_text'][1]['content']
    print(f'text: {text}')
    content = json.loads(text)
    print(f'content: {content}')
    # input_data = text.split(f"{source_language}:")[1].split(f"{target_language}:")[0]
    # output_data = text.split(f"{target_language}:")[1]
    input_data, output_data = content[source_language], content[target_language]