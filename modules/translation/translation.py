import io
import scipy
import torch
import base64
import torchaudio
import asyncio
import wave
import numpy as np

from loguru import logger
from typing import Optional
from functools import lru_cache
from typing import Dict, Tuple, Union
from transformers import AutoProcessor, SeamlessM4Tv2Model
from pydub import AudioSegment

from .data_models import TARGET_LANGUAGES, TASK_STRINGS, TranslationRequest, TranslationConfig
import bittensor as bt
translation_config = TranslationConfig()

class Translation:
    def __init__(self):
        """
        Initializes a new instance of the Translation class.

        Args:
            translation_config (TranslationConfig): The configuration object for translation.

        Initializes the following instance variables:
            - translation_config (TranslationConfig): The configuration object for translation.
            - processor (AutoProcessor): The processor object for preprocessing input data.
            - model (SeamlessM4Tv2Model): The model object for translation.
            - device (torch.device): The device to run the model on (CUDA if available, otherwise CPU).
            - target_languages (Dict[str, str]): A dictionary mapping target languages to their codes.
            - task_strings (Dict[str, str]): A dictionary mapping task strings to their codes.
            - data_input (None): The input data for translation.
            - task_string (None): The task string for translation.
            - source_language (None): The source language for translation.
            - target_language (None): The target language for translation.
        """
        self.translation_config = translation_config
        self.processor = AutoProcessor.from_pretrained(translation_config.model_name_or_card)
        self.model = SeamlessM4Tv2Model.from_pretrained(translation_config.model_name_or_card)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.target_languages: Dict[str, str] = TARGET_LANGUAGES
        self.task_strings: Dict[str, str] = TASK_STRINGS
        self.data_input = None
        self.task_string = None
        self.source_language = None
        self.target_language = None

    @lru_cache(maxsize=128)
    def _get_language(self, language: str) -> str:
        """
        Function to retrieve the language from the target_languages dictionary.
        
        Parameters:
            self: The Translation object.
            language: A string representing the language to retrieve.
        
        Returns:
            A string representing the language from the target_languages dictionary.
        """
        try:
            return self.target_languages[language]
        except KeyError as e:
            logger.error(f"Invalid language: {language} {e}")
            raise ValueError(f"Invalid language: {language}") from e

    async def process(self, translation_request: TranslationRequest, serialize = True) -> Tuple[Union[str, None], Union[torch.Tensor, None]]:
        """
        A function that processes a TranslationRequest object to perform translation tasks. 
        Retrieves input data, task string, source and target languages, preprocesses the input data, 
        predicts the output based on the input and languages, and processes the final output. 
        Raises ValueErrors for invalid task strings and missing input data.

        Parameters:
            self: The Translation object.
            translation_request (TranslationRequest): The request object containing input data, task string, 
                source language, and target language.

        Returns:
            Tuple[Union[str, None], Union[torch.Tensor, None]]: 
                A tuple containing either a string or None, and either a torch.Tensor or None, 
                representing the processed output.
        """
        if "input" in translation_request.data:
            self.data_input = translation_request.data["input"]
            bt.logging.info(f"data_input:{self.data_input[:100]}")
        if "task_string" in translation_request.data:
            self.task_string = translation_request.data["task_string"]
            bt.logging.info(f"task_string:{self.task_string}")
        if "source_language" in translation_request.data:
            self.source_language = translation_request.data["source_language"].title()
            bt.logging.info(f"source_language:{self.source_language}")
        if "target_language" in translation_request.data:
            self.target_language = translation_request.data["target_language"].title()
            bt.logging.info(f"target_language:{self.target_language}")
        if not self.task_string:
            raise ValueError(f"Invalid task string: {translation_request.data}")

        if self.data_input is None:
            raise ValueError("No input provided")
        if self.task_string.startswith("speech"):
            bt.logging.info("startswith(speech)")
            try:
                self.data_input = self._preprocess(self.data_input)
            except Exception as e:
                logger.error(f"Error preprocessing input: {e}")
                raise ValueError(f"Error preprocessing input: {e}") from e
        
        output = None
        with torch.no_grad():
            output = self._predict(
                input=self.data_input,
                task_str=self.task_strings[self.task_string],
                src_lang=self.target_languages[self.source_language],
                tgt_lang=self.target_languages[self.target_language]
            )
        bt.logging.info(f"output before audio processing:{output[:100]}")
        
        if serialize is False:
            return output
        
        if self.task_string.endswith("speech"):
            bt.logging.info("endswith(speech)")
            output = self._process_audio_output(output)
        else:
            output = output.encode("utf-8")
        # bt.logging.info(f"output after audio processing:{output[:100]}")  
        generated_output = self._process_output(output)
        
        return generated_output
    
    def _preprocess(self, input_data):
        """
        Preprocesses the input data by writing it to a file and returning the file path.

        Args:
            input_data (str): The base64 encoded audio data to be preprocessed.

        Returns:
            str: The file path of the preprocessed audio file.

        Raises:
            None
        """
        
        file_name1 = "./modules/translation/in/first_test_audio.wav"
        file_name2 = "./modules/translation/in/audio_request.wav"
        data, sr = self.wav_to_tensor(file_name1)
        bt.logging.info(f'FIRST TEST AUDIO : {data}')
        self._tensor_to_wav(data, file_name2, sr)
                
        
        file_name = "./modules/translation/in/audio_request.wav"
        decoded_data = base64.b64decode(input_data)
        buffer = io.BytesIO(decoded_data)
        decoded_data = torch.load(buffer)
        bt.logging.info(f'DECODED INPUT DATA: {decoded_data}')
        # self._tensor_to_wav(decoded_data, file_name)
        return "./modules/translation/in/audio_request.wav"
    
    def _process_text_inputs(self, input_data: str, src_lang: str) -> Dict[str, torch.Tensor]:
        """
        Processes text inputs by utilizing the processor to convert input data into torch tensors.

        Parameters:
            self: The Translation object.
            input_data (str): The input text data to be processed.
            src_lang (str): The source language of the input text.

        Returns:
            Dict[str, torch.Tensor]: A dictionary containing torch tensors as values for different keys.
        """
        return self.processor(text=input_data, src_lang=src_lang, return_tensors="pt")

    def _process_audio_input(self, input_data: str, src_lang: str) -> Dict[str, torch.Tensor]:
        """
        Processes the audio input data and returns a dictionary of tensors.

        Args:
            input_data (str): The path to the audio file.
            src_lang (str): The source language of the audio.

        Returns:
            Dict[str, torch.Tensor]: A dictionary containing the processed tensors.
        """
        waveform, sample_rate = torchaudio.load(input_data)
        if sample_rate != 16000:
            waveform = torchaudio.functional.resample(waveform, sample_rate, 16000)
        return self.processor(audios=waveform.squeeze(), src_lang=src_lang, sampling_rate=16000, return_tensors="pt")

    def _generate_audio(self, input_data: Dict[str, torch.Tensor], tgt_lang: str) -> torch.Tensor:
        """
        Generate an audio tensor based on the input data and target language.

        Args:
            input_data (Dict[str, torch.Tensor]): A dictionary containing input data tensors.
            tgt_lang (str): The target language for the generated audio.

        Returns:
            torch.Tensor: The generated audio tensor.

        """
        input_data = {k: v.to(self.device) for k, v in input_data.items()}
        return self.model.generate(**input_data, tgt_lang=tgt_lang)[0]

    def _generate_text(self, input_data: Dict[str, torch.Tensor], tgt_lang: str) -> str:
        """
        Generates text based on the input data and target language.

        Args:
            input_data (Dict[str, torch.Tensor]): A dictionary containing input data tensors.
            tgt_lang (str): The target language for the generated text.

        Returns:
            str: The generated text.
        """
        input_data = {k: v.to(self.device) for k, v in input_data.items()}
        output_tokens = self.model.generate(**input_data, tgt_lang=tgt_lang, generate_speech=False)
        return self.processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

    def _predict(self, **kwargs) -> Tuple[Union[str, None], Union[torch.Tensor, None]]:
        """
        A function that processes input data for prediction. 
        Retrieves input data, task string, source and target languages, preprocesses the input data based on the task string, 
        generates output based on the input and languages, and returns the output. 
        Logs intermediate information for debugging. 
        Raises errors for processing and prediction failures.

        Args:
            **kwargs: A dictionary containing input data, task string, source language, and target language.

        Returns:
            Tuple[Union[str, None], Union[torch.Tensor, None]]: 
                A tuple containing either a string or None, and either a torch.Tensor or None, 
                representing the predicted output.
        """
        try:
            input_data = kwargs['input']
            task_str = kwargs['task_str']
            src_lang = kwargs['src_lang']
            tgt_lang = kwargs['tgt_lang']
            
            if task_str.startswith('s2'):
                input_data = self._process_audio_input(input_data, src_lang)
            else:
                input_data = self._process_text_inputs(input_data, src_lang)
                
            logger.debug(str(input_data)[:30])
            logger.debug(type(input_data))
            logger.debug(kwargs)
            output = None
            try:
                if self.task_string.endswith("speech"):
                    output = self._generate_audio(input_data, tgt_lang)
                else:
                    output = self._generate_text(input_data, tgt_lang)
            except AttributeError as e:
                logger.error(f"Error processing translation: {e}")
                raise ValueError(f"Error processing translation: {e}") from e
            logger.debug(output)
            logger.debug(type(output))
            return output
        
        except Exception as e:
            logger.error(f"Error processing translation: {e}")
            raise
        
    def _process_audio_output(self, output: torch.Tensor) -> torch.Tensor:
        """
        Process the audio output tensor and return it as a bytes object.

        Args:
            output (torch.Tensor): The audio output tensor to be processed.

        Returns:
            torch.Tensor: The processed audio output as a bytes object.

        Raises:
            ValueError: If there is an error processing the audio output.
        """
        try:
            self._tensor_to_wav(output, './modules/translation/out/audio_generated.wav')
            buffer = io.BytesIO()
            torch.save(output, buffer)
        except Exception as e:
            logger.error(f"Error processing audio output: {e}")
            raise ValueError(f"Error processing audio output: {e}") from e
        return buffer.getvalue()
    
    def wav_to_tensor(self, file_path: str):
        """
        Reads a WAV file and converts it into a PyTorch tensor.

        Args:
        file_path (str): The path to the input wav file.

        Returns:
        torch.Tensor: A tensor containing the audio data.
        int: The sample rate of the audio.
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
    
    def _tensor_to_wav(self, tensor: torch.Tensor, file_path: str, sample_rate: int = 16000):
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

        # Open a wav file in write mode
        with wave.open(file_path, 'wb') as wav_file:
            n_channels = 1  # Mono audio
            sampwidth = 2  # 2 bytes = 16-bit audio
            wav_file.setnchannels(n_channels)
            wav_file.setsampwidth(sampwidth)
            wav_file.setframerate(sample_rate)

            # Convert NumPy array to int16 and write to the wave file
            wav_file.writeframes(audio_data.tobytes())

        print(f"Audio saved as '{file_path}'")


    def _process_output(self, output: str) -> str:
        """
        Process the final output to encode it in base64 and decode it to utf-8.

        Args:
            output (str): The final output to be processed.

        Returns:
            str: The processed output after encoding and decoding.
        Raises:
            ValueError: If there is an error processing the final output.
        """
        try:
            output = base64.b64encode(output).decode("utf-8")
        except Exception as e:
            logger.error(f"Error processing final output: {e}")
            raise ValueError(f"Error processing final output: {e}") from e
        bt.logging.info(f"generateoutput : {output[:100]}")
        return output

    
def text2text(translation: Translation, miner_request: Optional[TranslationRequest] = None):
    """
    Generates a translation of the input text from English to French using the given Translation object.

    Args:
        translation (Translation): The Translation object used to generate the translation.
        miner_request (Optional[TranslationRequest], optional): The optional TranslationRequest object containing additional data for the translation. Defaults to None.

    Returns:
        str: The translated text from English to French.

    Example:
        >>> translation = Translation()
        >>> miner_request = TranslationRequest(data={"input": "Hello, my name is John Doe.", "task_string": "text2text", "source_language": "English", "target_language": "French"})
        >>> text2text(translation, miner_request)
        'Bonjour, je m'appelle John Doe.'
    """
    translation_request = miner_request or TranslationRequest(
        data={"input": "Hello, my name is John Doe.", "task_string": "text2text", "source_language": "English", "target_language": "French"}
    )
    return translation.process(translation_request)


def text2speech(translation: Translation, miner_request: Optional[TranslationRequest] = None):
    """
    Generates speech from text using the given Translation object.

    Args:
        translation (Translation): The Translation object used to generate the speech.
        miner_request (Optional[TranslationRequest], optional): The optional TranslationRequest object containing additional data for the speech generation. Defaults to None.

    Returns:
        Union[str, None]: The generated speech as a string, or None if an error occurred.
    """
    translation_request = miner_request or TranslationRequest(
        data={"input": "Hello, my name is John Doe.", "task_string": "text2speech", "source_language": "English", "target_language": "French"}
    )
    return translation.process(translation_request)


def speech2text(translation: Translation, miner_request: Optional[TranslationRequest] = None):
    """
    A function that converts speech input to text using a given Translation object.
    
    Args:
        translation (Translation): The Translation object used for the conversion.
        miner_request (Optional[TranslationRequest], optional): Additional data for the conversion. Defaults to None.
        
    Returns:
        The processed text output.
    """
    translation_request = miner_request or TranslationRequest(
        data={"input": "./modules/translation/in/audio_request.wav", "task_string": "speech2text", "source_language": "English", "target_language": "French"}
    )
    return translation.process(translation_request)


def speech2speech(translation: Translation, miner_request: Optional[TranslationRequest] = None):
    """
    Converts speech input to speech output using a given Translation object.
    
    Args:
        translation (Translation): The Translation object used for the conversion.
        miner_request (Optional[TranslationRequest], optional): Additional data for the conversion. Defaults to None.
        
    Returns:
        The processed speech output.
    """
    translation_request = miner_request or TranslationRequest(
        data={"input": "./modules/translation/in/audio_request.wav", "task_string": "speech2speech", "source_language": "English", "target_language": "French"}
    )
    return translation.process(translation_request)


async def process(translation_request: TranslationRequest):
    translation = Translation()
    result = None
    try:
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(translation.process(translation_request=translation_request))
    except Exception:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        result = loop.run_until_complete(translation.process(translation_request=translation_request))
        new_loop.close()
    finally:
        return result  # type: ignore
    

if __name__ == "__main__":
    translation = Translation()
    result = speech2text(translation)
    print(f"speech2text: {result}")
    result = speech2speech(translation)
    print(f"speech2speech: {result}")
    result = text2text(translation)
    print(f"text2text: {result}")
    result = text2speech(translation)
    print(f"text2speech: {result}")
        
    