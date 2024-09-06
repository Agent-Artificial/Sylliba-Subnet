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
from pydantic import BaseModel

import base64


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
    input: str
    task_string: str
    source_language: str
    target_language: str
        
    
class TranslateRequest(bt.Synapse):
    """
    Base class for Synapse communication object for translating text.

    Attributes:
        validator_request: Optional[MinerRequest]. accepts a dictionary with the values:
            - input: str - the text to be translated
            - task_string: Enum[TASK_STRING] - the task to be performed
            - source_language: Enum[TARGET_LANGUAGE] - the source language of the text
            - target_language: Enum[TARGET_LANGUAGE] - the target language of the text
        miner_response: Optional[Response] = None - normal response object of the miners
    """
    # Required request input, filled by sending dendrite caller.
    validator_request: Optional[Union[Dict[str, Any], ValidatorRequest]] = None

    # Optional request output, filled by receiving axon.
    miner_response: Optional[Any] = None

    def deserialize(self, value) -> str:
        """
        Deserializes the given string from a base64 encoded string.
        
        Returns:
         - str: unencoded string
        """
        return base64.b64decode(value)
    
    def serilize(self, value) -> str:
        """
        Serializes the given string into a base64 encoded string.
        
        Returns:
         - str: encoded string
        """
        return base64.b64encode(value)
    
        
