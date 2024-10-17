import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

from neurons.enums.models import MODELS
from neurons.utils.model_load import load_wav2vec

# Function to transcribe audio from a torch.Tensor
def process(audio_tensor, sampling_rate=16000, device = torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    # load model
    if 'wav2vec' not in MODELS:
        MODELS['wav2vec'] = load_wav2vec(device)
    model, tokenizer = MODELS['wav2vec']

    # Ensure the tensor is 1D
    if audio_tensor.ndim > 1:
        audio_tensor = audio_tensor.squeeze()

    # Resample if necessary
    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
        audio_tensor = resampler(audio_tensor)

    # Tokenize the audio
    inputs = tokenizer(audio_tensor.cpu().numpy(), return_tensors="pt", padding="longest").to(device)

    # Perform inference
    with torch.no_grad():
        logits = model(inputs.input_values).logits

    # Get predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decode to text
    transcription = tokenizer.batch_decode(predicted_ids)

    return transcription[0]
