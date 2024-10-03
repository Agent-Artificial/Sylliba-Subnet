# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from typing import Optional, Any, Dict, Union
import bittensor as bt
from pydantic import BaseModel, Field, field_validator, ConfigDict
from modules.translation.data_models import TranslationRequest
import json


# TODO(developer): Rewrite with your protocol definition.

# This is the protocol for the dummy miner and validator.
# It is a simple request-response protocol where the validator sends a request
# to the miner, and the miner responds with a dummy response.

# ---- miner ----
# Example usage:
#   def dummy( synapse: Dummy ) -> Dummy:
#       synapse.dummy_output = synapse.dummy_input + 1
#       return synapse
#   axon = bt.axon().attach( dummy ).serve(netuid=...).start()

# ---- validator ---
# Example usage:
#   dendrite = bt.dendrite()
#   dummy_output = dendrite.query( Dummy( dummy_input = 1 ) )
#   assert dummy_output == 2


class ValidatorRequest(BaseModel):
    """
    Represents a request from a validator to a miner.

    Attributes:
        input (str): The input text to be translated.
        task_string (str): A description of the translation task.
        source_language (str): The language of the input text.
        target_language (str): The desired language for the translation.
    """
    input: str
    task_string: str
    source_language: str
    target_language: str
        
class HealthCheck(bt.Synapse):
    """
    Represents a health check request/response.

    Attributes:
        response (bool): Indicates whether the health check was successful.
    """
    response: bool = False

class TranslateRequest(bt.Synapse):
    """
    Represents a translation request in the Sylliba network.

    This class encapsulates both the request and response for a translation task,
    as well as metadata about the network communication.

    Attributes:
        translation_request (Optional[Union[Dict[str, Any], TranslationRequest]]): The translation request details.
        miner_response (Optional[Any]): The response from the miner.
        axon_ip (Optional[str]): IP address of the axon.
        axon_port (Optional[str]): Port of the axon.
        axon_hotkey (Optional[str]): Hotkey of the axon.
        dendrite_ip (Optional[str]): IP address of the dendrite.
        dendrite_version (Optional[str]): Version of the dendrite.
        dendrite_nonce (Optional[str]): Nonce used by the dendrite.
        dendrite_uuid (Optional[str]): UUID of the dendrite.
        dendrite_hotkey (Optional[str]): Hotkey of the dendrite.
        dendrite_signature (Optional[str]): Signature from the dendrite.
        computed_body_hash (Optional[str]): Computed hash of the request body.
    """
    translation_request: Optional[Union[Dict[str, Any], TranslationRequest]] = Field(default_factory=dict)
    miner_response: Optional[Any] = Field(default=None)
    
    # Add fields for the headers we're receiving
    axon_ip: Optional[str] = Field(default=None)
    axon_port: Optional[str] = Field(default=None)
    axon_hotkey: Optional[str] = Field(default=None)
    dendrite_ip: Optional[str] = Field(default=None)
    dendrite_version: Optional[str] = Field(default=None)
    dendrite_nonce: Optional[str] = Field(default=None)
    dendrite_uuid: Optional[str] = Field(default=None)
    dendrite_hotkey: Optional[str] = Field(default=None)
    dendrite_signature: Optional[str] = Field(default=None)
    computed_body_hash: Optional[str] = Field(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_validator("*")
    def convert_string_to_int(cls, v):
        """
        Converts string values to integers if possible.

        Args:
            v: The value to be converted.

        Returns:
            int or original value: Converted integer if possible, otherwise the original value.
        """
        if isinstance(v, str) and v.isdigit():
            return int(v)
        return v

    @field_validator("*")
    def convert_string_to_int(cls, v):
        """
        Converts string values to integers if possible.

        Args:
            v: The value to be converted.

        Returns:
            int or original value: Converted integer if possible, otherwise the original value.
        """
        if isinstance(v, str) and v.isdigit():
            return int(v)
        return v

    def __init__(self, **data):
        """
        Initializes the TranslateRequest with the given data.

        Args:
            **data: Keyword arguments to initialize the object's attributes.
        """
        super().__init__()
        for key, value in data.items():
            setattr(self, key, value)

    @classmethod
    def from_headers(cls, headers: Dict[str, str]):
        """
        Creates a TranslateRequest instance from HTTP headers.

        Args:
            headers (Dict[str, str]): HTTP headers containing request metadata.

        Returns:
            TranslateRequest: An instance initialized with data from the headers.
        """
        return cls(
            axon_ip=headers.get('bt_header_axon_ip'),
            axon_port=headers.get('bt_header_axon_port'),
            axon_hotkey=headers.get('bt_header_axon_hotkey'),
            dendrite_ip=headers.get('bt_header_dendrite_ip'),
            dendrite_version=headers.get('bt_header_dendrite_version'),
            dendrite_nonce=headers.get('bt_header_dendrite_nonce'),
            dendrite_uuid=headers.get('bt_header_dendrite_uuid'),
            dendrite_hotkey=headers.get('bt_header_dendrite_hotkey'),
            dendrite_signature=headers.get('bt_header_dendrite_signature'),
        )


    def __setattr__(self, name, value):
        """
        Custom attribute setter to handle 'response' and 'request' attributes.

        Args:
            name (str): Name of the attribute to set.
            value: Value to set for the attribute.
        """
        if name == 'response':
            self._response = value
            self.miner_response = value
        elif name == 'request':
            self._request = value
            self.translation_request = value
        else:
            super().__setattr__(name, value)

    @property
    def response(self):
        """
        Gets the response value.

        Returns:
            Any: The miner's response or the internal _response value.
        """
        return self._response or self.miner_response

    @property
    def request(self):
        """
        Gets the request object.

        Returns:
            Any: The translation request object.
        """
        return self._request or self.translation_request

    @staticmethod
    def deserialize(serialized_str: str) -> 'TranslateRequest':
        """
        Deserializes a JSON string into a TranslateRequest object.

        Args:
            serialized_str (str): JSON-encoded string representation of a TranslateRequest.

        Returns:
            TranslateRequest: Deserialized TranslateRequest object.
        """
        request_dict = json.loads(serialized_str)
        
        # Create a new TranslateRequest instance and populate its attributes
        obj = TranslateRequest()
        if request_dict['translation_request']:
            obj.translation_request = TranslationRequest.from_dict(request_dict['translation_request'])
        obj.miner_response = request_dict['miner_response']
        
        return obj
    
    def serilize(self) -> str:
        """
        Serializes the given string into a base64 encoded string.
        
        Returns:
         - str: encoded string
        """
        request_dict = {
            'translation_request': self.translation_request.to_dict() if self.translation_request else None,
            'miner_response': self.miner_response
        }
        return json.dumps(request_dict)
