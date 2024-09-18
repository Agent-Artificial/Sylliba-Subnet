import base64
import io
import torch

def synapse_encode(data, content_type):
    if content_type == 'speech':
        buffer = io.BytesIO()
        torch.save(data, buffer)
        data = buffer.getvalue()
    else:
        data = data.encode('utf-8')
    output = base64.b64encode(data).decode("utf-8")
    return output

def synapse_decode(data, content_type):
    decoded_data = base64.b64decode(data)
    if content_type == 'speech':
        buffer = io.BytesIO(decoded_data)
        decoded_data = torch.load(buffer)
    return decoded_data

if __name__ == '__main__':
    text_data = 'Hello How are you doing today?'
    content_type = 'text'

    encoded_data = synapse_encode(text_data, content_type)
    print(encoded_data)

    decoded_data = synapse_decode(encoded_data, content_type)
    print(decoded_data)

    wave_data = torch.tensor([1, 2, 3, 4, 5])
    content_type = 'speech'

    encoded_data = synapse_encode(wave_data, content_type)
    print(encoded_data)

    decoded_data = synapse_decode(encoded_data, content_type)
    print(decoded_data)