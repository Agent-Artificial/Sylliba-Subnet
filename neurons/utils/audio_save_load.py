import numpy as np
import torch
import wave
from fastapi import File
from typing import Union
import io
import base64

async def _wav_to_tensor(file: Union[str, File]) -> torch.Tensor:
    """
    Reads a WAV file and converts it into a PyTorch tensor.

    Args:
    file_path (str): The path to the input wav file.

    Returns:
    torch.Tensor: A tensor containing the audio data.
    int: The sample rate of the audio.
    """
    frames, sample_rate, num_channels, sampwidth = _load_raw_audio_file(file)
    # Convert byte data to numpy array
    if sampwidth == 2:
        # 16-bit audio
        audio_data = np.frombuffer(frames, dtype=np.int16).astype(np.float32)
        audio_data /= 2**15  # Normalize to [-1, 1] for 16-bit audio
    elif sampwidth == 4:
        # 32-bit audio
        audio_data = np.frombuffer(frames, dtype=np.int32).astype(np.float32)
        audio_data /= 2**31  # Normalize to [-1, 1] for 32-bit audio
    else:
        raise ValueError(f"Unsupported sample width: {sampwidth}")

    # If stereo, reshape the array to have the correct number of channels
    if num_channels > 1:
        audio_data = np.reshape(audio_data, (-1, num_channels))
        # Average the channels if you want to convert it to mono
        audio_data = np.mean(audio_data, axis=1)

    # Convert the numpy array to a PyTorch tensor
    audio_tensor = torch.tensor(audio_data, dtype=torch.float32)

    return audio_tensor, sample_rate

def _tensor_to_wav(tensor: torch.Tensor, file_path: str = None, sample_rate: int = 16000):
    """
    Converts a PyTorch tensor to a WAV file.

    Args:
    tensor (torch.Tensor): The input tensor representing audio waveform.
    file_path (str): The output path for the wav file.
    sample_rate (int): The sample rate of the audio (default is 16000).
    """
    # Ensure the tensor is on the CPU and converted to NumPy
    audio_data = tensor.cpu().numpy()

    # Convert to int16 for 16-bit audio, scale to the correct range
    audio_data = np.clip(audio_data * 2**15, -2**15, 2**15 - 1).astype(np.int16)
    
    return _save_raw_audio_file(audio_data, file_path, sample_rate)

def _load_raw_audio_file(file_path: str):
    """
    Loads a raw audio file from disk.

    Args:
        file_path (str): The path to the audio file.
    """
    # Open the wav file
    with wave.open(file_path, 'rb') as wav_file:
        # Extract audio parameters
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        num_channels = wav_file.getnchannels()
        sampwidth = wav_file.getsampwidth()

        # Read all audio frames
        frames = wav_file.readframes(num_frames)
    
    return frames, sample_rate, num_channels, sampwidth

def _save_raw_audio_file(audio_data, file_path: str = None, sample_rate: int = 16000):
    """
    Saves a raw audio file to disk.

    Args:
    file (Union[str, File]): The input audio file.
    file_path (str): The path to save the audio file.
    """

    # Open a wav file in write mode
    if file_path is None:
        file_path = io.BytesIO()

    with wave.open(file_path, 'wb') as wav_file:
        n_channels = 1  # Mono audio
        sampwidth = 2  # 2 bytes = 16-bit audio
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(sample_rate)

        # Convert NumPy array to int16 and write to the wave file
        if(isinstance(audio_data, np.ndarray)):
            audio_data = audio_data.tobytes()
        elif(isinstance(audio_data, str)):
            audio_data = base64.b64decode(audio_data)
        wav_file.writeframes(audio_data)

    if file_path:
        print(f"Audio saved as '{file_path}'")
    return file_path