from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline, T5Tokenizer, T5ForConditionalGeneration, AutoProcessor, SeamlessM4Tv2Model
from unsloth import FastLanguageModel
import torch

def load_flan_t5_large(device = torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    model_id = "google/flan-t5-large"  # Using Flan-T5 model for Seq2Seq tasks
    model = T5ForConditionalGeneration.from_pretrained(model_id).to(device)
    tokenizer = T5Tokenizer.from_pretrained(model_id)

    print('flan_t5_model loaded successfully')

    return model, tokenizer

def load_meta_llama(device = torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,           # This flag is now part of BitsAndBytesConfig
        bnb_4bit_use_double_quant=True,  # Optional, for double quantization
        bnb_4bit_quant_type="nf4",   # Choose between 'fp4' or 'nf4' (Non-negative quantization)
    )

    if not hasattr(AutoModelForCausalLM, 'cached_model'):
        AutoModelForCausalLM.cached_model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=quant_config,  # 4-bit Quantization config
            torch_dtype=torch.bfloat16,        # Mixed precision (optional, use bfloat16 for efficiency)
        ).to(device)
    model = AutoModelForCausalLM.cached_model
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    print('llama loaded successfully')

    return model, tokenizer

def load_seamless(device = torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    model_id = "facebook/seamless-M4T-V2-large"

    processor = AutoProcessor.from_pretrained(model_id)
    model = SeamlessM4Tv2Model.from_pretrained(model_id).to(device)

    return model, processor

def load_llama(device = torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    max_seq_length = 2048 # Choose any! We auto support RoPE Scaling internally!
    dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
    load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "unsloth/llama-3-8b-Instruct-bnb-4bit", # Choose ANY! eg teknium/OpenHermes-2.5-Mistral-7B
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )
    FastLanguageModel.for_inference(model) 

    return model, tokenizer