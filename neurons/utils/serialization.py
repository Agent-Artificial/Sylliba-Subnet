import base64
import io
import torch

def audio_encode(data):
    """
    Encode audio data.

    Args:
        data: The audio data to encode.

    Returns:
        The encoded audio data.
    """
    buffer = io.BytesIO()
    torch.save(data, buffer)
    data = buffer.getvalue()
    return base64.b64encode(data).decode("utf-8")

def audio_decode(data):
    """
    Decode audio data.

    Args:
        data: The audio data to be decoded.

    Returns:
        The decoded audio data.
    """
    decoded_data = base64.b64decode(data)
    buffer = io.BytesIO(decoded_data)
    decoded_data = torch.load(buffer)
    return decoded_data

if __name__ == '__main__':
    wave_data = torch.tensor([1, 2, 3, 4, 5])
    content_type = 'speech'

    encoded_data = audio_encode(wave_data)
    print(encoded_data)

    decoded_data = audio_encode(encoded_data)
    print(decoded_data)