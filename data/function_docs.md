# Python Functions Documentation

## **`__getattr__`**

**Parameters:**
- `self`
- `name`

**Returns:** `None specified`

---

## **`turn_console_off`**

**Parameters:**
None

**Returns:** `None specified`

---

## **`turn_console_on`**

**Parameters:**
None

**Returns:** `None specified`

---

## **`trace`**

**Docstring:**
```
Wraps trace message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`debug`**

**Docstring:**
```
Wraps debug message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`from_scale_encoding`**

**Docstring:**
```
Decodes input_ data from SCALE encoding based on the specified type name and modifiers.

Args:
    input_ (Union[List[int], bytes, ScaleBytes]): The input_ data to decode.
    type_name (ChainDataType): The type of data being decoded.
    is_vec (bool, optional): Whether the data is a vector of the specified type. Default is ``False``.
    is_option (bool, optional): Whether the data is an optional value of the specified type. Default is ``False``.

Returns:
    Optional[Dict]: The decoded data as a dictionary, or ``None`` if the decoding fails.
```

**Parameters:**
- `input_`: `Union[List[int], bytes, ScaleBytes]`
- `type_name`: `ChainDataType`
- `is_vec`: `bool`
- `is_option`: `bool`

**Returns:** `Optional[Dict]`

---

## **`from_scale_encoding_using_type_string`**

**Parameters:**
- `input_`: `Union[List[int], bytes, ScaleBytes]`
- `type_string`: `str`

**Returns:** `Optional[Dict]`

---

## **`is_serving`**

**Docstring:**
```
True if the endpoint is serving.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`ip_str`**

**Docstring:**
```
Return the whole IP as string
```

**Parameters:**
- `self`

**Returns:** `str`

---

## **`__eq__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__str__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__repr__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`to_string`**

**Docstring:**
```
Provides a human-readable representation of the AxonInfo for this Axon.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`from_string`**

**Docstring:**
```
Creates an AxonInfo object from its string representation using JSON.

Args:
    json_string (str): The JSON string representation of the AxonInfo object.

Returns:
    AxonInfo: An instance of AxonInfo created from the JSON string. If decoding fails, returns a default AxonInfo object with default values.

Raises:
    json.JSONDecodeError: If there is an error in decoding the JSON string.
    TypeError: If there is a type error when creating the AxonInfo object.
    ValueError: If there is a value error when creating the AxonInfo object.
```

**Parameters:**
- `cls`
- `json_string`: `str`

**Returns:** `'AxonInfo'`

---

## **`from_neuron_info`**

**Docstring:**
```
Converts a dictionary to an AxonInfo object.

Args:
    neuron_info (dict): A dictionary containing the neuron information.

Returns:
    instance (AxonInfo): An instance of AxonInfo created from the dictionary.
```

**Parameters:**
- `cls`
- `neuron_info`: `dict`

**Returns:** `'AxonInfo'`

---

## **`to_parameter_dict`**

**Docstring:**
```
Returns a torch tensor or dict of the subnet IP info.
```

**Parameters:**
- `self`

**Returns:** `Union[dict[str, Union[str, int]], 'torch.nn.ParameterDict']`

---

## **`from_parameter_dict`**

**Parameters:**
- `cls`
- `parameter_dict`: `Union[dict[str, Any], 'torch.nn.ParameterDict']`

**Returns:** `'IPInfo'`

---

## **`fix_decoded_values`**

**Docstring:**
```
Fixes the decoded values.
```

**Parameters:**
- `cls`
- `decoded`: `Any`

**Returns:** `'ScheduledColdkeySwapInfo'`

---

## **`from_vec_u8`**

**Docstring:**
```
Returns a ScheduledColdkeySwapInfo object from a ``vec_u8``.
```

**Parameters:**
- `cls`
- `vec_u8`: `List[int]`

**Returns:** `Optional['ScheduledColdkeySwapInfo']`

---

## **`list_from_vec_u8`**

**Docstring:**
```
Returns a list of ScheduledColdkeySwapInfo objects from a ``vec_u8``.
```

**Parameters:**
- `cls`
- `vec_u8`: `List[int]`

**Returns:** `List['ScheduledColdkeySwapInfo']`

---

## **`get_null_neuron`**

**Parameters:**
None

**Returns:** `'NeuronInfoLite'`

---

## **`from_weights_bonds_and_neuron_lite`**

**Parameters:**
- `cls`
- `neuron_lite`: `'NeuronInfoLite'`
- `weights_as_dict`: `Dict[int, List[Tuple[int, int]]]`
- `bonds_as_dict`: `Dict[int, List[Tuple[int, int]]]`

**Returns:** `'NeuronInfo'`

---

## **`delegated_list_from_vec_u8`**

**Docstring:**
```
Returns a list of Tuples of DelegateInfo objects, and Balance, from a ``vec_u8``.

This is the list of delegates that the user has delegated to, and the amount of stake delegated.
```

**Parameters:**
- `cls`
- `vec_u8`: `List[int]`

**Returns:** `List[Tuple['DelegateInfo', Balance]]`

---

## **`list_of_tuple_from_vec_u8`**

**Docstring:**
```
Returns a list of StakeInfo objects from a ``vec_u8``.
```

**Parameters:**
- `cls`
- `vec_u8`: `List[int]`

**Returns:** `Dict[str, List['StakeInfo']]`

---

## **`encode`**

**Docstring:**
```
Returns a dictionary of the IPInfo object that can be encoded.
```

**Parameters:**
- `self`

**Returns:** `Dict[str, Any]`

---

## **`decode_account_id_list`**

**Docstring:**
```
Decodes a list of AccountIds from vec_u8.
```

**Parameters:**
- `cls`
- `vec_u8`: `List[int]`

**Returns:** `Optional[List[str]]`

---

## **`__init__`**

**Docstring:**
```
Init bittensor wallet object containing a hot and coldkey.
Args:
    _mock (required=True, default=False):
        If true creates a mock wallet with random keys.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`get_save_dir`**

**Docstring:**
```
Return directory path from ``network`` and ``netuid``.

Args:
    network (str): Network name.
    netuid (int): Network UID.

Returns:
    str: Directory path.
```

**Parameters:**
- `network`: `str`
- `netuid`: `int`

**Returns:** `str`

---

## **`latest_block_path`**

**Docstring:**
```
Get the latest block path from the directory.

Args:
    dir_path (str): Directory path.

Returns:
    str: Latest block path.
```

**Parameters:**
- `dir_path`: `str`

**Returns:** `str`

---

## **`S`**

**Docstring:**
```
Represents the stake of each neuron in the Bittensor network. Stake is an important concept in the
Bittensor ecosystem, signifying the amount of network weight (or “stake”) each neuron holds,
represented on a digital ledger. The stake influences a neuron's ability to contribute to and benefit
from the network, playing a crucial role in the distribution of incentives and decision-making processes.

Returns:
    NDArray: A tensor representing the stake of each neuron in the network. Higher values signify a greater stake held by the respective neuron.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`R`**

**Docstring:**
```
Contains the ranks of neurons in the Bittensor network. Ranks are determined by the network based
on each neuron's performance and contributions. Higher ranks typically indicate a greater level of
contribution or performance by a neuron. These ranks are crucial in determining the distribution of
incentives within the network, with higher-ranked neurons receiving more incentive.

Returns:
    NDArray: A tensor where each element represents the rank of a neuron. Higher values indicate higher ranks within the network.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`I`**

**Docstring:**
```
Incentive values of neurons represent the rewards they receive for their contributions to the network.
The Bittensor network employs an incentive mechanism that rewards neurons based on their
informational value, stake, and consensus with other peers. This ensures that the most valuable and
trusted contributions are incentivized.

Returns:
    NDArray: A tensor of incentive values, indicating the rewards or benefits accrued by each neuron based on their contributions and network consensus.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`E`**

**Docstring:**
```
Denotes the emission values of neurons in the Bittensor network. Emissions refer to the distribution or
release of rewards (often in the form of cryptocurrency) to neurons, typically based on their stake and
performance. This mechanism is central to the network's incentive model, ensuring that active and
contributing neurons are appropriately rewarded.

Returns:
    NDArray: A tensor where each element represents the emission value for a neuron, indicating the amount of reward distributed to that neuron.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`C`**

**Docstring:**
```
Represents the consensus values of neurons in the Bittensor network. Consensus is a measure of how
much a neuron's contributions are trusted and agreed upon by the majority of the network. It is
calculated based on a staked weighted trust system, where the network leverages the collective
judgment of all participating peers. Higher consensus values indicate that a neuron's contributions
are more widely trusted and valued across the network.

Returns:
    NDArray: A tensor of consensus values, where each element reflects the level of trust and agreement a neuron has achieved within the network.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`T`**

**Docstring:**
```
Represents the trust values assigned to each neuron in the Bittensor network. Trust is a key metric that
reflects the reliability and reputation of a neuron based on its past behavior and contributions. It is
an essential aspect of the network's functioning, influencing decision-making processes and interactions
between neurons.

The trust matrix is inferred from the network's inter-peer weights, indicating the level of trust each neuron
has in others. A higher value in the trust matrix suggests a stronger trust relationship between neurons.

Returns:
    NDArray: A tensor of trust values, where each element represents the trust level of a neuron. Higher values denote a higher level of trust within the network.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`Tv`**

**Docstring:**
```
Contains the validator trust values of neurons in the Bittensor network. Validator trust is specifically
associated with neurons that act as validators within the network. This specialized form of trust reflects
the validators' reliability and integrity in their role, which is crucial for maintaining the network's
stability and security.

Validator trust values are particularly important for the network's consensus and validation processes,
determining the validators' influence and responsibilities in these critical functions.

Returns:
    NDArray: A tensor of validator trust values, specifically applicable to neurons serving as validators, where higher values denote greater trustworthiness in their validation roles.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`D`**

**Docstring:**
```
Represents the dividends received by neurons in the Bittensor network. Dividends are a form of reward or
distribution, typically given to neurons based on their stake, performance, and contribution to the network.
They are an integral part of the network's incentive structure, encouraging active and beneficial participation.

Returns:
    NDArray: A tensor of dividend values, where each element indicates the dividends received by a neuron, reflecting their share of network rewards.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`B`**

**Docstring:**
```
Bonds in the Bittensor network represent a speculative reward mechanism where neurons can accumulate
bonds in other neurons. Bonds are akin to investments or stakes in other neurons, reflecting a belief in
their future value or performance. This mechanism encourages correct weighting and collaboration
among neurons while providing an additional layer of incentive.

Returns:
    NDArray: A tensor representing the bonds held by each neuron, where each value signifies the proportion of bonds owned by one neuron in another.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`W`**

**Docstring:**
```
Represents the weights assigned to each neuron in the Bittensor network. In the context of Bittensor,
weights are crucial for determining the influence and interaction between neurons. Each neuron is responsible
for setting its weights, which are then recorded on a digital ledger. These weights are reflective of the
neuron's assessment or judgment of other neurons in the network.

The weight matrix :math:`W = [w_{ij}]` is a key component of the network's architecture, where the :math:`i^{th}` row is set by
neuron :math:`i` and represents its weights towards other neurons. These weights influence the ranking and incentive
mechanisms within the network. Higher weights from a neuron towards another can imply greater trust or value
placed on that neuron's contributions.

Returns:
    NDArray: A tensor of inter-peer weights, where each element :math:`w_{ij}` represents the weight assigned by neuron :math:`i` to neuron :math:`j`. This matrix is fundamental to the network's functioning, influencing the distribution of incentives and the inter-neuronal dynamics.
```

**Parameters:**
- `self`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`hotkeys`**

**Docstring:**
```
Represents a list of ``hotkeys`` for each neuron in the Bittensor network.

Hotkeys are unique identifiers used by neurons for active participation in the network, such as sending and receiving information or
transactions. They are akin to public keys in cryptographic systems and are essential for identifying and authenticating neurons within the network's operations.

Returns:
    List[str]: A list of hotkeys, with each string representing the hotkey of a corresponding neuron.

    These keys are crucial for the network's security and integrity, ensuring proper identification and authorization of network participants.

Note:
    While the `NeurIPS paper <https://bittensor.com/pdfs/academia/NeurIPS_DAO_Workshop_2022_3_3.pdf>`_ may not explicitly detail the concept of hotkeys, they are a fundamental  of decentralized networks for secure and authenticated interactions.
```

**Parameters:**
- `self`

**Returns:** `List[str]`

---

## **`coldkeys`**

**Docstring:**
```
Contains a list of ``coldkeys`` for each neuron in the Bittensor network.

Coldkeys are similar to hotkeys but are typically used for more secure, offline activities such as storing assets or offline signing of transactions. They are an important aspect of a neuron's security, providing an additional layer of protection for sensitive operations and assets.

Returns:
    List[str]: A list of coldkeys, each string representing the coldkey of a neuron. These keys play a vital role in the secure management of assets and sensitive operations within the network.

Note:
    The concept of coldkeys, while not explicitly covered in the NeurIPS paper, is a standard practice in
    blockchain and decentralized networks for enhanced security and asset protection.
```

**Parameters:**
- `self`

**Returns:** `List[str]`

---

## **`addresses`**

**Docstring:**
```
Provides a list of IP addresses for each neuron in the Bittensor network. These addresses are used for
network communication, allowing neurons to connect, interact, and exchange information with each other.
IP addresses are fundamental for the network's peer-to-peer communication infrastructure.

Returns:
    List[str]: A list of IP addresses, with each string representing the address of a neuron. These addresses enable the decentralized, distributed nature of the network, facilitating direct communication and data exchange among neurons.

Note:
    While IP addresses are a basic aspect of network communication, specific details about their use in
    the Bittensor network may not be covered in the `NeurIPS paper <https://bittensor.com/pdfs/academia/NeurIPS_DAO_Workshop_2022_3_3.pdf>`_. They are, however, integral to the
    functioning of any distributed network.
```

**Parameters:**
- `self`

**Returns:** `List[str]`

---

## **`metadata`**

**Docstring:**
```
Retrieves the metadata of the metagraph, providing key information about the current state of the
Bittensor network. This metadata includes details such as the network's unique identifier (``netuid``),
the total number of neurons (``n``), the current block number, the network's name, and the version of
the Bittensor network.

Returns:
    dict: A dictionary containing essential metadata about the metagraph, including:

    - ``netuid``: The unique identifier for the network.
    - ``n``: The total number of neurons in the network.
    - ``block``: The current block number in the network's blockchain.
    - ``network``: The name of the Bittensor network.
    - ``version``: The version number of the Bittensor software.

Note:
    This metadata is crucial for understanding the current state and configuration of the network, as well as for tracking its evolution over time.
```

**Parameters:**
- `self`

**Returns:** `dict`

---

## **`state_dict`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`sync`**

**Docstring:**
```
Synchronizes the metagraph with the Bittensor network's current state. It updates the metagraph's attributes
to reflect the latest data from the network, ensuring the metagraph represents the most current state of the network.

Args:
    block (Optional[int]): A specific block number to synchronize with. If None, the metagraph syncs with the latest block.
                            This allows for historical analysis or specific state examination of the network.
    lite (bool): If True, a lite version of the metagraph is used for quicker synchronization. This is beneficial
                when full detail is not necessary, allowing for reduced computational and time overhead.
    subtensor (Optional[bittensor.subtensor]): An instance of the subtensor class from Bittensor, providing an
                                                interface to the underlying blockchain data. If provided, this
                                                instance is used for data retrieval during synchronization.

Returns:
    metagraph: The metagraph instance, updated to the state of the specified block or the latest network state.

Example:
    Sync the metagraph with the latest block from the subtensor, using the lite version for efficiency::

        metagraph.sync(subtensor=subtensor)

    Sync with a specific block number for detailed analysis::

        metagraph.sync(block=12345, lite=False, subtensor=subtensor)

NOTE:
    If attempting to access data beyond the previous 300 blocks, you **must** use the ``archive`` network for subtensor.
    Light nodes are configured only to store the previous 300 blocks if connecting to finney or test networks.

    For example::

        subtensor = bittensor.subtensor(network='archive')
```

**Parameters:**
- `self`
- `block`: `Optional[int]`
- `lite`: `bool`
- `subtensor`: `Optional['bittensor.subtensor']`

**Returns:** `None specified`

---

## **`_initialize_subtensor`**

**Docstring:**
```
Initializes the subtensor to be used for syncing the metagraph.

This method ensures that a subtensor instance is available and properly set up for data retrieval during the synchronization process.

If no subtensor is provided, this method is responsible for creating a new instance of the subtensor, configured according to the current network settings.

Args:
    subtensor: The subtensor instance provided for initialization. If ``None``, a new subtensor instance is created using the current network configuration.

Returns:
    subtensor: The initialized subtensor instance, ready to be used for syncing the metagraph.

Internal Usage:
    Used internally during the sync process to ensure a valid subtensor instance is available::

        subtensor = self._initialize_subtensor(subtensor)
```

**Parameters:**
- `self`
- `subtensor`

**Returns:** `None specified`

---

## **`_assign_neurons`**

**Docstring:**
```
Assigns neurons to the metagraph based on the provided block number and the lite flag.

This method is responsible for fetching and setting the neuron data in the metagraph, which includes neuron attributes like UID, stake, trust, and other relevant information.

Args:
    block: The block number for which the neuron data needs to be fetched. If ``None``, the latest block data is used.
    lite: A boolean flag indicating whether to use a lite version of the neuron data. The lite version typically includes essential information and is quicker to fetch and process.
    subtensor: The subtensor instance used for fetching neuron data from the network.

Internal Usage:
    Used internally during the sync process to fetch and set neuron data::

        self._assign_neurons(block, lite, subtensor)
```

**Parameters:**
- `self`
- `block`
- `lite`
- `subtensor`

**Returns:** `None specified`

---

## **`_create_tensor`**

**Docstring:**
```
Creates a numpy array with the given data and data type. This method is a utility function used internally to encapsulate data into a np.array, making it compatible with the metagraph's numpy model structure.

Args:
    data: The data to be included in the tensor. This could be any numeric data, like stakes, ranks, etc.
    dtype: The data type for the tensor, typically a numpy data type like ``np.float32`` or ``np.int64``.

Returns:
    A tensor parameter encapsulating the provided data.

Internal Usage:
    Used internally to create tensor parameters for various metagraph attributes::

        self.stake = self._create_tensor(neuron_stakes, dtype=np.float32)
```

**Parameters:**
- `data`
- `dtype`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`_set_weights_and_bonds`**

**Docstring:**
```
Computes and sets the weights and bonds for each neuron in the metagraph. This method is responsible for processing the raw weight and bond data obtained from the network and converting it into a structured format suitable for the metagraph model.

Args:
    subtensor: The subtensor instance used for fetching weights and bonds data. If ``None``, the weights and bonds are not updated.

Internal Usage:
    Used internally during the sync process to update the weights and bonds of the neurons::

        self._set_weights_and_bonds(subtensor=subtensor)
```

**Parameters:**
- `self`
- `subtensor`: `Optional[bittensor.subtensor]`

**Returns:** `None specified`

---

## **`_process_weights_or_bonds`**

**Docstring:**
```
Processes the raw weights or bonds data and converts it into a structured tensor format. This method handles the transformation of neuron connection data (``weights`` or ``bonds``) from a list or other unstructured format into a tensor that can be utilized within the metagraph model.

Args:
    data: The raw weights or bonds data to be processed. This data typically comes from the subtensor.
    attribute: A string indicating whether the data is ``weights`` or ``bonds``, which determines the specific processing steps to be applied.

Returns:
    A tensor parameter encapsulating the processed weights or bonds data.

Internal Usage:
    Used internally to process and set weights or bonds for the neurons::

        self.weights = self._process_weights_or_bonds(raw_weights_data, "weights")
```

**Parameters:**
- `self`
- `data`
- `attribute`: `str`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`_set_metagraph_attributes`**

**Docstring:**
```
Sets various attributes of the metagraph based on the latest network data fetched from the subtensor.

This method updates parameters like the number of neurons, block number, stakes, trusts, ranks, and other neuron-specific information.

Args:
    block: The block number for which the metagraph attributes need to be set. If ``None``, the latest block data is used.
    subtensor: The subtensor instance used for fetching the latest network data.

Internal Usage:
    Used internally during the sync process to update the metagraph's attributes::

        self._set_metagraph_attributes(block, subtensor)
```

**Parameters:**
- `self`
- `block`
- `subtensor`

**Returns:** `None specified`

---

## **`_process_root_weights`**

**Docstring:**
```
Specifically processes the root weights data for the metagraph. This method is similar to :func:`_process_weights_or_bonds` but is tailored for processing root weights, which have a different structure and significance in the network.

Args:
    data: The raw root weights data to be processed.
    attribute: A string indicating the attribute type, here it's typically ``weights``.
    subtensor: The subtensor instance used for additional data and context needed in processing.

Returns:
    A tensor parameter encapsulating the processed root weights data.

Internal Usage:
    Used internally to process and set root weights for the metagraph::

        self.root_weights = self._process_root_weights(
            raw_root_weights_data, "weights", subtensor
            )
```

**Parameters:**
- `self`
- `data`
- `attribute`: `str`
- `subtensor`: `bittensor.subtensor`

**Returns:** `Union[NDArray, 'torch.nn.Parameter']`

---

## **`save`**

**Docstring:**
```
Saves the current state of the metagraph to a file on disk. This function is crucial for persisting the current state of the network's metagraph, which can later be reloaded or analyzed. The save operation includes all neuron attributes and parameters, ensuring a complete snapshot of the metagraph's state.

Returns:
    metagraph: The metagraph instance after saving its state.

Example:
    Save the current state of the metagraph to the default directory::

        metagraph.save()

    The saved state can later be loaded to restore or analyze the metagraph's state at this point.

    If using the default save path::

        metagraph.load()

    If using a custom save path::

        metagraph.load_from_path(dir_path)
```

**Parameters:**
- `self`

**Returns:** `'metagraph'`

---

## **`load`**

**Docstring:**
```
Loads the state of the metagraph from the default save directory. This method is instrumental for restoring the metagraph to its last saved state. It automatically identifies the save directory based on the ``network`` and ``netuid`` properties of the metagraph, locates the latest block file in that directory, and loads all metagraph parameters from it.

This functionality is particularly beneficial when continuity in the state of the metagraph is necessary
across different runtime sessions, or after a restart of the system. It ensures that the metagraph reflects
the exact state it was in at the last save point, maintaining consistency in the network's representation.

The method delegates to ``load_from_path``, supplying it with the directory path constructed from the metagraph's current ``network`` and ``netuid`` properties. This abstraction simplifies the process of loading the metagraph's state for the user, requiring no direct path specifications.

Returns:
    metagraph: The metagraph instance after loading its state from the default directory.

Example:
    Load the metagraph state from the last saved snapshot in the default directory::

        metagraph.load()

    After this operation, the metagraph's parameters and neuron data are restored to their state at the time of the last save in the default directory.

Note:
    The default save directory is determined based on the metagraph's ``network`` and ``netuid`` attributes. It is important to ensure that these attributes are set correctly and that the default save directory contains the appropriate state files for the metagraph.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`load_from_path`**

**Parameters:**
- `self`
- `dir_path`: `str`

**Returns:** `'metagraph'`

---

## **`display_mnemonic_msg`**

**Docstring:**
```
Display the mnemonic and a warning message to keep the mnemonic safe.

Args:
    keypair (Keypair): Keypair object.
    key_type (str): Type of the key (coldkey or hotkey).
```

**Parameters:**
- `keypair`: `Keypair`
- `key_type`: `str`

**Returns:** `None specified`

---

## **`config`**

**Docstring:**
```
Get config from the argument parser.

Return:
    config (bittensor.config): config object
```

**Parameters:**
- `cls`

**Returns:** `bittensor.config`

---

## **`help`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`add_args`**

**Parameters:**
- `parser`: `argparse.ArgumentParser`

**Returns:** `None specified`

---

## **`create_if_non_existent`**

**Docstring:**
```
Checks for existing coldkeypub and hotkeys, and creates them if non-existent.

Args:
    coldkey_use_password (bool, optional): Whether to use a password for coldkey. Defaults to ``True``.
    hotkey_use_password (bool, optional): Whether to use a password for hotkey. Defaults to ``False``.

Returns:
    wallet: The wallet object.
```

**Parameters:**
- `self`
- `coldkey_use_password`: `bool`
- `hotkey_use_password`: `bool`

**Returns:** `'wallet'`

---

## **`create`**

**Docstring:**
```
Checks for existing coldkeypub and hotkeys, and creates them if non-existent.

Args:
    coldkey_use_password (bool, optional): Whether to use a password for coldkey. Defaults to ``True``.
    hotkey_use_password (bool, optional): Whether to use a password for hotkey. Defaults to ``False``.

Returns:
    wallet: The wallet object.
```

**Parameters:**
- `self`
- `coldkey_use_password`: `bool`
- `hotkey_use_password`: `bool`

**Returns:** `'wallet'`

---

## **`recreate`**

**Docstring:**
```
Checks for existing coldkeypub and hotkeys and creates them if non-existent.

Args:
    coldkey_use_password (bool, optional): Whether to use a password for coldkey. Defaults to ``True``.
    hotkey_use_password (bool, optional): Whether to use a password for hotkey. Defaults to ``False``.

Returns:
    wallet: The wallet object.
```

**Parameters:**
- `self`
- `coldkey_use_password`: `bool`
- `hotkey_use_password`: `bool`

**Returns:** `'wallet'`

---

## **`hotkey_file`**

**Parameters:**
- `self`

**Returns:** `'bittensor.keyfile'`

---

## **`coldkey_file`**

**Parameters:**
- `self`

**Returns:** `'bittensor.keyfile'`

---

## **`coldkeypub_file`**

**Parameters:**
- `self`

**Returns:** `'bittensor.keyfile'`

---

## **`set_hotkey`**

**Docstring:**
```
Sets the hotkey for the wallet.

Args:
    keypair (bittensor.Keypair): The hotkey keypair.
    encrypt (bool, optional): Whether to encrypt the hotkey. Defaults to ``False``.
    overwrite (bool, optional): Whether to overwrite an existing hotkey. Defaults to ``False``.

Returns:
    bittensor.keyfile: The hotkey file.
```

**Parameters:**
- `self`
- `keypair`: `'bittensor.Keypair'`
- `encrypt`: `bool`
- `overwrite`: `bool`

**Returns:** `'bittensor.keyfile'`

---

## **`set_coldkeypub`**

**Docstring:**
```
Sets the coldkeypub for the wallet.

Args:
    keypair (bittensor.Keypair): The coldkeypub keypair.
    encrypt (bool, optional): Whether to encrypt the coldkeypub. Defaults to ``False``.
    overwrite (bool, optional): Whether to overwrite an existing coldkeypub. Defaults to ``False``.

Returns:
    bittensor.keyfile: The coldkeypub file.
```

**Parameters:**
- `self`
- `keypair`: `'bittensor.Keypair'`
- `encrypt`: `bool`
- `overwrite`: `bool`

**Returns:** `'bittensor.keyfile'`

---

## **`set_coldkey`**

**Docstring:**
```
Sets the coldkey for the wallet.

Args:
    keypair (bittensor.Keypair): The coldkey keypair.
    encrypt (bool, optional): Whether to encrypt the coldkey. Defaults to ``True``.
    overwrite (bool, optional): Whether to overwrite an existing coldkey. Defaults to ``False``.

Returns:
    bittensor.keyfile: The coldkey file.
```

**Parameters:**
- `self`
- `keypair`: `'bittensor.Keypair'`
- `encrypt`: `bool`
- `overwrite`: `bool`

**Returns:** `'bittensor.keyfile'`

---

## **`get_coldkey`**

**Docstring:**
```
Gets the coldkey from the wallet.

Args:
    password (str, optional): The password to decrypt the coldkey. Defaults to ``None``.

Returns:
    bittensor.Keypair: The coldkey keypair.
```

**Parameters:**
- `self`
- `password`: `str`

**Returns:** `'bittensor.Keypair'`

---

## **`get_hotkey`**

**Docstring:**
```
Gets the hotkey from the wallet.

Args:
    password (str, optional): The password to decrypt the hotkey. Defaults to ``None``.

Returns:
    bittensor.Keypair: The hotkey keypair.
```

**Parameters:**
- `self`
- `password`: `str`

**Returns:** `'bittensor.Keypair'`

---

## **`get_coldkeypub`**

**Docstring:**
```
Gets the coldkeypub from the wallet.

Args:
    password (str, optional): The password to decrypt the coldkeypub. Defaults to ``None``.

Returns:
    bittensor.Keypair: The coldkeypub keypair.
```

**Parameters:**
- `self`
- `password`: `str`

**Returns:** `'bittensor.Keypair'`

---

## **`hotkey`**

**Docstring:**
```
Loads the hotkey from wallet.path/wallet.name/hotkeys/wallet.hotkey or raises an error.

Returns:
    hotkey (Keypair):
        hotkey loaded from config arguments.
Raises:
    KeyFileError: Raised if the file is corrupt of non-existent.
    CryptoKeyError: Raised if the user enters an incorrec password for an encrypted keyfile.
```

**Parameters:**
- `self`

**Returns:** `'bittensor.Keypair'`

---

## **`coldkey`**

**Docstring:**
```
Loads the hotkey from wallet.path/wallet.name/coldkey or raises an error.

Returns:
    coldkey (Keypair): coldkey loaded from config arguments.
Raises:
    KeyFileError: Raised if the file is corrupt of non-existent.
    CryptoKeyError: Raised if the user enters an incorrec password for an encrypted keyfile.
```

**Parameters:**
- `self`

**Returns:** `'bittensor.Keypair'`

---

## **`coldkeypub`**

**Docstring:**
```
Loads the coldkeypub from wallet.path/wallet.name/coldkeypub.txt or raises an error.

Returns:
    coldkeypub (Keypair): coldkeypub loaded from config arguments.
Raises:
    KeyFileError: Raised if the file is corrupt of non-existent.
    CryptoKeyError: Raised if the user enters an incorrect password for an encrypted keyfile.
```

**Parameters:**
- `self`

**Returns:** `'bittensor.Keypair'`

---

## **`create_coldkey_from_uri`**

**Docstring:**
```
Creates coldkey from suri string, optionally encrypts it with the user-provided password.

Args:
    uri: (str, required):
        URI string to use i.e., ``/Alice`` or ``/Bob``.
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determines if this operation overwrites the coldkey under the same path ``<wallet path>/<wallet name>/coldkey``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created coldkey.
```

**Parameters:**
- `self`
- `uri`: `str`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`create_hotkey_from_uri`**

**Docstring:**
```
Creates hotkey from suri string, optionally encrypts it with the user-provided password.

Args:
    uri: (str, required):
        URI string to use i.e., ``/Alice`` or ``/Bob``
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determines if this operation overwrites the hotkey under the same path ``<wallet path>/<wallet name>/hotkeys/<hotkey>``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created hotkey.
```

**Parameters:**
- `self`
- `uri`: `str`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`new_coldkey`**

**Docstring:**
```
Creates a new coldkey, optionally encrypts it with the user-provided password and saves to disk.

Args:
    n_words: (int, optional):
        Number of mnemonic words to use.
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determines if this operation overwrites the coldkey under the same path ``<wallet path>/<wallet name>/coldkey``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created coldkey.
```

**Parameters:**
- `self`
- `n_words`: `int`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`create_new_coldkey`**

**Docstring:**
```
Creates a new coldkey, optionally encrypts it with the user-provided password and saves to disk.

Args:
    n_words: (int, optional):
        Number of mnemonic words to use.
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determines if this operation overwrites the coldkey under the same path ``<wallet path>/<wallet name>/coldkey``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created coldkey.
```

**Parameters:**
- `self`
- `n_words`: `int`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`new_hotkey`**

**Docstring:**
```
Creates a new hotkey, optionally encrypts it with the user-provided password and saves to disk.

Args:
    n_words: (int, optional):
        Number of mnemonic words to use.
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determines if this operation overwrites the hotkey under the same path ``<wallet path>/<wallet name>/hotkeys/<hotkey>``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created hotkey.
```

**Parameters:**
- `self`
- `n_words`: `int`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`create_new_hotkey`**

**Docstring:**
```
Creates a new hotkey, optionally encrypts it with the user-provided password and saves to disk.

Args:
    n_words: (int, optional):
        Number of mnemonic words to use.
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Will this operation overwrite the hotkey under the same path <wallet path>/<wallet name>/hotkeys/<hotkey>
Returns:
    wallet (bittensor.wallet):
        This object with newly created hotkey.
```

**Parameters:**
- `self`
- `n_words`: `int`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`regenerate_coldkeypub`**

**Docstring:**
```
Regenerates the coldkeypub from the passed ``ss58_address`` or public_key and saves the file. Requires either ``ss58_address`` or public_key to be passed.

Args:
    ss58_address: (str, optional):
        Address as ``ss58`` string.
    public_key: (str | bytes, optional):
        Public key as hex string or bytes.
    overwrite (bool, optional) (default: False):
        Determins if this operation overwrites the coldkeypub (if exists) under the same path ``<wallet path>/<wallet name>/coldkeypub``.
Returns:
    wallet (bittensor.wallet):
        Newly re-generated wallet with coldkeypub.
```

**Parameters:**
- `self`
- `ss58_address`: `Optional[str]`
- `public_key`: `Optional[Union[str, bytes]]`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`regenerate_coldkey`**

**Docstring:**
```
Regenerates the coldkey from the passed mnemonic or seed, or JSON encrypts it with the user's password and saves the file.

Args:
    mnemonic: (Union[list, str], optional):
        Key mnemonic as list of words or string space separated words.
    seed: (str, optional):
        Seed as hex string.
    json: (Tuple[Union[str, Dict], str], optional):
        Restore from encrypted JSON backup as ``(json_data: Union[str, Dict], passphrase: str)``
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determines if this operation overwrites the coldkey under the same path ``<wallet path>/<wallet name>/coldkey``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created coldkey.

Note:
    Uses priority order: ``mnemonic > seed > json``.
```

**Parameters:**
- `self`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`regenerate_hotkey`**

**Docstring:**
```
Regenerates the hotkey from passed mnemonic or seed, encrypts it with the user's password and saves the file.

Args:
    mnemonic: (Union[list, str], optional):
        Key mnemonic as list of words or string space separated words.
    seed: (str, optional):
        Seed as hex string.
    json: (Tuple[Union[str, Dict], str], optional):
        Restore from encrypted JSON backup as ``(json_data: Union[str, Dict], passphrase: str)``.
    use_password (bool, optional):
        Is the created key password protected.
    overwrite (bool, optional):
        Determies if this operation overwrites the hotkey under the same path ``<wallet path>/<wallet name>/hotkeys/<hotkey>``.
Returns:
    wallet (bittensor.wallet):
        This object with newly created hotkey.
```

**Parameters:**
- `self`
- `use_password`: `bool`
- `overwrite`: `bool`
- `suppress`: `bool`

**Returns:** `'wallet'`

---

## **`serialized_keypair_to_keyfile_data`**

**Docstring:**
```
Serializes keypair object into keyfile data.

Args:
    keypair (bittensor.Keypair): The keypair object to be serialized.
Returns:
    data (bytes): Serialized keypair data.
```

**Parameters:**
- `keypair`: `'bittensor.Keypair'`

**Returns:** `bytes`

---

## **`deserialize_keypair_from_keyfile_data`**

**Docstring:**
```
Deserializes Keypair object from passed keyfile data.

Args:
    keyfile_data (bytes): The keyfile data as bytes to be loaded.
Returns:
    keypair (bittensor.Keypair): The Keypair loaded from bytes.
Raises:
    KeyFileError: Raised if the passed bytes cannot construct a keypair object.
```

**Parameters:**
- `keyfile_data`: `bytes`

**Returns:** `'bittensor.Keypair'`

---

## **`validate_password`**

**Docstring:**
```
Validates the password against a password policy.

Args:
    password (str): The password to verify.
Returns:
    valid (bool): ``True`` if the password meets validity requirements.
```

**Parameters:**
- `password`: `str`

**Returns:** `bool`

---

## **`ask_password_to_encrypt`**

**Docstring:**
```
Prompts the user to enter a password for key encryption.

Returns:
    password (str): The valid password entered by the user.
```

**Parameters:**
None

**Returns:** `str`

---

## **`keyfile_data_is_encrypted_nacl`**

**Docstring:**
```
Returns true if the keyfile data is NaCl encrypted.

Args:
    keyfile_data ( bytes, required ):
        Bytes to validate.
Returns:
    is_nacl (bool):
        ``True`` if data is ansible encrypted.
```

**Parameters:**
- `keyfile_data`: `bytes`

**Returns:** `bool`

---

## **`keyfile_data_is_encrypted_ansible`**

**Docstring:**
```
Returns true if the keyfile data is ansible encrypted.

Args:
    keyfile_data (bytes): The bytes to validate.
Returns:
    is_ansible (bool): True if the data is ansible encrypted.
```

**Parameters:**
- `keyfile_data`: `bytes`

**Returns:** `bool`

---

## **`keyfile_data_is_encrypted_legacy`**

**Docstring:**
```
Returns true if the keyfile data is legacy encrypted.
Args:
    keyfile_data (bytes): The bytes to validate.
Returns:
    is_legacy (bool): ``True`` if the data is legacy encrypted.
```

**Parameters:**
- `keyfile_data`: `bytes`

**Returns:** `bool`

---

## **`keyfile_data_is_encrypted`**

**Docstring:**
```
Returns ``true`` if the keyfile data is encrypted.

Args:
    keyfile_data (bytes): The bytes to validate.
Returns:
    is_encrypted (bool): ``True`` if the data is encrypted.
```

**Parameters:**
- `keyfile_data`: `bytes`

**Returns:** `bool`

---

## **`keyfile_data_encryption_method`**

**Docstring:**
```
Returns ``true`` if the keyfile data is encrypted.

Args:
    keyfile_data ( bytes, required ):
        Bytes to validate
Returns:
    encryption_method (bool):
        ``True`` if data is encrypted.
```

**Parameters:**
- `keyfile_data`: `bytes`

**Returns:** `bool`

---

## **`legacy_encrypt_keyfile_data`**

**Parameters:**
- `keyfile_data`: `bytes`
- `password`: `str`

**Returns:** `bytes`

---

## **`encrypt_keyfile_data`**

**Docstring:**
```
Encrypts the passed keyfile data using ansible vault.

Args:
    keyfile_data (bytes): The bytes to encrypt.
    password (str, optional): The password used to encrypt the data. If ``None``, asks for user input.
Returns:
    encrypted_data (bytes): The encrypted data.
```

**Parameters:**
- `keyfile_data`: `bytes`
- `password`: `str`

**Returns:** `bytes`

---

## **`get_coldkey_password_from_environment`**

**Docstring:**
```
Retrieves the cold key password from the environment variables.

Args:
    coldkey_name (str): The name of the cold key.
Returns:
    password (str): The password retrieved from the environment variables, or ``None`` if not found.
```

**Parameters:**
- `coldkey_name`: `str`

**Returns:** `Optional[str]`

---

## **`decrypt_keyfile_data`**

**Docstring:**
```
Decrypts the passed keyfile data using ansible vault.

Args:
    keyfile_data (bytes): The bytes to decrypt.
    password (str, optional): The password used to decrypt the data. If ``None``, asks for user input.
    coldkey_name (str, optional): The name of the cold key. If provided, retrieves the password from environment variables.
Returns:
    decrypted_data (bytes): The decrypted data.
Raises:
    KeyFileError: Raised if the file is corrupted or if the password is incorrect.
```

**Parameters:**
- `keyfile_data`: `bytes`
- `password`: `str`
- `coldkey_name`: `Optional[str]`

**Returns:** `bytes`

---

## **`keypair`**

**Parameters:**
- `self`

**Returns:** `'Keypair'`

---

## **`data`**

**Parameters:**
- `self`

**Returns:** `bytes`

---

## **`keyfile_data`**

**Parameters:**
- `self`

**Returns:** `bytes`

---

## **`set_keypair`**

**Parameters:**
- `self`
- `keypair`: `'Keypair'`
- `encrypt`: `bool`
- `overwrite`: `bool`
- `password`: `str`

**Returns:** `None specified`

---

## **`get_keypair`**

**Parameters:**
- `self`
- `password`: `str`

**Returns:** `'Keypair'`

---

## **`make_dirs`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`exists_on_device`**

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`is_readable`**

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`is_writable`**

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`is_encrypted`**

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`_may_overwrite`**

**Docstring:**
```
Asks the user if it is okay to overwrite the file.

Returns:
    may_overwrite (bool): ``True`` if the user allows overwriting the file.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`check_and_update_encryption`**

**Parameters:**
- `self`
- `no_prompt`
- `print_result`

**Returns:** `None specified`

---

## **`encrypt`**

**Parameters:**
- `self`
- `password`: `str`

**Returns:** `None specified`

---

## **`decrypt`**

**Parameters:**
- `self`
- `password`: `str`

**Returns:** `None specified`

---

## **`_read_keyfile_data_from_file`**

**Docstring:**
```
Reads the keyfile data from the file.

Returns:
    keyfile_data (bytes): The keyfile data stored under the path.
Raises:
    KeyFileError: Raised if the file does not exist or is not readable.
```

**Parameters:**
- `self`

**Returns:** `bytes`

---

## **`_write_keyfile_data_to_file`**

**Docstring:**
```
Writes the keyfile data to the file.

Args:
    keyfile_data (bytes): The byte data to store under the path.
    overwrite (bool, optional): If ``True``, overwrites the data without asking for permission from the user. Default is ``False``.
Raises:
    KeyFileError: Raised if the file is not writable or the user responds No to the overwrite prompt.
```

**Parameters:**
- `self`
- `keyfile_data`: `bytes`
- `overwrite`: `bool`

**Returns:** `None specified`

---

## **`close_session`**

**Docstring:**
```
Closes the internal `aiohttp <https://github.com/aio-libs/aiohttp>`_ client session synchronously.

This method ensures the proper closure and cleanup of the aiohttp client session, releasing any
resources like open connections and internal buffers. It is crucial for preventing resource leakage
and should be called when the dendrite instance is no longer in use, especially in synchronous contexts.

Note:
    This method utilizes asyncio's event loop to close the session asynchronously from a synchronous context. It is advisable to use this method only when asynchronous context management is not feasible.

Usage:
    When finished with dendrite in a synchronous context
    :func:`dendrite_instance.close_session()`.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`_get_endpoint_url`**

**Docstring:**
```
Constructs the endpoint URL for a network request to a target axon.

This internal method generates the full HTTP URL for sending a request to the specified axon. The
URL includes the IP address and port of the target axon, along with the specific request name. It
differentiates between requests to the local system (using '0.0.0.0') and external systems.

Args:
    target_axon: The target axon object containing IP and port information.
    request_name: The specific name of the request being made.

Returns:
    str: A string representing the complete HTTP URL for the request.
```

**Parameters:**
- `self`
- `target_axon`
- `request_name`

**Returns:** `None specified`

---

## **`_handle_request_errors`**

**Docstring:**
```
Handles exceptions that occur during network requests, updating the synapse with appropriate status codes and messages.

This method interprets different types of exceptions and sets the corresponding status code and
message in the synapse object. It covers common network errors such as connection issues and timeouts.

Args:
    synapse: The synapse object associated with the request.
    request_name: The name of the request during which the exception occurred.
    exception: The exception object caught during the request.

Note:
    This method updates the synapse object in-place.
```

**Parameters:**
- `self`
- `synapse`
- `request_name`
- `exception`

**Returns:** `None specified`

---

## **`_log_outgoing_request`**

**Docstring:**
```
Logs information about outgoing requests for debugging purposes.

This internal method logs key details about each outgoing request, including the size of the
request, the name of the synapse, the axon's details, and a success indicator. This information
is crucial for monitoring and debugging network activity within the Bittensor network.

To turn on debug messages, set the environment variable BITTENSOR_DEBUG to ``1``, or call the bittensor debug method like so::

    import bittensor
    bittensor.debug()

Args:
    synapse: The synapse object representing the request being sent.
```

**Parameters:**
- `self`
- `synapse`

**Returns:** `None specified`

---

## **`_log_incoming_response`**

**Docstring:**
```
Logs information about incoming responses for debugging and monitoring.

Similar to :func:`_log_outgoing_request`, this method logs essential details of the incoming responses,
including the size of the response, synapse name, axon details, status code, and status message.
This logging is vital for troubleshooting and understanding the network interactions in Bittensor.

Args:
    synapse: The synapse object representing the received response.
```

**Parameters:**
- `self`
- `synapse`

**Returns:** `None specified`

---

## **`query`**

**Docstring:**
```
Makes a synchronous request to multiple target Axons and returns the server responses.

Cleanup is automatically handled and sessions are closed upon completed requests.

Args:
    axons (Union[List[Union['bittensor.AxonInfo', 'bittensor.axon']], Union['bittensor.AxonInfo', 'bittensor.axon']]):
        The list of target Axon information.
    synapse (bittensor.Synapse, optional): The Synapse object. Defaults to :func:`bittensor.Synapse()`.
    timeout (float, optional): The request timeout duration in seconds.
        Defaults to ``12.0`` seconds.
Returns:
    Union[bittensor.Synapse, List[bittensor.Synapse]]: If a single target axon is provided, returns the response from that axon. If multiple target axons are provided, returns a list of responses from all target axons.
```

**Parameters:**
- `self`

**Returns:** `List[Union[AsyncGenerator[Any, Any], bittensor.Synapse, bittensor.StreamingSynapse]]`

---

## **`preprocess_synapse_for_request`**

**Docstring:**
```
Preprocesses the synapse for making a request. This includes building
headers for Dendrite and Axon and signing the request.

Args:
    target_axon_info (bittensor.AxonInfo): The target axon information.
    synapse (bittensor.Synapse): The synapse object to be preprocessed.
    timeout (float, optional): The request timeout duration in seconds.
        Defaults to ``12.0`` seconds.

Returns:
    bittensor.Synapse: The preprocessed synapse.
```

**Parameters:**
- `self`
- `target_axon_info`: `bittensor.AxonInfo`
- `synapse`: `bittensor.Synapse`
- `timeout`: `float`

**Returns:** `bittensor.Synapse`

---

## **`process_server_response`**

**Docstring:**
```
Processes the server response, updates the local synapse state with the
server's state and merges headers set by the server.

Args:
    server_response (object): The `aiohttp <https://github.com/aio-libs/aiohttp>`_ response object from the server.
    json_response (dict): The parsed JSON response from the server.
    local_synapse (bittensor.Synapse): The local synapse object to be updated.

Raises:
    None: But errors in attribute setting are silently ignored.
```

**Parameters:**
- `self`
- `server_response`: `aiohttp.ClientResponse`
- `json_response`: `dict`
- `local_synapse`: `bittensor.Synapse`

**Returns:** `None specified`

---

## **`__del__`**

**Docstring:**
```
This magic method is called when the Axon object is about to be destroyed.
It ensures that the Axon server shuts down properly.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__split_params__`**

**Parameters:**
- `params`: `argparse.Namespace`
- `_config`: `'config'`

**Returns:** `None specified`

---

## **`__parse_args__`**

**Docstring:**
```
Parses the passed args use the passed parser.

Args:
    args (List[str]):
        List of arguments to parse.
    parser (argparse.ArgumentParser):
        Command line parser object.
    strict (bool):
        If ``true``, the command line arguments are strictly parsed.
Returns:
    Namespace:
        Namespace object created from parser arguments.
```

**Parameters:**
- `args`: `List[str]`
- `parser`: `argparse.ArgumentParser`
- `strict`: `bool`

**Returns:** `argparse.Namespace`

---

## **`__deepcopy__`**

**Parameters:**
- `self`
- `memo`

**Returns:** `'config'`

---

## **`_remove_private_keys`**

**Parameters:**
- `d`

**Returns:** `None specified`

---

## **`copy`**

**Parameters:**
- `self`

**Returns:** `'config'`

---

## **`update_with_kwargs`**

**Docstring:**
```
Add config to self
```

**Parameters:**
- `self`
- `kwargs`

**Returns:** `None specified`

---

## **`_merge`**

**Docstring:**
```
Merge two configurations recursively.
If there is a conflict, the value from the second configuration will take precedence.
```

**Parameters:**
- `cls`
- `a`
- `b`

**Returns:** `None specified`

---

## **`merge`**

**Docstring:**
```
Merges the current config with another config.

Args:
    b: Another config to merge.
```

**Parameters:**
- `self`
- `b`

**Returns:** `None specified`

---

## **`merge_all`**

**Docstring:**
```
Merge all configs in the list into one config.
If there is a conflict, the value from the last configuration in the list will take precedence.

Args:
    configs (list of config):
        List of configs to be merged.

Returns:
    config:
        Merged config object.
```

**Parameters:**
- `cls`
- `configs`: `List['config']`

**Returns:** `'config'`

---

## **`is_set`**

**Docstring:**
```
Returns a boolean indicating whether the parameter has been set or is still the default.
```

**Parameters:**
- `self`
- `param_name`: `str`

**Returns:** `bool`

---

## **`__check_for_missing_required_args`**

**Parameters:**
- `self`
- `parser`: `argparse.ArgumentParser`
- `args`: `List[str]`

**Returns:** `List[str]`

---

## **`__get_required_args_from_parser`**

**Parameters:**
- `parser`: `argparse.ArgumentParser`

**Returns:** `List[str]`

---

## **`default`**

**Parameters:**
- `cls`

**Returns:** `None specified`

---

## **`_worker`**

**Parameters:**
- `executor_reference`
- `work_queue`
- `initializer`
- `initargs`

**Returns:** `None specified`

---

## **`run`**

**Docstring:**
```
Lists wallets.
```

**Parameters:**
- `cli`

**Returns:** `None specified`

---

## **`is_empty`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`submit`**

**Parameters:**
- `self`
- `fn`: `Callable`

**Returns:** `_base.Future`

---

## **`_adjust_thread_count`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`_initializer_failed`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`shutdown`**

**Parameters:**
- `self`
- `wait`

**Returns:** `None specified`

---

## **`weakref_cb`**

**Parameters:**
- `_`
- `q`

**Returns:** `None specified`

---

## **`create_error_response`**

**Parameters:**
- `synapse`: `bittensor.Synapse`

**Returns:** `None specified`

---

## **`log_and_handle_error`**

**Parameters:**
- `synapse`: `bittensor.Synapse`
- `exception`: `Exception`
- `status_code`: `typing.Optional[int]`
- `start_time`: `typing.Optional[float]`

**Returns:** `None specified`

---

## **`install_signal_handlers`**

**Docstring:**
```
Overrides the default signal handlers provided by ``uvicorn.Server``. This method is essential to ensure that the signal handling in the threaded server does not interfere with the main application's flow, especially in a complex asynchronous environment like the Axon server.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`run_in_thread`**

**Docstring:**
```
Manages the execution of the server in a separate thread, allowing the FastAPI application to run asynchronously without blocking the main thread of the Axon server. This method is a key component in enabling concurrent request handling in the Axon server.

Yields:
    None: This method yields control back to the caller while the server is running in the background thread.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`_wrapper_run`**

**Docstring:**
```
A wrapper method for the :func:`run_in_thread` context manager. This method is used internally by the ``start`` method to initiate the server's execution in a separate thread.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`start`**

**Parameters:**
- `self`

**Returns:** `None`

---

## **`stop`**

**Parameters:**
- `self`

**Returns:** `None`

---

## **`info`**

**Docstring:**
```
Wraps info message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`attach`**

**Docstring:**
```
Attaches custom functions to the Axon server for handling incoming requests. This method enables
the Axon to define specific behaviors for request forwarding, verification, blacklisting, and
prioritization, thereby customizing its interaction within the Bittensor network.

Registers an API endpoint to the FastAPI application router.
It uses the name of the first argument of the :func:`forward_fn` function as the endpoint name.

The attach method in the Bittensor framework's axon class is a crucial function for registering
API endpoints to the Axon's FastAPI application router. This method allows the Axon server to
define how it handles incoming requests by attaching functions for forwarding, verifying,
blacklisting, and prioritizing requests. It's a key part of customizing the server's behavior
and ensuring efficient and secure handling of requests within the Bittensor network.

Args:
    forward_fn (Callable): Function to be called when the API endpoint is accessed. It should have at least one argument.
    blacklist_fn (Callable, optional): Function to filter out undesired requests. It should take the same arguments as :func:`forward_fn` and return a boolean value. Defaults to ``None``, meaning no blacklist filter will be used.
    priority_fn (Callable, optional): Function to rank requests based on their priority. It should take the same arguments as :func:`forward_fn` and return a numerical value representing the request's priority. Defaults to ``None``, meaning no priority sorting will be applied.
    verify_fn (Callable, optional): Function to verify requests. It should take the same arguments as :func:`forward_fn` and return a boolean value. If ``None``, :func:`self.default_verify` function will be used.

Note:
    The methods :func:`forward_fn`, :func:`blacklist_fn`, :func:`priority_fn`, and :func:`verify_fn` should be designed to receive the same parameters.

Raises:
    AssertionError: If :func:`forward_fn` does not have the signature: ``forward( synapse: YourSynapse ) -> synapse``.
    AssertionError: If :func:`blacklist_fn` does not have the signature: ``blacklist( synapse: YourSynapse ) -> bool``.
    AssertionError: If :func:`priority_fn` does not have the signature: ``priority( synapse: YourSynapse ) -> float``.
    AssertionError: If :func:`verify_fn` does not have the signature: ``verify( synapse: YourSynapse ) -> None``.

Returns:
    self: Returns the instance of the AxonServer class for potential method chaining.

Example Usage::

    def forward_custom(synapse: MyCustomSynapse) -> MyCustomSynapse:
        # Custom logic for processing the request
        return synapse

    def blacklist_custom(synapse: MyCustomSynapse) -> Tuple[bool, str]:
        return True, "Allowed!"

    def priority_custom(synapse: MyCustomSynapse) -> float:
        return 1.0

    def verify_custom(synapse: MyCustomSynapse):
        # Custom logic for verifying the request
        pass

    my_axon = bittensor.axon(...)
    my_axon.attach(forward_fn=forward_custom, verify_fn=verify_custom)

Note:
    The :func:`attach` method is fundamental in setting up the Axon server's request handling capabilities,
    enabling it to participate effectively and securely in the Bittensor network. The flexibility
    offered by this method allows developers to tailor the Axon's behavior to specific requirements and
    use cases.
```

**Parameters:**
- `self`
- `forward_fn`: `Callable`
- `blacklist_fn`: `Optional[Callable]`
- `priority_fn`: `Optional[Callable]`
- `verify_fn`: `Optional[Callable]`

**Returns:** `'bittensor.axon'`

---

## **`check_config`**

**Parameters:**
- `config`: `'bittensor.config'`

**Returns:** `None specified`

---

## **`serve`**

**Docstring:**
```
Registers a neuron's serving endpoint on the Bittensor network. This function announces the
IP address and port where the neuron is available to serve requests, facilitating peer-to-peer
communication within the network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron being served.
    ip (str): The IP address of the serving neuron.
    port (int): The port number on which the neuron is serving.
    protocol (int): The protocol type used by the neuron (e.g., GRPC, HTTP).
    netuid (int): The unique identifier of the subnetwork.
    placeholder1 (int, optional): Placeholder parameter for future extensions. Default is ``0``.
    placeholder2 (int, optional): Placeholder parameter for future extensions. Default is ``0``.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block. Default is
        ``False``.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain. Default
        is ``True``.

Returns:
    bool: ``True`` if the serve registration is successful, False otherwise.

This function is essential for establishing the neuron's presence in the network, enabling
it to participate in the decentralized machine learning processes of Bittensor.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `ip`: `str`
- `port`: `int`
- `protocol`: `int`
- `netuid`: `int`
- `placeholder1`: `int`
- `placeholder2`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`

**Returns:** `bool`

---

## **`ping`**

**Parameters:**
- `r`: `bittensor.Synapse`

**Returns:** `bittensor.Synapse`

---

## **`get_size`**

**Docstring:**
```
Recursively finds size of objects.

This function traverses every item of a given object and sums their sizes to compute the total size.

Args:
    obj (any type): The object to get the size of.
    seen (set): Set of object ids that have been calculated.

Returns:
    int: The total size of the object.
```

**Parameters:**
- `obj`
- `seen`

**Returns:** `int`

---

## **`cast_int`**

**Docstring:**
```
Converts a string to an integer, if the string is not ``None``.

This function attempts to convert a string to an integer. If the string is ``None``, it simply returns ``None``.

Args:
    raw (str): The string to convert.

Returns:
    int or None: The converted integer, or ``None`` if the input was ``None``.
```

**Parameters:**
- `raw`: `str`

**Returns:** `int`

---

## **`cast_float`**

**Docstring:**
```
Converts a string to a float, if the string is not ``None``.

This function attempts to convert a string to a float. If the string is ``None``, it simply returns ``None``.

Args:
    raw (str): The string to convert.

Returns:
    float or None: The converted float, or ``None`` if the input was ``None``.
```

**Parameters:**
- `raw`: `str`

**Returns:** `float`

---

## **`deserialize`**

**Docstring:**
```
Deserializes the Tensor object.

Returns:
    np.array or torch.Tensor: The deserialized tensor object.

Raises:
    Exception: If the deserialization process encounters an error.
```

**Parameters:**
- `self`

**Returns:** `Union['np.ndarray', 'torch.Tensor']`

---

## **`set_name_type`**

**Parameters:**
- `cls`
- `values`

**Returns:** `dict`

---

## **`__setattr__`**

**Docstring:**
```
Override the :func:`__setattr__` method to make the ``required_hash_fields`` property read-only.

This is a security mechanism such that the ``required_hash_fields`` property cannot be
overridden by the user or malicious code.
```

**Parameters:**
- `self`
- `name`: `str`
- `value`: `Any`

**Returns:** `None specified`

---

## **`get_total_size`**

**Docstring:**
```
Get the total size of the current object.

This method first calculates the size of the current object, then assigns it
to the instance variable :func:`self.total_size` and finally returns this value.

Returns:
    int: The total size of the current object.
```

**Parameters:**
- `self`

**Returns:** `int`

---

## **`is_success`**

**Docstring:**
```
Checks if the dendrite's status code indicates success.

This method returns ``True`` if the status code of the dendrite is ``200``,
which typically represents a successful HTTP request.

Returns:
    bool: ``True`` if dendrite's status code is ``200``, ``False`` otherwise.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`is_failure`**

**Docstring:**
```
Checks if the dendrite's status code indicates failure.

This method returns ``True`` if the status code of the dendrite is not ``200``,
which would mean the HTTP request was not successful.

Returns:
    bool: ``True`` if dendrite's status code is not ``200``, ``False`` otherwise.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`is_timeout`**

**Docstring:**
```
Checks if the dendrite's status code indicates a timeout.

This method returns ``True`` if the status code of the dendrite is ``408``,
which is the HTTP status code for a request timeout.

Returns:
    bool: ``True`` if dendrite's status code is ``408``, ``False`` otherwise.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`is_blacklist`**

**Docstring:**
```
Checks if the dendrite's status code indicates a blacklisted request.

This method returns ``True`` if the status code of the dendrite is ``403``,
which is the HTTP status code for a forbidden request.

Returns:
    bool: ``True`` if dendrite's status code is ``403``, ``False`` otherwise.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`failed_verification`**

**Docstring:**
```
Checks if the dendrite's status code indicates failed verification.

This method returns ``True`` if the status code of the dendrite is ``401``,
which is the HTTP status code for unauthorized access.

Returns:
    bool: ``True`` if dendrite's status code is ``401``, ``False`` otherwise.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`get_required_fields`**

**Docstring:**
```
Get the required fields from the model's JSON schema.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`to_headers`**

**Docstring:**
```
Converts the state of a Synapse instance into a dictionary of HTTP headers.

This method is essential for
packaging Synapse data for network transmission in the Bittensor framework, ensuring that each key aspect of
the Synapse is represented in a format suitable for HTTP communication.

Process:

1. Basic Information: It starts by including the ``name`` and ``timeout`` of the Synapse, which are fundamental for identifying the query and managing its lifespan on the network.
2. Complex Objects: The method serializes the ``axon`` and ``dendrite`` objects, if present, into strings. This serialization is crucial for preserving the state and structure of these objects over the network.
3. Encoding: Non-optional complex objects are serialized and encoded in base64, making them safe for HTTP transport.
4. Size Metrics: The method calculates and adds the size of headers and the total object size, providing valuable information for network bandwidth management.

Example Usage::

    synapse = Synapse(name="ExampleSynapse", timeout=30)
    headers = synapse.to_headers()
    # headers now contains a dictionary representing the Synapse instance

Returns:
    dict: A dictionary containing key-value pairs representing the Synapse's properties, suitable for HTTP communication.
```

**Parameters:**
- `self`

**Returns:** `dict`

---

## **`body_hash`**

**Docstring:**
```
Computes a SHA3-256 hash of the serialized body of the Synapse instance.

This hash is used to
ensure the data integrity and security of the Synapse instance when it's transmitted across the
network. It is a crucial feature for verifying that the data received is the same as the data sent.

Process:

1. Iterates over each required field as specified in ``required_hash_fields``.
2. Concatenates the string representation of these fields.
3. Applies SHA3-256 hashing to the concatenated string to produce a unique fingerprint of the data.

Example::

    synapse = Synapse(name="ExampleRoute", timeout=10)
    hash_value = synapse.body_hash
    # hash_value is the SHA3-256 hash of the serialized body of the Synapse instance

Returns:
    str: The SHA3-256 hash as a hexadecimal string, providing a fingerprint of the Synapse instance's data for integrity checks.
```

**Parameters:**
- `self`

**Returns:** `str`

---

## **`parse_headers_to_inputs`**

**Docstring:**
```
Interprets and transforms a given dictionary of headers into a structured dictionary, facilitating the reconstruction of Synapse objects.

This method is essential for parsing network-transmitted
data back into a Synapse instance, ensuring data consistency and integrity.

Process:

1. Separates headers into categories based on prefixes (``axon``, ``dendrite``, etc.).
2. Decodes and deserializes ``input_obj`` headers into their original objects.
3. Assigns simple fields directly from the headers to the input dictionary.

Example::

    received_headers = {
        'bt_header_axon_address': '127.0.0.1',
        'bt_header_dendrite_port': '8080',
        # Other headers...
    }
    inputs = Synapse.parse_headers_to_inputs(received_headers)
    # inputs now contains a structured representation of Synapse properties based on the headers

Note:
    This is handled automatically when calling :func:`Synapse.from_headers(headers)` and does not need to be called directly.

Args:
    headers (dict): The headers dictionary to parse.

Returns:
    dict: A structured dictionary representing the inputs for constructing a Synapse instance.
```

**Parameters:**
- `cls`
- `headers`: `dict`

**Returns:** `dict`

---

## **`from_headers`**

**Docstring:**
```
Constructs a new Synapse instance from a given headers dictionary, enabling the re-creation of the Synapse's state as it was prior to network transmission.

This method is a key part of the
deserialization process in the Bittensor network, allowing nodes to accurately reconstruct Synapse
objects from received data.

Example::

    received_headers = {
        'bt_header_axon_address': '127.0.0.1',
        'bt_header_dendrite_port': '8080',
        # Other headers...
    }
    synapse = Synapse.from_headers(received_headers)
    # synapse is a new Synapse instance reconstructed from the received headers

Args:
    headers (dict): The dictionary of headers containing serialized Synapse information.

Returns:
    Synapse: A new instance of Synapse, reconstructed from the parsed header information, replicating the original instance's state.
```

**Parameters:**
- `cls`
- `headers`: `dict`

**Returns:** `'Synapse'`

---

## **`convert_type_string`**

**Parameters:**
- `_`
- `name`

**Returns:** `None specified`

---

## **`determine_chain_endpoint_and_network`**

**Docstring:**
```
Determines the chain endpoint and network from the passed network or chain_endpoint.

Args:
    network (str): The network flag. The choices are: ``-- finney`` (main network), ``-- archive``
        (archive network +300 blocks), ``-- local`` (local running network), ``-- test`` (test network).
Returns:
    network (str): The network flag.
    chain_endpoint (str): The chain endpoint flag. If set, overrides the ``network`` argument.
```

**Parameters:**
- `network`: `str`

**Returns:** `None specified`

---

## **`setup_config`**

**Docstring:**
```
Sets up and returns the configuration for the Subtensor network and endpoint.

This method determines the appropriate network and chain endpoint based on the provided network string or
configuration object. It evaluates the network and endpoint in the following order of precedence:
1. Provided network string.
2. Configured chain endpoint in the `config` object.
3. Configured network in the `config` object.
4. Default chain endpoint.
5. Default network.

Args:
    network (str): The name of the Subtensor network. If None, the network and endpoint will be determined from
        the `config` object.
    config (bittensor.config): The configuration object containing the network and chain endpoint settings.

Returns:
    tuple: A tuple containing the formatted WebSocket endpoint URL and the evaluated network name.
```

**Parameters:**
- `network`: `str`
- `config`: `'bittensor.config'`

**Returns:** `None specified`

---

## **`close`**

**Docstring:**
```
Cleans up resources for this subtensor instance like active websocket connection and active extensions.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`nominate`**

**Docstring:**
```
Becomes a delegate for the hotkey associated with the given wallet. This method is used to nominate
a neuron (identified by the hotkey in the wallet) as a delegate on the Bittensor network, allowing it
to participate in consensus and validation processes.

Args:
    wallet (bittensor.wallet): The wallet containing the hotkey to be nominated.
    wait_for_finalization (bool, optional): If ``True``, waits until the transaction is finalized on the
        blockchain.
    wait_for_inclusion (bool, optional): If ``True``, waits until the transaction is included in a block.

Returns:
    bool: ``True`` if the nomination process is successful, ``False`` otherwise.

This function is a key part of the decentralized governance mechanism of Bittensor, allowing for the
dynamic selection and participation of validators in the network's consensus process.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_finalization`: `bool`
- `wait_for_inclusion`: `bool`

**Returns:** `bool`

---

## **`delegate`**

**Docstring:**
```
Becomes a delegate for the hotkey associated with the given wallet. This method is used to nominate
a neuron (identified by the hotkey in the wallet) as a delegate on the Bittensor network, allowing it
to participate in consensus and validation processes.

Args:
    wallet (bittensor.wallet): The wallet containing the hotkey to be nominated.
    delegate_ss58 (Optional[str]): The ``SS58`` address of the delegate neuron.
    amount (Union[Balance, float]): The amount of TAO to undelegate.
    wait_for_finalization (bool, optional): If ``True``, waits until the transaction is finalized on the
        blockchain.
    wait_for_inclusion (bool, optional): If ``True``, waits until the transaction is included in a block.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the nomination process is successful, False otherwise.

This function is a key part of the decentralized governance mechanism of Bittensor, allowing for the
dynamic selection and participation of validators in the network's consensus process.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `delegate_ss58`: `Optional[str]`
- `amount`: `Optional[Union[Balance, float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`undelegate`**

**Docstring:**
```
Removes a specified amount of stake from a delegate neuron using the provided wallet. This action
reduces the staked amount on another neuron, effectively withdrawing support or speculation.

Args:
    wallet (bittensor.wallet): The wallet used for the undelegation process.
    delegate_ss58 (Optional[str]): The ``SS58`` address of the delegate neuron.
    amount (Union[Balance, float]): The amount of TAO to undelegate.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the undelegation is successful, False otherwise.

This function reflects the dynamic and speculative nature of the Bittensor network, allowing neurons
to adjust their stakes and investments based on changing perceptions and performances within the network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `delegate_ss58`: `Optional[str]`
- `amount`: `Optional[Union[Balance, float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`set_take`**

**Docstring:**
```
Set delegate hotkey take
Args:
    wallet (bittensor.wallet): The wallet containing the hotkey to be nominated.
    delegate_ss58 (str, optional): Hotkey
    take (float): Delegate take on subnet ID
    wait_for_finalization (bool, optional): If ``True``, waits until the transaction is finalized on the
        blockchain.
    wait_for_inclusion (bool, optional): If ``True``, waits until the transaction is included in a block.

Returns:
    bool: ``True`` if the process is successful, False otherwise.

This function is a key part of the decentralized governance mechanism of Bittensor, allowing for the
dynamic selection and participation of validators in the network's consensus process.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `delegate_ss58`: `Optional[str]`
- `take`: `float`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`send_extrinsic`**

**Docstring:**
```
Sends an extrinsic to the Bittensor blockchain using the provided wallet and parameters. This method
constructs and submits the extrinsic, handling retries and blockchain communication.

Args:
    wallet (bittensor.wallet): The wallet associated with the extrinsic.
    module (str): The module name for the extrinsic.
    function (str): The function name for the extrinsic.
    params (dict): The parameters for the extrinsic.
    period (int, optional): The number of blocks for the extrinsic to live in the mempool. Defaults to 5.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    max_retries (int, optional): The maximum number of retries for the extrinsic. Defaults to 3.
    wait_time (int, optional): The wait time between retries. Defaults to 3.
    max_wait (int, optional): The maximum wait time for the extrinsic. Defaults to 20.

Returns:
    Optional[ExtrinsicReceipt]: The receipt of the extrinsic if successful, None otherwise.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `module`: `str`
- `function`: `str`
- `params`: `dict`
- `period`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `max_retries`: `int`
- `wait_time`: `int`
- `max_wait`: `int`

**Returns:** `Optional[ExtrinsicReceipt]`

---

## **`set_weights`**

**Docstring:**
```
Sets the inter-neuronal weights for the specified neuron. This process involves specifying the
influence or trust a neuron places on other neurons in the network, which is a fundamental aspect
of Bittensor's decentralized learning architecture.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron setting the weights.
    netuid (int): The unique identifier of the subnet.
    uids (Union[NDArray[np.int64], torch.LongTensor, list]): The list of neuron UIDs that the weights are being
        set for.
    weights (Union[NDArray[np.float32], torch.FloatTensor, list]): The corresponding weights to be set for each
        UID.
    version_key (int, optional): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
    max_retries (int, optional): The number of maximum attempts to set weights. (Default: 5)

Returns:
    Tuple[bool, str]: ``True`` if the setting of weights is successful, False otherwise. And `msg`, a string
    value describing the success or potential error.

This function is crucial in shaping the network's collective intelligence, where each neuron's
learning and contribution are influenced by the weights it sets towards others【81†source】.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `uids`: `Union[NDArray[np.int64], 'torch.LongTensor', list]`
- `weights`: `Union[NDArray[np.float32], 'torch.FloatTensor', list]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_retries`: `int`

**Returns:** `Tuple[bool, str]`

---

## **`_do_set_weights`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `netuid`: `int`
- `uids`: `int`
- `vals`: `List[int]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`commit_weights`**

**Docstring:**
```
Commits a hash of the neuron's weights to the Bittensor blockchain using the provided wallet.
This action serves as a commitment or snapshot of the neuron's current weight distribution.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron committing the weights.
    netuid (int): The unique identifier of the subnet.
    salt (List[int]): list of randomly generated integers as salt to generated weighted hash.
    uids (np.ndarray): NumPy array of neuron UIDs for which weights are being committed.
    weights (np.ndarray): NumPy array of weight values corresponding to each UID.
    version_key (int, optional): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
    max_retries (int, optional): The number of maximum attempts to commit weights. (Default: 5)

Returns:
    Tuple[bool, str]: ``True`` if the weight commitment is successful, False otherwise. And `msg`, a string
    value describing the success or potential error.

This function allows neurons to create a tamper-proof record of their weight distribution at a specific point in time,
enhancing transparency and accountability within the Bittensor network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `salt`: `List[int]`
- `uids`: `Union[NDArray[np.int64], list]`
- `weights`: `Union[NDArray[np.int64], list]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_retries`: `int`

**Returns:** `Tuple[bool, str]`

---

## **`_do_commit_weights`**

**Docstring:**
```
Internal method to send a transaction to the Bittensor blockchain, committing the hash of a neuron's weights.
This method constructs and submits the transaction, handling retries and blockchain communication.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron committing the weights.
    netuid (int): The unique identifier of the subnet.
    commit_hash (str): The hash of the neuron's weights to be committed.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.

Returns:
    Tuple[bool, Optional[str]]: A tuple containing a success flag and an optional error message.

This method ensures that the weight commitment is securely recorded on the Bittensor blockchain, providing a
verifiable record of the neuron's weight distribution at a specific point in time.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `commit_hash`: `str`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`reveal_weights`**

**Docstring:**
```
Reveals the weights for a specific subnet on the Bittensor blockchain using the provided wallet.
This action serves as a revelation of the neuron's previously committed weight distribution.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron revealing the weights.
    netuid (int): The unique identifier of the subnet.
    uids (np.ndarray): NumPy array of neuron UIDs for which weights are being revealed.
    weights (np.ndarray): NumPy array of weight values corresponding to each UID.
    salt (np.ndarray): NumPy array of salt values corresponding to the hash function.
    version_key (int, optional): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
    max_retries (int, optional): The number of maximum attempts to reveal weights. (Default: 5)

Returns:
    Tuple[bool, str]: ``True`` if the weight revelation is successful, False otherwise. And `msg`, a string
    value describing the success or potential error.

This function allows neurons to reveal their previously committed weight distribution, ensuring transparency
and accountability within the Bittensor network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `uids`: `Union[NDArray[np.int64], list]`
- `weights`: `Union[NDArray[np.int64], list]`
- `salt`: `Union[NDArray[np.int64], list]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_retries`: `int`

**Returns:** `Tuple[bool, str]`

---

## **`_do_reveal_weights`**

**Docstring:**
```
Internal method to send a transaction to the Bittensor blockchain, revealing the weights for a specific subnet.
This method constructs and submits the transaction, handling retries and blockchain communication.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron revealing the weights.
    netuid (int): The unique identifier of the subnet.
    uids (List[int]): List of neuron UIDs for which weights are being revealed.
    values (List[int]): List of weight values corresponding to each UID.
    salt (List[int]): List of salt values corresponding to the hash function.
    version_key (int): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.

Returns:
    Tuple[bool, Optional[str]]: A tuple containing a success flag and an optional error message.

This method ensures that the weight revelation is securely recorded on the Bittensor blockchain, providing transparency
and accountability for the neuron's weight distribution.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `uids`: `List[int]`
- `values`: `List[int]`
- `salt`: `List[int]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`register`**

**Docstring:**
```
Registers a neuron on the Bittensor network using the provided wallet. Registration
is a critical step for a neuron to become an active participant in the network, enabling
it to stake, set weights, and receive incentives.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron to be registered.
    netuid (int): The unique identifier of the subnet.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
        Defaults to `False`.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
         Defaults to `True`.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
    max_allowed_attempts (int): Maximum number of attempts to register the wallet.
    output_in_place (bool): If true, prints the progress of the proof of work to the console in-place. Meaning
        the progress is printed on the same lines. Defaults to `True`.
    cuda (bool): If ``true``, the wallet should be registered using CUDA device(s). Defaults to `False`.
    dev_id (Union[List[int], int]): The CUDA device id to use, or a list of device ids. Defaults to `0` (zero).
    tpb (int): The number of threads per block (CUDA). Default to `256`.
    num_processes (Optional[int]): The number of processes to use to register. Default to `None`.
    update_interval (Optional[int]): The number of nonces to solve between updates.  Default to `None`.
    log_verbose (bool): If ``true``, the registration process will log more information.  Default to `False`.

Returns:
    bool: ``True`` if the registration is successful, False otherwise.

This function facilitates the entry of new neurons into the network, supporting the decentralized
growth and scalability of the Bittensor ecosystem.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_allowed_attempts`: `int`
- `output_in_place`: `bool`
- `cuda`: `bool`
- `dev_id`: `Union[List[int], int]`
- `tpb`: `int`
- `num_processes`: `Optional[int]`
- `update_interval`: `Optional[int]`
- `log_verbose`: `bool`

**Returns:** `bool`

---

## **`swap_hotkey`**

**Docstring:**
```
Swaps an old hotkey with a new hotkey for the specified wallet.

This method initiates an extrinsic to change the hotkey associated with a wallet to a new hotkey. It provides
options to wait for inclusion and finalization of the transaction, and to prompt the user for confirmation.

Args:
    wallet (bittensor.wallet): The wallet whose hotkey is to be swapped.
    new_wallet (bittensor.wallet): The new wallet with the hotkey to be set.
    wait_for_inclusion (bool): Whether to wait for the transaction to be included in a block.
        Default is `False`.
    wait_for_finalization (bool): Whether to wait for the transaction to be finalized. Default is `True`.
    prompt (bool): Whether to prompt the user for confirmation before proceeding. Default is `False`.

Returns:
    bool: True if the hotkey swap was successful, False otherwise.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `new_wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`run_faucet`**

**Docstring:**
```
Facilitates a faucet transaction, allowing new neurons to receive an initial amount of TAO
for participating in the network. This function is particularly useful for newcomers to the
Bittensor network, enabling them to start with a small stake on testnet only.

Args:
    wallet (bittensor.wallet): The wallet for which the faucet transaction is to be run.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
        Defaults to `False`.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
         Defaults to `True`.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
    max_allowed_attempts (int): Maximum number of attempts to register the wallet.
    output_in_place (bool): If true, prints the progress of the proof of work to the console in-place. Meaning
        the progress is printed on the same lines. Defaults to `True`.
    cuda (bool): If ``true``, the wallet should be registered using CUDA device(s). Defaults to `False`.
    dev_id (Union[List[int], int]): The CUDA device id to use, or a list of device ids. Defaults to `0` (zero).
    tpb (int): The number of threads per block (CUDA). Default to `256`.
    num_processes (Optional[int]): The number of processes to use to register. Default to `None`.
    update_interval (Optional[int]): The number of nonces to solve between updates.  Default to `None`.
    log_verbose (bool): If ``true``, the registration process will log more information.  Default to `False`.

Returns:
    bool: ``True`` if the faucet transaction is successful, False otherwise.

This function is part of Bittensor's onboarding process, ensuring that new neurons have
the necessary resources to begin their journey in the decentralized AI network.

Note:
    This is for testnet ONLY and is disabled currently. You must build your own staging subtensor chain with the
    ``--features pow-faucet`` argument to enable this.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_allowed_attempts`: `int`
- `output_in_place`: `bool`
- `cuda`: `bool`
- `dev_id`: `Union[List[int], int]`
- `tpb`: `int`
- `num_processes`: `Optional[int]`
- `update_interval`: `Optional[int]`
- `log_verbose`: `bool`

**Returns:** `bool`

---

## **`burned_register`**

**Docstring:**
```
Registers a neuron on the Bittensor network by recycling TAO. This method of registration
involves recycling TAO tokens, allowing them to be re-mined by performing work on the network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron to be registered.
    netuid (int): The unique identifier of the subnet.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
        Defaults to `False`.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
        Defaults to `True`.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding. Defaults to `False`.

Returns:
    bool: ``True`` if the registration is successful, False otherwise.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`_do_pow_register`**

**Parameters:**
- `self`
- `netuid`: `int`
- `wallet`: `'wallet'`
- `pow_result`: `'POWSolution'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`_do_burned_register`**

**Parameters:**
- `self`
- `netuid`: `int`
- `wallet`: `'wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`_do_swap_hotkey`**

**Docstring:**
```
Performs a hotkey swap extrinsic call to the Subtensor chain.

Args:
    wallet (bittensor.wallet): The wallet whose hotkey is to be swapped.
    new_wallet (bittensor.wallet): The wallet with the new hotkey to be set.
    wait_for_inclusion (bool): Whether to wait for the transaction to be included in a block. Default is
    `False`.
    wait_for_finalization (bool): Whether to wait for the transaction to be finalized. Default is `True`.

Returns:
    Tuple[bool, Optional[str]]: A tuple containing a boolean indicating success or failure, and an optional
        error message.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `new_wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`transfer`**

**Docstring:**
```
Executes a transfer of funds from the provided wallet to the specified destination address.
This function is used to move TAO tokens within the Bittensor network, facilitating transactions
between neurons.

Args:
    wallet (bittensor.wallet): The wallet from which funds are being transferred.
    dest (str): The destination public key address.
    amount (Union[Balance, float]): The amount of TAO to be transferred.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    transfer_extrinsic (bool): ``True`` if the transfer is successful, False otherwise.

This function is essential for the fluid movement of tokens in the network, supporting
various economic activities such as staking, delegation, and reward distribution.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `dest`: `str`
- `amount`: `Union[Balance, float]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`get_transfer_fee`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `dest`: `str`
- `value`: `Union['Balance', float, int]`

**Returns:** `'Balance'`

---

## **`_do_transfer`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `dest`: `str`
- `transfer_balance`: `'Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str], Optional[str]]`

---

## **`get_existential_deposit`**

**Docstring:**
```
Retrieves the existential deposit amount for the Bittensor blockchain. The existential deposit
is the minimum amount of TAO required for an account to exist on the blockchain. Accounts with
balances below this threshold can be reaped to conserve network resources.

Args:
    block (Optional[int]): Block number at which to query the deposit amount. If ``None``, the current block is
        used.

Returns:
    Optional[Balance]: The existential deposit amount, or ``None`` if the query fails.

The existential deposit is a fundamental economic parameter in the Bittensor network, ensuring
efficient use of storage and preventing the proliferation of dust accounts.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional['Balance']`

---

## **`register_subnetwork`**

**Docstring:**
```
Registers a new subnetwork on the Bittensor network using the provided wallet. This function
is used for the creation and registration of subnetworks, which are specialized segments of the
overall Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet to be used for registration.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the subnetwork registration is successful, False otherwise.

This function allows for the expansion and diversification of the Bittensor network, supporting
its decentralized and adaptable architecture.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`set_hyperparameter`**

**Docstring:**
```
Sets a specific hyperparameter for a given subnetwork on the Bittensor blockchain. This action
involves adjusting network-level parameters, influencing the behavior and characteristics of the
subnetwork.

Args:
    wallet (bittensor.wallet): The wallet used for setting the hyperparameter.
    netuid (int): The unique identifier of the subnetwork.
    parameter (str): The name of the hyperparameter to be set.
    value: The new value for the hyperparameter.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the hyperparameter setting is successful, False otherwise.

This function plays a critical role in the dynamic governance and adaptability of the Bittensor
network, allowing for fine-tuning of network operations and characteristics.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `parameter`: `str`
- `value`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`serve_axon`**

**Docstring:**
```
Registers an Axon serving endpoint on the Bittensor network for a specific neuron. This function
is used to set up the Axon, a key component of a neuron that handles incoming queries and data
processing tasks.

Args:
    netuid (int): The unique identifier of the subnetwork.
    axon (bittensor.Axon): The Axon instance to be registered for serving.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.

Returns:
    bool: ``True`` if the Axon serve registration is successful, False otherwise.

By registering an Axon, the neuron becomes an active part of the network's distributed
computing infrastructure, contributing to the collective intelligence of Bittensor.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `axon`: `'bittensor.axon'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`_do_serve_axon`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `call_params`: `'AxonServeCallParams'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`serve_prometheus`**

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `port`: `int`
- `netuid`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`_do_serve_prometheus`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `call_params`: `'PrometheusServeCallParams'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`_do_associate_ips`**

**Docstring:**
```
Sends an associate IPs extrinsic to the chain.

Args:
    wallet (:func:`bittensor.wallet`): Wallet object.
    ip_info_list (:func:`List[IPInfo]`): List of IPInfo objects.
    netuid (int): Netuid to associate IPs to.
    wait_for_inclusion (bool): If ``true``, waits for inclusion.
    wait_for_finalization (bool): If ``true``, waits for finalization.

Returns:
    success (bool): ``True`` if associate IPs was successful.
    error (:func:`Optional[str]`): Error message if associate IPs failed, None otherwise.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `ip_info_list`: `List['IPInfo']`
- `netuid`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`add_stake`**

**Docstring:**
```
Adds the specified amount of stake to a neuron identified by the hotkey ``SS58`` address. Staking
is a fundamental process in the Bittensor network that enables neurons to participate actively
and earn incentives.

Args:
    wallet (bittensor.wallet): The wallet to be used for staking.
    hotkey_ss58 (Optional[str]): The ``SS58`` address of the hotkey associated with the neuron.
    amount (Union[Balance, float]): The amount of TAO to stake.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the staking is successful, False otherwise.

This function enables neurons to increase their stake in the network, enhancing their influence
and potential rewards in line with Bittensor's consensus and reward mechanisms.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `Optional[str]`
- `amount`: `Optional[Union['Balance', float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`add_stake_multiple`**

**Docstring:**
```
Adds stakes to multiple neurons identified by their hotkey SS58 addresses. This bulk operation
allows for efficient staking across different neurons from a single wallet.

Args:
    wallet (bittensor.wallet): The wallet used for staking.
    hotkey_ss58s (List[str]): List of ``SS58`` addresses of hotkeys to stake to.
    amounts (List[Union[Balance, float]], optional): Corresponding amounts of TAO to stake for each hotkey.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the staking is successful for all specified neurons, False otherwise.

This function is essential for managing stakes across multiple neurons, reflecting the dynamic
and collaborative nature of the Bittensor network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58s`: `List[str]`
- `amounts`: `Optional[List[Union['Balance', float]]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`_do_stake`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `hotkey_ss58`: `str`
- `amount`: `'Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`unstake_multiple`**

**Docstring:**
```
Performs batch unstaking from multiple hotkey accounts, allowing a neuron to reduce its staked amounts
efficiently. This function is useful for managing the distribution of stakes across multiple neurons.

Args:
    wallet (bittensor.wallet): The wallet linked to the coldkey from which the stakes are being withdrawn.
    hotkey_ss58s (List[str]): A list of hotkey ``SS58`` addresses to unstake from.
    amounts (List[Union[Balance, float]], optional): The amounts of TAO to unstake from each hotkey. If not
        provided, unstakes all available stakes.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the batch unstaking is successful, False otherwise.

This function allows for strategic reallocation or withdrawal of stakes, aligning with the dynamic
stake management aspect of the Bittensor network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58s`: `List[str]`
- `amounts`: `Optional[List[Union['Balance', float]]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`unstake`**

**Docstring:**
```
Removes a specified amount of stake from a single hotkey account. This function is critical for adjusting
individual neuron stakes within the Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron from which the stake is being removed.
    hotkey_ss58 (Optional[str]): The ``SS58`` address of the hotkey account to unstake from.
    amount (Union[Balance, float], optional): The amount of TAO to unstake. If not specified, unstakes all.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the unstaking process is successful, False otherwise.

This function supports flexible stake management, allowing neurons to adjust their network participation
and potential reward accruals.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `Optional[str]`
- `amount`: `Optional[Union['Balance', float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`_do_unstake`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `hotkey_ss58`: `str`
- `amount`: `'Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`check_in_arbitration`**

**Docstring:**
```
Checks storage function to see if the provided coldkey is in arbitration.
If 0, `swap` has not been called on this key. If 1, swap has been called once, so
the key is not in arbitration. If >1, `swap` has been called with multiple destinations, and
the key is thus in arbitration.
```

**Parameters:**
- `self`
- `ss58_address`: `str`

**Returns:** `int`

---

## **`get_remaining_arbitration_period`**

**Docstring:**
```
Retrieves the remaining arbitration period for a given coldkey.
Args:
    coldkey_ss58 (str): The SS58 address of the coldkey.
    block (Optional[int], optional): The block number to query. If None, uses the latest block.
Returns:
    Optional[int]: The remaining arbitration period in blocks, or 0 if not found.
```

**Parameters:**
- `self`
- `coldkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`register_senate`**

**Docstring:**
```
Removes a specified amount of stake from a single hotkey account. This function is critical for adjusting
individual neuron stakes within the Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron from which the stake is being removed.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the unstaking process is successful, False otherwise.

This function supports flexible stake management, allowing neurons to adjust their network participation
and potential reward accruals.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`leave_senate`**

**Docstring:**
```
Removes a specified amount of stake from a single hotkey account. This function is critical for adjusting
individual neuron stakes within the Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron from which the stake is being removed.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the unstaking process is successful, False otherwise.

This function supports flexible stake management, allowing neurons to adjust their network participation
and potential reward accruals.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`vote_senate`**

**Docstring:**
```
Removes a specified amount of stake from a single hotkey account. This function is critical for adjusting
individual neuron stakes within the Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron from which the stake is being removed.
    proposal_hash (str): The hash of the proposal being voted on.
    proposal_idx (int): The index of the proposal being voted on.
    vote (bool): The vote to be cast (True for yes, False for no).
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the unstaking process is successful, False otherwise.

This function supports flexible stake management, allowing neurons to adjust their network participation
and potential reward accruals.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `proposal_hash`: `str`
- `proposal_idx`: `int`
- `vote`: `bool`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`is_senate_member`**

**Docstring:**
```
Checks if a given neuron (identified by its hotkey SS58 address) is a member of the Bittensor senate.
The senate is a key governance body within the Bittensor network, responsible for overseeing and
approving various network operations and proposals.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int]): The blockchain block number at which to check senate membership.

Returns:
    bool: ``True`` if the neuron is a senate member at the given block, False otherwise.

This function is crucial for understanding the governance dynamics of the Bittensor network and for
identifying the neurons that hold decision-making power within the network.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`get_vote_data`**

**Docstring:**
```
Retrieves the voting data for a specific proposal on the Bittensor blockchain. This data includes
information about how senate members have voted on the proposal.

Args:
    proposal_hash (str): The hash of the proposal for which voting data is requested.
    block (Optional[int]): The blockchain block number to query the voting data.

Returns:
    Optional[ProposalVoteData]: An object containing the proposal's voting data, or ``None`` if not found.

This function is important for tracking and understanding the decision-making processes within
the Bittensor network, particularly how proposals are received and acted upon by the governing body.
```

**Parameters:**
- `self`
- `proposal_hash`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[ProposalVoteData]`

---

## **`get_senate_members`**

**Docstring:**
```
Retrieves the list of current senate members from the Bittensor blockchain. Senate members are
responsible for governance and decision-making within the network.

Args:
    block (Optional[int]): The blockchain block number at which to retrieve the senate members.

Returns:
    Optional[List[str]]: A list of ``SS58`` addresses of current senate members, or ``None`` if not available.

Understanding the composition of the senate is key to grasping the governance structure and
decision-making authority within the Bittensor network.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[List[str]]`

---

## **`get_proposal_call_data`**

**Docstring:**
```
Retrieves the call data of a specific proposal on the Bittensor blockchain. This data provides
detailed information about the proposal, including its purpose and specifications.

Args:
    proposal_hash (str): The hash of the proposal.
    block (Optional[int]): The blockchain block number at which to query the proposal call data.

Returns:
    Optional[GenericCall]: An object containing the proposal's call data, or ``None`` if not found.

This function is crucial for analyzing the types of proposals made within the network and the
specific changes or actions they intend to implement or address.
```

**Parameters:**
- `self`
- `proposal_hash`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional['GenericCall']`

---

## **`get_proposal_hashes`**

**Docstring:**
```
Retrieves the list of proposal hashes currently present on the Bittensor blockchain. Each hash
uniquely identifies a proposal made within the network.

Args:
    block (Optional[int]): The blockchain block number to query the proposal hashes.

Returns:
    Optional[List[str]]: A list of proposal hashes, or ``None`` if not available.

This function enables tracking and reviewing the proposals made in the network, offering insights
into the active governance and decision-making processes.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[List[str]]`

---

## **`get_proposals`**

**Docstring:**
```
Retrieves all active proposals on the Bittensor blockchain, along with their call and voting data.
This comprehensive view allows for a thorough understanding of the proposals and their reception
by the senate.

Args:
    block (Optional[int]): The blockchain block number to query the proposals.

Returns:
    Optional[Dict[str, Tuple[bittensor.ProposalCallData, bittensor.ProposalVoteData]]]: A dictionary mapping
        proposal hashes to their corresponding call and vote data, or ``None`` if not available.

This function is integral for analyzing the governance activity on the Bittensor network,
providing a holistic view of the proposals and their impact or potential changes within the network.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[Dict[str, Tuple['GenericCall', 'ProposalVoteData']]]`

---

## **`root_register`**

**Docstring:**
```
Registers the neuron associated with the wallet on the root network. This process is integral for
participating in the highest layer of decision-making and governance within the Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron to be registered on the root network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the registration on the root network is successful, False otherwise.

This function enables neurons to engage in the most critical and influential aspects of the network's
governance, signifying a high level of commitment and responsibility in the Bittensor ecosystem.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`_do_root_register`**

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`root_set_weights`**

**Docstring:**
```
Sets the weights for neurons on the root network. This action is crucial for defining the influence
and interactions of neurons at the root level of the Bittensor network.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron setting the weights.
    netuids (Union[NDArray[np.int64], torch.LongTensor, list]): The list of neuron UIDs for which weights are
        being set.
    weights (Union[NDArray[np.float32], torch.FloatTensor, list]): The corresponding weights to be set for each
        UID.
    version_key (int, optional): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.

Returns:
    bool: ``True`` if the setting of root-level weights is successful, False otherwise.

This function plays a pivotal role in shaping the root network's collective intelligence and decision-making
processes, reflecting the principles of decentralized governance and collaborative learning in Bittensor.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuids`: `Union[NDArray[np.int64], 'torch.LongTensor', list]`
- `weights`: `Union[NDArray[np.float32], 'torch.FloatTensor', list]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`_do_set_root_weights`**

**Docstring:**
```
Internal method to send a transaction to the Bittensor blockchain, setting weights
for specified neurons on root. This method constructs and submits the transaction, handling
retries and blockchain communication.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron setting the weights.
    uids (List[int]): List of neuron UIDs for which weights are being set.
    vals (List[int]): List of weight values corresponding to each UID.
    netuid (int): Unique identifier for the network.
    version_key (int, optional): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.

Returns:
    Tuple[bool, Optional[str]]: A tuple containing a success flag and an optional error message.

This method is vital for the dynamic weighting mechanism in Bittensor, where neurons adjust their
trust in other neurons based on observed performance and contributions on the root network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `uids`: `List[int]`
- `vals`: `List[int]`
- `netuid`: `int`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`query_identity`**

**Docstring:**
```
Queries the identity of a neuron on the Bittensor blockchain using the given key. This function retrieves
detailed identity information about a specific neuron, which is a crucial aspect of the network's decentralized
identity and governance system.

NOTE:
    See the `Bittensor CLI documentation <https://docs.bittensor.com/reference/btcli>`_ for supported identity
    parameters.

Args:
    key (str): The key used to query the neuron's identity, typically the neuron's ``SS58`` address.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    result (dict): An object containing the identity information of the neuron if found, ``None`` otherwise.

The identity information can include various attributes such as the neuron's stake, rank, and other
network-specific details, providing insights into the neuron's role and status within the Bittensor network.
```

**Parameters:**
- `self`
- `key`: `str`
- `block`: `Optional[int]`

**Returns:** `dict`

---

## **`update_identity`**

**Docstring:**
```
Updates the identity of a neuron on the Bittensor blockchain. This function allows neurons to modify their
identity attributes, reflecting changes in their roles, stakes, or other network-specific parameters.

NOTE:
    See the `Bittensor CLI documentation <https://docs.bittensor.com/reference/btcli>`_ for supported identity
    parameters.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron whose identity is being updated.
    identified (str, optional): The identified ``SS58`` address of the neuron. Defaults to the wallet's coldkey
        address.
    params (dict, optional): A dictionary of parameters to update in the neuron's identity.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.

Returns:
    bool: ``True`` if the identity update is successful, False otherwise.

This function plays a vital role in maintaining the accuracy and currency of neuron identities in the
Bittensor network, ensuring that the network's governance and consensus mechanisms operate effectively.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `identified`: `Optional[str]`
- `params`: `Optional[dict]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`commit`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `netuid`: `int`
- `data`: `str`

**Returns:** `None`

---

## **`get_commitment`**

**Parameters:**
- `self`
- `netuid`: `int`
- `uid`: `int`
- `block`: `Optional[int]`

**Returns:** `str`

---

## **`query_subtensor`**

**Parameters:**
- `self`
- `name`: `str`
- `block`: `Optional[int]`
- `params`: `Optional[List[object]]`

**Returns:** `MockSubtensorValue`

---

## **`query_map_subtensor`**

**Docstring:**
```
Note: Double map requires one param
```

**Parameters:**
- `self`
- `name`: `str`
- `block`: `Optional[int]`
- `params`: `Optional[List[object]]`

**Returns:** `Optional[MockMapResult]`

---

## **`query_constant`**

**Parameters:**
- `self`
- `module_name`: `str`
- `constant_name`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[object]`

---

## **`query_module`**

**Docstring:**
```
Queries any module storage on the Bittensor blockchain with the specified parameters and block number.
This function is a generic query interface that allows for flexible and diverse data retrieval from
various blockchain modules.

Args:
    module (str): The name of the module from which to query data.
    name (str): The name of the storage function within the module.
    block (Optional[int]): The blockchain block number at which to perform the query.
    params (Optional[List[object]], optional): A list of parameters to pass to the query function.

Returns:
    Optional[ScaleType]: An object containing the requested data if found, ``None`` otherwise.

This versatile query function is key to accessing a wide range of data and insights from different
parts of the Bittensor blockchain, enhancing the understanding and analysis of the network's state and dynamics.
```

**Parameters:**
- `self`
- `module`: `str`
- `name`: `str`
- `block`: `Optional[int]`
- `params`: `Optional[list]`

**Returns:** `'ScaleType'`

---

## **`query_map`**

**Docstring:**
```
Queries map storage from any module on the Bittensor blockchain. This function retrieves data structures
that represent key-value mappings, essential for accessing complex and structured data within the blockchain
modules.

Args:
    module (str): The name of the module from which to query the map storage.
    name (str): The specific storage function within the module to query.
    block (Optional[int]): The blockchain block number at which to perform the query.
    params (Optional[List[object]], optional): Parameters to be passed to the query.

Returns:
    result (QueryMapResult): A data structure representing the map storage if found, ``None`` otherwise.

This function is particularly useful for retrieving detailed and structured data from various blockchain
modules, offering insights into the network's state and the relationships between its different components.
```

**Parameters:**
- `self`
- `module`: `str`
- `name`: `str`
- `block`: `Optional[int]`
- `params`: `Optional[list]`

**Returns:** `QueryMapResult`

---

## **`state_call`**

**Docstring:**
```
Makes a state call to the Bittensor blockchain, allowing for direct queries of the blockchain's state.
This function is typically used for advanced queries that require specific method calls and data inputs.

Args:
    method (str): The method name for the state call.
    data (str): The data to be passed to the method.
    block (Optional[int]): The blockchain block number at which to perform the state call.

Returns:
    result (Dict[Any, Any]): The result of the rpc call.

The state call function provides a more direct and flexible way of querying blockchain data,
useful for specific use cases where standard queries are insufficient.
```

**Parameters:**
- `self`
- `method`: `str`
- `data`: `str`
- `block`: `Optional[int]`

**Returns:** `Dict[Any, Any]`

---

## **`query_runtime_api`**

**Docstring:**
```
Queries the runtime API of the Bittensor blockchain, providing a way to interact with the underlying
runtime and retrieve data encoded in Scale Bytes format. This function is essential for advanced users
who need to interact with specific runtime methods and decode complex data types.

Args:
    runtime_api (str): The name of the runtime API to query.
    method (str): The specific method within the runtime API to call.
    params (Optional[List[ParamWithTypes]], optional): The parameters to pass to the method call.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    Optional[bytes]: The Scale Bytes encoded result from the runtime API call, or ``None`` if the call fails.

This function enables access to the deeper layers of the Bittensor blockchain, allowing for detailed
and specific interactions with the network's runtime environment.
```

**Parameters:**
- `self`
- `runtime_api`: `str`
- `method`: `str`
- `params`: `Optional[Union[List[int], Dict[str, int]]]`
- `block`: `Optional[int]`

**Returns:** `Optional[str]`

---

## **`_encode_params`**

**Docstring:**
```
Returns a hex encoded string of the params using their types.
```

**Parameters:**
- `self`
- `call_definition`: `List['ParamWithTypes']`
- `params`: `Union[List[Any], Dict[str, Any]]`

**Returns:** `str`

---

## **`_get_hyperparameter`**

**Docstring:**
```
Retrieves a specified hyperparameter for a specific subnet.

Args:
    param_name (str): The name of the hyperparameter to retrieve.
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[Union[int, float]]: The value of the specified hyperparameter if the subnet exists, ``None``
        otherwise.
```

**Parameters:**
- `self`
- `param_name`: `str`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[Any]`

---

## **`rho`**

**Docstring:**
```
Retrieves the 'Rho' hyperparameter for a specified subnet within the Bittensor network. 'Rho' represents the
global inflation rate, which directly influences the network's token emission rate and economic model.

Note:
    This is currently fixed such that the Bittensor blockchain emmits 7200 Tao per day.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number at which to query the parameter.

Returns:
    Optional[int]: The value of the 'Rho' hyperparameter if the subnet exists, ``None`` otherwise.

Mathematical Context:
    Rho (p) is calculated based on the network's target inflation and actual neuron staking.
    It adjusts the emission rate of the TAO token to balance the network's economy and dynamics.
    The formula for Rho is defined as: p = (Staking_Target / Staking_Actual) * Inflation_Target.
    Here, Staking_Target and Staking_Actual represent the desired and actual total stakes in the network,
    while Inflation_Target is the predefined inflation rate goal.

'Rho' is essential for understanding the network's economic dynamics, affecting the reward distribution
and incentive structures across the network's neurons.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`kappa`**

**Docstring:**
```
Retrieves the 'Kappa' hyperparameter for a specified subnet. 'Kappa' is a critical parameter in
the Bittensor network that controls the distribution of stake weights among neurons, impacting their
rankings and incentive allocations.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[float]: The value of the 'Kappa' hyperparameter if the subnet exists, None otherwise.

Mathematical Context:
    Kappa (κ) is used in the calculation of neuron ranks, which determine their share of network incentives.
    It is derived from the softmax function applied to the inter-neuronal weights set by each neuron.
    The formula for Kappa is: κ_i = exp(w_i) / Σ(exp(w_j)), where w_i represents the weight set by neuron i,
    and the denominator is the sum of exponential weights set by all neurons.
    This mechanism ensures a normalized and probabilistic distribution of ranks based on relative weights.

Understanding 'Kappa' is crucial for analyzing stake dynamics and the consensus mechanism within the network,
as it plays a significant role in neuron ranking and incentive allocation processes.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`difficulty`**

**Docstring:**
```
Retrieves the 'Difficulty' hyperparameter for a specified subnet in the Bittensor network.
This parameter is instrumental in determining the computational challenge required for neurons
to participate in consensus and validation processes.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[int]: The value of the 'Difficulty' hyperparameter if the subnet exists, ``None`` otherwise.

The 'Difficulty' parameter directly impacts the network's security and integrity by setting the
computational effort required for validating transactions and participating in the network's consensus
mechanism.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`recycle`**

**Docstring:**
```
Retrieves the 'Burn' hyperparameter for a specified subnet. The 'Burn' parameter represents the
amount of Tao that is effectively recycled within the Bittensor network.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[Balance]: The value of the 'Burn' hyperparameter if the subnet exists, None otherwise.

Understanding the 'Burn' rate is essential for analyzing the network registration usage, particularly
how it is correlated with user activity and the overall cost of participation in a given subnet.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional['Balance']`

---

## **`immunity_period`**

**Docstring:**
```
Retrieves the 'ImmunityPeriod' hyperparameter for a specific subnet. This parameter defines the
duration during which new neurons are protected from certain network penalties or restrictions.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[int]: The value of the 'ImmunityPeriod' hyperparameter if the subnet exists, ``None`` otherwise.

The 'ImmunityPeriod' is a critical aspect of the network's governance system, ensuring that new
participants have a grace period to establish themselves and contribute to the network without facing
immediate punitive actions.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`validator_batch_size`**

**Docstring:**
```
Returns network ValidatorBatchSize hyper parameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int]): The block number to retrieve the parameter from. If None, the latest block
        is used. Default is ``None``.

Returns:
    Optional[int]: The value of the ValidatorBatchSize hyperparameter, or None if the subnetwork does not exist
        or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`validator_prune_len`**

**Docstring:**
```
Returns network ValidatorPruneLen hyper parameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int]): The block number to retrieve the parameter from. If None, the latest block
    is used. Default is ``None``.

Returns:
    Optional[int]: The value of the ValidatorPruneLen hyperparameter, or None if the subnetwork does not exist
    or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`validator_logits_divergence`**

**Docstring:**
```
Returns network ValidatorLogitsDivergence hyper parameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int]): The block number to retrieve the parameter from. If None, the latest block
    is used. Default is ``None``.

Returns:
    Optional[float]: The value of the ValidatorLogitsDivergence hyperparameter, or None if the subnetwork does
    not exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`validator_sequence_length`**

**Docstring:**
```
Returns network ValidatorSequenceLength hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the ValidatorSequenceLength hyperparameter, or ``None`` if the subnetwork does
        not exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`validator_epochs_per_reset`**

**Docstring:**
```
Returns network ValidatorEpochsPerReset hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the ValidatorEpochsPerReset hyperparameter, or ``None`` if the subnetwork does
        not exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`validator_epoch_length`**

**Docstring:**
```
Returns network ValidatorEpochLen hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the ValidatorEpochLen hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`validator_exclude_quantile`**

**Docstring:**
```
Returns network ValidatorExcludeQuantile hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest block is used. Default is ``None``.

Returns:
    Optional[float]: The value of the ValidatorExcludeQuantile hyperparameter, or ``None`` if the subnetwork does not exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`max_allowed_validators`**

**Docstring:**
```
Returns network ValidatorExcludeQuantile hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[float]: The value of the ValidatorExcludeQuantile hyperparameter, or ``None`` if the subnetwork
        does not exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`min_allowed_weights`**

**Docstring:**
```
Returns network MinAllowedWeights hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the MinAllowedWeights hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`max_weight_limit`**

**Docstring:**
```
Returns network MaxWeightsLimit hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[float]: The value of the MaxWeightsLimit hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`adjustment_alpha`**

**Docstring:**
```
Returns network AdjustmentAlpha hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[float]: The value of the AdjustmentAlpha hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`bonds_moving_avg`**

**Docstring:**
```
Returns network BondsMovingAverage hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[float]: The value of the BondsMovingAverage hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`scaling_law_power`**

**Docstring:**
```
Returns network ScalingLawPower hyper parameter
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`synergy_scaling_law_power`**

**Docstring:**
```
Returns network ScalingLawPower hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[float]: The value of the ScalingLawPower hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`subnetwork_n`**

**Docstring:**
```
Returns network SubnetworkN hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the SubnetworkN hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`max_n`**

**Docstring:**
```
Returns network MaxAllowedUids hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the MaxAllowedUids hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`blocks_since_epoch`**

**Docstring:**
```
Returns network BlocksSinceEpoch hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the BlocksSinceEpoch hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`blocks_since_last_update`**

**Docstring:**
```
Returns the number of blocks since the last update for a specific UID in the subnetwork.

Args:
    netuid (int): The unique identifier of the subnetwork.
    uid (int): The unique identifier of the neuron.

Returns:
    Optional[int]: The number of blocks since the last update, or ``None`` if the subnetwork or UID does not
        exist.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `uid`: `int`

**Returns:** `Optional[int]`

---

## **`weights_rate_limit`**

**Docstring:**
```
Returns network WeightsSetRateLimit hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.

Returns:
    Optional[int]: The value of the WeightsSetRateLimit hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`

**Returns:** `Optional[int]`

---

## **`tempo`**

**Docstring:**
```
Returns network Tempo hyperparameter.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the Tempo hyperparameter, or ``None`` if the subnetwork does not
        exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`get_total_stake_for_hotkey`**

**Docstring:**
```
Returns the total stake held on a hotkey including delegative.

Args:
    ss58_address (str): The SS58 address of the hotkey.
    block (Optional[int], optional): The block number to retrieve the stake from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[Balance]: The total stake held on the hotkey, or ``None`` if the hotkey does not
        exist or the stake is not found.
```

**Parameters:**
- `self`
- `ss58_address`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional['Balance']`

---

## **`get_total_stake_for_coldkey`**

**Docstring:**
```
Returns the total stake held on a coldkey.

Args:
    ss58_address (str): The SS58 address of the coldkey.
    block (Optional[int], optional): The block number to retrieve the stake from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[Balance]: The total stake held on the coldkey, or ``None`` if the coldkey does not
        exist or the stake is not found.
```

**Parameters:**
- `self`
- `ss58_address`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional['Balance']`

---

## **`get_stake_for_coldkey_and_hotkey`**

**Docstring:**
```
Returns the stake under a coldkey - hotkey pairing.

Args:
    hotkey_ss58 (str): The SS58 address of the hotkey.
    coldkey_ss58 (str): The SS58 address of the coldkey.
    block (Optional[int], optional): The block number to retrieve the stake from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[Balance]: The stake under the coldkey - hotkey pairing, or ``None`` if the pairing does not
        exist or the stake is not found.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `coldkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional['Balance']`

---

## **`get_stake`**

**Docstring:**
```
Returns a list of stake tuples (coldkey, balance) for each delegating coldkey including the owner.

Args:
    hotkey_ss58 (str): The SS58 address of the hotkey.
    block (Optional[int], optional): The block number to retrieve the stakes from. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    List[Tuple[str, Balance]]: A list of tuples, each containing a coldkey SS58 address and the corresponding
        balance staked by that coldkey.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `List[Tuple[str, 'Balance']]`

---

## **`does_hotkey_exist`**

**Docstring:**
```
Returns true if the hotkey is known by the chain and there are accounts.

Args:
    hotkey_ss58 (str): The SS58 address of the hotkey.
    block (Optional[int], optional): The block number to check the hotkey against. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    bool: ``True`` if the hotkey is known by the chain and there are accounts, ``False`` otherwise.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`get_hotkey_owner`**

**Docstring:**
```
Returns the coldkey owner of the passed hotkey.

Args:
    hotkey_ss58 (str): The SS58 address of the hotkey.
    block (Optional[int], optional): The block number to check the hotkey owner against. If ``None``, the latest
        block is used. Default is ``None``.

Returns:
    Optional[str]: The SS58 address of the coldkey owner, or ``None`` if the hotkey does not exist or the owner
        is not found.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[str]`

---

## **`get_axon_info`**

**Docstring:**
```
Returns the axon information for this hotkey account.

Args:
    netuid (int): The unique identifier of the subnetwork.
    hotkey_ss58 (str): The SS58 address of the hotkey.
    block (Optional[int], optional): The block number to retrieve the axon information from. If ``None``, the
        latest block is used. Default is ``None``.

Returns:
    Optional[AxonInfo]: An AxonInfo object containing the axon information, or ``None`` if the axon information
        is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[AxonInfo]`

---

## **`get_prometheus_info`**

**Docstring:**
```
Returns the prometheus information for this hotkey account.

Args:
    netuid (int): The unique identifier of the subnetwork.
    hotkey_ss58 (str): The SS58 address of the hotkey.
    block (Optional[int], optional): The block number to retrieve the prometheus information from. If ``None``,
        the latest block is used. Default is ``None``.

Returns:
    Optional[PrometheusInfo]: A PrometheusInfo object containing the prometheus information, or ``None`` if the
        prometheus information is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[PrometheusInfo]`

---

## **`block`**

**Docstring:**
```
Returns current chain block.
Returns:
    block (int):
        Current chain block.
```

**Parameters:**
- `self`

**Returns:** `int`

---

## **`total_issuance`**

**Docstring:**
```
Retrieves the total issuance of the Bittensor network's native token (Tao) as of a specific
blockchain block. This represents the total amount of currency that has been issued or mined on the network.

Args:
    block (Optional[int], optional): The blockchain block number at which to perform the query.

Returns:
    Balance: The total issuance of TAO, represented as a Balance object.

The total issuance is a key economic indicator in the Bittensor network, reflecting the overall supply
of the currency and providing insights into the network's economic health and inflationary trends.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[Balance]`

---

## **`total_stake`**

**Docstring:**
```
Retrieves the total amount of TAO staked on the Bittensor network as of a specific blockchain block.
This represents the cumulative stake across all neurons in the network, indicating the overall level
of participation and investment by the network's participants.

Args:
    block (Optional[int], optional): The blockchain block number at which to perform the query.

Returns:
    Balance: The total amount of TAO staked on the network, represented as a Balance object.

The total stake is an important metric for understanding the network's security, governance dynamics,
and the level of commitment by its participants. It is also a critical factor in the network's
consensus and incentive mechanisms.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[Balance]`

---

## **`serving_rate_limit`**

**Docstring:**
```
Retrieves the serving rate limit for a specific subnet within the Bittensor network.
This rate limit determines how often you can change your node's IP address on the blockchain. Expressed in
number of blocks. Applies to both subnet validator and subnet miner nodes. Used when you move your node to a new
machine.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int], optional): The blockchain block number at which to perform the query.

Returns:
    Optional[int]: The serving rate limit of the subnet if it exists, ``None`` otherwise.

The serving rate limit is a crucial parameter for maintaining network efficiency and preventing
overuse of resources by individual neurons. It helps ensure a balanced distribution of service
requests across the network.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`tx_rate_limit`**

**Docstring:**
```
Retrieves the transaction rate limit for the Bittensor network as of a specific blockchain block.
This rate limit sets the maximum number of transactions that can be processed within a given time frame.

Args:
    block (Optional[int], optional): The blockchain block number at which to perform the query.

Returns:
    Optional[int]: The transaction rate limit of the network, None if not available.

The transaction rate limit is an essential parameter for ensuring the stability and scalability
of the Bittensor network. It helps in managing network load and preventing congestion, thereby
maintaining efficient and timely transaction processing.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`subnet_exists`**

**Docstring:**
```
Checks if a subnet with the specified unique identifier (netuid) exists within the Bittensor network.

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int], optional): The blockchain block number at which to check the subnet's existence.

Returns:
    bool: ``True`` if the subnet exists, False otherwise.

This function is critical for verifying the presence of specific subnets in the network,
enabling a deeper understanding of the network's structure and composition.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`get_all_subnet_netuids`**

**Docstring:**
```
Retrieves the list of all subnet unique identifiers (netuids) currently present in the Bittensor network.

Args:
    block (Optional[int], optional): The blockchain block number at which to retrieve the subnet netuids.

Returns:
    List[int]: A list of subnet netuids.

This function provides a comprehensive view of the subnets within the Bittensor network,
offering insights into its diversity and scale.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `List[int]`

---

## **`get_total_subnets`**

**Docstring:**
```
Retrieves the total number of subnets within the Bittensor network as of a specific blockchain block.

Args:
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    int: The total number of subnets in the network.

Understanding the total number of subnets is essential for assessing the network's growth and
the extent of its decentralized infrastructure.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`get_subnet_modality`**

**Docstring:**
```
Returns the NetworkModality hyperparameter for a specific subnetwork.

Args:
    netuid (int): The unique identifier of the subnetwork.
    block (Optional[int], optional): The block number to retrieve the parameter from. If ``None``, the latest block is used. Default is ``None``.

Returns:
    Optional[int]: The value of the NetworkModality hyperparameter, or ``None`` if the subnetwork does not exist or the parameter is not found.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`get_subnet_connection_requirement`**

**Parameters:**
- `self`
- `netuid_0`: `int`
- `netuid_1`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`get_emission_value_by_subnet`**

**Docstring:**
```
Retrieves the emission value of a specific subnet within the Bittensor network. The emission value
represents the rate at which the subnet emits or distributes the network's native token (Tao).

Args:
    netuid (int): The unique identifier of the subnet.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    Optional[float]: The emission value of the subnet, None if not available.

The emission value is a critical economic parameter, influencing the incentive distribution and
reward mechanisms within the subnet.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`get_subnet_connection_requirements`**

**Docstring:**
```
Retrieves the connection requirements for a specific subnet within the Bittensor network. This
function provides details on the criteria that must be met for neurons to connect to the subnet.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    Dict[str, int]: A dictionary detailing the connection requirements for the subnet.

Understanding these requirements is crucial for neurons looking to participate in or interact
with specific subnets, ensuring compliance with their connection standards.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Dict[str, int]`

---

## **`get_subnets`**

**Docstring:**
```
Retrieves a list of all subnets currently active within the Bittensor network. This function
provides an overview of the various subnets and their identifiers.

Args:
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    List[int]: A list of network UIDs representing each active subnet.

This function is valuable for understanding the network's structure and the diversity of subnets
available for neuron participation and collaboration.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `List[int]`

---

## **`get_all_subnets_info`**

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `List[SubnetInfo]`

---

## **`get_subnet_info`**

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[SubnetInfo]`

---

## **`get_subnet_hyperparameters`**

**Docstring:**
```
Retrieves the hyperparameters for a specific subnet within the Bittensor network. These hyperparameters
define the operational settings and rules governing the subnet's behavior.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    Optional[SubnetHyperparameters]: The subnet's hyperparameters, or ``None`` if not available.

Understanding the hyperparameters is crucial for comprehending how subnets are configured and
managed, and how they interact with the network's consensus and incentive mechanisms.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[Union[List, SubnetHyperparameters]]`

---

## **`get_subnet_owner`**

**Docstring:**
```
Retrieves the owner's address of a specific subnet within the Bittensor network. The owner is
typically the entity responsible for the creation and maintenance of the subnet.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    Optional[str]: The SS58 address of the subnet's owner, or ``None`` if not available.

Knowing the subnet owner provides insights into the governance and operational control of the subnet,
which can be important for decision-making and collaboration within the network.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[str]`

---

## **`is_hotkey_delegate`**

**Docstring:**
```
Determines whether a given hotkey (public key) is a delegate on the Bittensor network. This function
checks if the neuron associated with the hotkey is part of the network's delegation system.

Args:
    hotkey_ss58 (str): The SS58 address of the neuron's hotkey.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    bool: ``True`` if the hotkey is a delegate, ``False`` otherwise.

Being a delegate is a significant status within the Bittensor network, indicating a neuron's
involvement in consensus and governance processes.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`get_delegate_take`**

**Docstring:**
```
Retrieves the delegate 'take' percentage for a neuron identified by its hotkey. The 'take'
represents the percentage of rewards that the delegate claims from its nominators' stakes.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    Optional[float]: The delegate take percentage, None if not available.

The delegate take is a critical parameter in the network's incentive structure, influencing
the distribution of rewards among neurons and their nominators.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[float]`

---

## **`get_nominators_for_hotkey`**

**Docstring:**
```
Retrieves a list of nominators and their stakes for a neuron identified by its hotkey.
Nominators are neurons that stake their tokens on a delegate to support its operations.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
   Union[List[Tuple[str, Balance]], int]: A list of tuples containing each nominator's address and staked amount or 0.

This function provides insights into the neuron's support network within the Bittensor ecosystem,
indicating its trust and collaboration relationships.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Union[List[Tuple[str, Balance]], int]`

---

## **`get_delegate_by_hotkey`**

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional['DelegateInfo']`

---

## **`get_delegates_lite`**

**Docstring:**
```
Retrieves a lighter list of all delegate neurons within the Bittensor network. This function provides an
overview of the neurons that are actively involved in the network's delegation system.

Analyzing the delegate population offers insights into the network's governance dynamics and the distribution
of trust and responsibility among participating neurons.

This is a lighter version of :func:`get_delegates`.

Args:
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    List[DelegateInfoLite]: A list of ``DelegateInfoLite`` objects detailing each delegate's characteristics.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `List[DelegateInfoLite]`

---

## **`get_delegates`**

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `List['DelegateInfo']`

---

## **`get_delegated`**

**Docstring:**
```
Returns the list of delegates that a given coldkey is staked to.
```

**Parameters:**
- `self`
- `coldkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `List[Tuple['DelegateInfo', 'Balance']]`

---

## **`get_stake_info_for_coldkey`**

**Docstring:**
```
Retrieves stake information associated with a specific coldkey. This function provides details
about the stakes held by an account, including the staked amounts and associated delegates.

Args:
    coldkey_ss58 (str): The ``SS58`` address of the account's coldkey.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    List[StakeInfo]: A list of StakeInfo objects detailing the stake allocations for the account.

Stake information is vital for account holders to assess their investment and participation
in the network's delegation and consensus processes.
```

**Parameters:**
- `self`
- `coldkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `Optional[List[StakeInfo]]`

---

## **`get_stake_info_for_coldkeys`**

**Docstring:**
```
Retrieves stake information for a list of coldkeys. This function aggregates stake data for multiple
accounts, providing a collective view of their stakes and delegations.

Args:
    coldkey_ss58_list (List[str]): A list of ``SS58`` addresses of the accounts' coldkeys.
    block (Optional[int], optional): The blockchain block number for the query.

Returns:
    Dict[str, List[StakeInfo]]: A dictionary mapping each coldkey to a list of its StakeInfo objects.

This function is useful for analyzing the stake distribution and delegation patterns of multiple
accounts simultaneously, offering a broader perspective on network participation and investment strategies.
```

**Parameters:**
- `self`
- `coldkey_ss58_list`: `List[str]`
- `block`: `Optional[int]`

**Returns:** `Optional[Dict[str, List[StakeInfo]]]`

---

## **`get_minimum_required_stake`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`is_hotkey_registered_any`**

**Docstring:**
```
Checks if a neuron's hotkey is registered on any subnet within the Bittensor network.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int]): The blockchain block number at which to perform the check.

Returns:
    bool: ``True`` if the hotkey is registered on any subnet, False otherwise.

This function is essential for determining the network-wide presence and participation of a neuron.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`is_hotkey_registered_on_subnet`**

**Docstring:**
```
Checks if a neuron's hotkey is registered on a specific subnet within the Bittensor network.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number at which to perform the check.

Returns:
    bool: ``True`` if the hotkey is registered on the specified subnet, False otherwise.

This function helps in assessing the participation of a neuron in a particular subnet,
indicating its specific area of operation or influence within the network.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`is_hotkey_registered`**

**Docstring:**
```
Determines whether a given hotkey (public key) is registered in the Bittensor network, either
globally across any subnet or specifically on a specified subnet. This function checks the registration
status of a neuron identified by its hotkey, which is crucial for validating its participation and
activities within the network.

Args:
    hotkey_ss58 (str): The SS58 address of the neuron's hotkey.
    netuid (Optional[int]): The unique identifier of the subnet to check the registration. If ``None``, the
        registration is checked across all subnets.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    bool: ``True`` if the hotkey is registered in the specified context (either any subnet or a specific
        subnet), ``False`` otherwise.

This function is important for verifying the active status of neurons in the Bittensor network. It aids
in understanding whether a neuron is eligible to participate in network processes such as consensus,
validation, and incentive distribution based on its registration status.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `netuid`: `Optional[int]`
- `block`: `Optional[int]`

**Returns:** `bool`

---

## **`get_uid_for_hotkey_on_subnet`**

**Docstring:**
```
Retrieves the unique identifier (UID) for a neuron's hotkey on a specific subnet.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[int]: The UID of the neuron if it is registered on the subnet, ``None`` otherwise.

The UID is a critical identifier within the network, linking the neuron's hotkey to its
operational and governance activities on a particular subnet.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[int]`

---

## **`get_all_uids_for_hotkey`**

**Docstring:**
```
Retrieves all unique identifiers (UIDs) associated with a given hotkey across different subnets
within the Bittensor network. This function helps in identifying all the neuron instances that are
linked to a specific hotkey.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    List[int]: A list of UIDs associated with the given hotkey across various subnets.

This function is important for tracking a neuron's presence and activities across different
subnets within the Bittensor ecosystem.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `List[int]`

---

## **`get_netuids_for_hotkey`**

**Docstring:**
```
Retrieves a list of subnet UIDs (netuids) for which a given hotkey is a member. This function
identifies the specific subnets within the Bittensor network where the neuron associated with
the hotkey is active.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    List[int]: A list of netuids where the neuron is a member.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `List[int]`

---

## **`get_neuron_for_pubkey_and_subnet`**

**Docstring:**
```
Retrieves information about a neuron based on its public key (hotkey SS58 address) and the specific
subnet UID (netuid). This function provides detailed neuron information for a particular subnet within
the Bittensor network.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    Optional[NeuronInfo]: Detailed information about the neuron if found, ``None`` otherwise.

This function is crucial for accessing specific neuron data and understanding its status, stake,
and other attributes within a particular subnet of the Bittensor ecosystem.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[NeuronInfo]`

---

## **`get_all_neurons_for_pubkey`**

**Docstring:**
```
Retrieves information about all neuron instances associated with a given public key (hotkey ``SS58``
address) across different subnets of the Bittensor network. This function aggregates neuron data
from various subnets to provide a comprehensive view of a neuron's presence and status within the network.

Args:
    hotkey_ss58 (str): The ``SS58`` address of the neuron's hotkey.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    List[NeuronInfo]: A list of NeuronInfo objects detailing the neuron's presence across various subnets.

This function is valuable for analyzing a neuron's overall participation, influence, and
contributions across the Bittensor network.
```

**Parameters:**
- `self`
- `hotkey_ss58`: `str`
- `block`: `Optional[int]`

**Returns:** `List[NeuronInfo]`

---

## **`neuron_has_validator_permit`**

**Docstring:**
```
Checks if a neuron, identified by its unique identifier (UID), has a validator permit on a specific
subnet within the Bittensor network. This function determines whether the neuron is authorized to
participate in validation processes on the subnet.

Args:
    uid (int): The unique identifier of the neuron.
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[bool]: ``True`` if the neuron has a validator permit, False otherwise.

This function is essential for understanding a neuron's role and capabilities within a specific
subnet, particularly regarding its involvement in network validation and governance.
```

**Parameters:**
- `self`
- `uid`: `int`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[bool]`

---

## **`neuron_for_wallet`**

**Docstring:**
```
Retrieves information about a neuron associated with a given wallet on a specific subnet.
This function provides detailed data about the neuron's status, stake, and activities based on
the wallet's hotkey address.

Args:
    wallet (bittensor.wallet): The wallet associated with the neuron.
    netuid (int): The unique identifier of the subnet.
    block (Optional[int]): The blockchain block number at which to perform the query.

Returns:
    Optional[NeuronInfo]: Detailed information about the neuron if found, ``None`` otherwise.

This function is important for wallet owners to understand and manage their neuron's presence
and activities within a particular subnet of the Bittensor network.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[NeuronInfo]`

---

## **`neuron_for_uid`**

**Parameters:**
- `self`
- `uid`: `int`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[NeuronInfo]`

---

## **`neurons`**

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `List[NeuronInfo]`

---

## **`neuron_for_uid_lite`**

**Parameters:**
- `self`
- `uid`: `int`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[NeuronInfoLite]`

---

## **`neurons_lite`**

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `List[NeuronInfoLite]`

---

## **`metagraph`**

**Docstring:**
```
Returns a synced metagraph for a specified subnet within the Bittensor network. The metagraph
represents the network's structure, including neuron connections and interactions.

Args:
    netuid (int): The network UID of the subnet to query.
    lite (bool, default=True): If true, returns a metagraph using a lightweight sync (no weights, no bonds).
    block (Optional[int]): Block number for synchronization, or ``None`` for the latest block.

Returns:
    bittensor.Metagraph: The metagraph representing the subnet's structure and neuron relationships.

The metagraph is an essential tool for understanding the topology and dynamics of the Bittensor
network's decentralized architecture, particularly in relation to neuron interconnectivity and consensus
    processes.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `lite`: `bool`
- `block`: `Optional[int]`

**Returns:** `'bittensor.metagraph'`

---

## **`incentive`**

**Docstring:**
```
Retrieves the list of incentives for neurons within a specific subnet of the Bittensor network.
This function provides insights into the reward distribution mechanisms and the incentives allocated
to each neuron based on their contributions and activities.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    List[int]: The list of incentives for neurons within the subnet, indexed by UID.

Understanding the incentive structure is crucial for analyzing the network's economic model and
the motivational drivers for neuron participation and collaboration.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `List[int]`

---

## **`weights`**

**Docstring:**
```
Retrieves the weight distribution set by neurons within a specific subnet of the Bittensor network.
This function maps each neuron's UID to the weights it assigns to other neurons, reflecting the
network's trust and value assignment mechanisms.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    List[Tuple[int, List[Tuple[int, int]]]]: A list of tuples mapping each neuron's UID to its assigned weights.

The weight distribution is a key factor in the network's consensus algorithm and the ranking of neurons,
influencing their influence and reward allocation within the subnet.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `List[Tuple[int, List[Tuple[int, int]]]]`

---

## **`bonds`**

**Docstring:**
```
Retrieves the bond distribution set by neurons within a specific subnet of the Bittensor network.
Bonds represent the investments or commitments made by neurons in one another, indicating a level
of trust and perceived value. This bonding mechanism is integral to the network's market-based approach
to measuring and rewarding machine intelligence.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    List[Tuple[int, List[Tuple[int, int]]]]: A list of tuples mapping each neuron's UID to its bonds with other
        neurons.

Understanding bond distributions is crucial for analyzing the trust dynamics and market behavior
within the subnet. It reflects how neurons recognize and invest in each other's intelligence and
contributions, supporting diverse and niche systems within the Bittensor ecosystem.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `List[Tuple[int, List[Tuple[int, int]]]]`

---

## **`associated_validator_ip_info`**

**Docstring:**
```
Retrieves the list of all validator IP addresses associated with a specific subnet in the Bittensor
network. This information is crucial for network communication and the identification of validator nodes.

Args:
    netuid (int): The network UID of the subnet to query.
    block (Optional[int]): The blockchain block number for the query.

Returns:
    Optional[List[IPInfo]]: A list of IPInfo objects for validator nodes in the subnet, or ``None`` if no
        validators are associated.

Validator IP information is key for establishing secure and reliable connections within the network,
facilitating consensus and validation processes critical for the network's integrity and performance.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[List['IPInfo']]`

---

## **`get_subnet_burn_cost`**

**Docstring:**
```
Retrieves the burn cost for registering a new subnet within the Bittensor network. This cost
represents the amount of Tao that needs to be locked or burned to establish a new subnet.

Args:
    block (Optional[int]): The blockchain block number for the query.

Returns:
    int: The burn cost for subnet registration.

The subnet burn cost is an important economic parameter, reflecting the network's mechanisms for
controlling the proliferation of subnets and ensuring their commitment to the network's long-term viability.
```

**Parameters:**
- `self`
- `block`: `Optional[int]`

**Returns:** `Optional[str]`

---

## **`_do_delegation`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `delegate_ss58`: `str`
- `amount`: `'Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`_do_undelegation`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `delegate_ss58`: `str`
- `amount`: `'Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`_do_nominate`**

**Parameters:**
- `self`
- `wallet`: `'wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`_do_increase_take`**

**Docstring:**
```
Increases the take rate for a delegate's hotkey.

This method sends a transaction to increase the take rate for a delegate's hotkey and retries the call up to
three times with exponential backoff in case of failures.

Args:
    wallet (bittensor.wallet): The wallet from which the transaction will be signed.
    hotkey_ss58 (str): The SS58 address of the delegate's hotkey.
    take (int): The new take rate to be set.
    wait_for_inclusion (bool, optional): Whether to wait for the transaction to be included in a block. Default is ``True``.
    wait_for_finalization (bool, optional): Whether to wait for the transaction to be finalized. Default is ``False``.

Returns:
    bool: ``True`` if the take rate increase is successful, ``False`` otherwise.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `str`
- `take`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`_do_decrease_take`**

**Docstring:**
```
Decreases the take rate for a delegate's hotkey.

This method sends a transaction to decrease the take rate for a delegate's hotkey and retries the call up to
three times with exponential backoff in case of failures.

Args:
    wallet (bittensor.wallet): The wallet from which the transaction will be signed.
    hotkey_ss58 (str): The SS58 address of the delegate's hotkey.
    take (int): The new take rate to be set.
    wait_for_inclusion (bool, optional): Whether to wait for the transaction to be included in a block. Default is ``True``.
    wait_for_finalization (bool, optional): Whether to wait for the transaction to be finalized. Default is ``False``.

Returns:
    bool: ``True`` if the take rate decrease is successful, ``False`` otherwise.
```

**Parameters:**
- `self`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `str`
- `take`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`get_balance`**

**Parameters:**
- `self`
- `address`: `str`
- `block`: `int`

**Returns:** `'Balance'`

---

## **`get_current_block`**

**Parameters:**
- `self`

**Returns:** `int`

---

## **`get_balances`**

**Parameters:**
- `self`
- `block`: `int`

**Returns:** `Dict[str, 'Balance']`

---

## **`_null_neuron`**

**Parameters:**
None

**Returns:** `NeuronInfo`

---

## **`get_block_hash`**

**Parameters:**
- `self`
- `block_id`: `int`

**Returns:** `str`

---

## **`get_error_info_by_index`**

**Docstring:**
```
Returns the error name and description from the Subtensor error list.

Args:
    error_index (int): The index of the error to retrieve.

Returns:
    Tuple[str, str]: A tuple containing the error name and description from substrate metadata. If the error index is not found, returns ("Unknown Error", "") and logs a warning.
```

**Parameters:**
- `self`
- `error_index`: `int`

**Returns:** `Tuple[str, str]`

---

## **`make_substrate_call_with_retry`**

**Parameters:**
None

**Returns:** `None specified`

---

## **`prepare_synapse`**

**Docstring:**
```
Prepare the synapse-specific payload.
```

**Parameters:**
- `self`

**Returns:** `Any`

---

## **`process_responses`**

**Docstring:**
```
Process the responses from the network.
```

**Parameters:**
- `self`
- `responses`: `List[Union['bt.Synapse', Any]]`

**Returns:** `Any`

---

## **`error`**

**Docstring:**
```
Wraps error message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`__create_parser__`**

**Docstring:**
```
Creates the argument parser for the Bittensor CLI.

Returns:
    argparse.ArgumentParser: An argument parser object for Bittensor CLI.
```

**Parameters:**
None

**Returns:** `'argparse.ArgumentParser'`

---

## **`create_config`**

**Docstring:**
```
From the argument parser, add config to bittensor.executor and local config

Args:
    args (List[str]): List of command line arguments.

Returns:
    bittensor.config: The configuration object for Bittensor CLI.
```

**Parameters:**
- `args`: `List[str]`

**Returns:** `'bittensor.config'`

---

## **`extract_response_json`**

**Docstring:**
```
Abstract method that must be implemented by the subclass.
This method should provide logic to extract JSON data from the response, including headers and content.
It is called after the response has been processed and is responsible for retrieving structured data
that can be used by the application.

Args:
    response: The response object from which to extract JSON data.
```

**Parameters:**
- `self`
- `response`: `ClientResponse`

**Returns:** `dict`

---

## **`create_streaming_response`**

**Docstring:**
```
Creates a streaming response using the provided token streamer.
This method can be used by the subclass to create a response object that can be sent back to the client.
The token streamer should be implemented to generate the content of the response according to the specific
requirements of the subclass.

Args:
    token_streamer: A callable that takes a send function and returns an awaitable. It's responsible for generating the content of the response.

Returns:
    BTStreamingResponse: The streaming response object, ready to be sent to the client.
```

**Parameters:**
- `self`
- `token_streamer`: `Callable[[Send], Awaitable[None]]`

**Returns:** `BTStreamingResponse`

---

## **`cast_dtype`**

**Docstring:**
```
Casts the raw value to a string representing the
`numpy data type <https://numpy.org/doc/stable/user/basics.types.html>`_, or the
`torch data type <https://pytorch.org/docs/stable/tensor_attributes.html>`_ if using torch.

Args:
    raw (Union[None, numpy.dtype, torch.dtype, str]): The raw value to cast.

Returns:
    str: The string representing the numpy/torch data type.

Raises:
    Exception: If the raw value is of an invalid type.
```

**Parameters:**
- `raw`: `Union[None, np.dtype, 'torch.dtype', str]`

**Returns:** `Optional[str]`

---

## **`cast_shape`**

**Docstring:**
```
Casts the raw value to a string representing the tensor shape.

Args:
    raw (Union[None, List[int], str]): The raw value to cast.

Returns:
    str: The string representing the tensor shape.

Raises:
    Exception: If the raw value is of an invalid type or if the list elements are not of type int.
```

**Parameters:**
- `raw`: `Union[None, List[int], str]`

**Returns:** `Optional[Union[str, list]]`

---

## **`__getitem__`**

**Parameters:**
- `self`
- `key`

**Returns:** `None specified`

---

## **`__contains__`**

**Parameters:**
- `self`
- `key`

**Returns:** `None specified`

---

## **`_add_torch`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__new__`**

**Parameters:**
- `cls`
- `tensor`: `Union[list, np.ndarray, 'torch.Tensor']`

**Returns:** `None specified`

---

## **`tensor`**

**Parameters:**
- `self`

**Returns:** `Union[np.ndarray, 'torch.Tensor']`

---

## **`tolist`**

**Parameters:**
- `self`

**Returns:** `List[object]`

---

## **`numpy`**

**Parameters:**
- `self`

**Returns:** `'numpy.ndarray'`

---

## **`serialize`**

**Docstring:**
```
Serializes the given tensor.

Args:
    tensor_ (np.array or torch.Tensor): The tensor to serialize.

Returns:
    Tensor: The serialized tensor.

Raises:
    Exception: If the serialization process encounters an error.
```

**Parameters:**
- `tensor_`: `Union['np.ndarray', 'torch.Tensor']`

**Returns:** `'Tensor'`

---

## **`ss58_to_vec_u8`**

**Parameters:**
- `ss58_address`: `str`

**Returns:** `List[int]`

---

## **`_unbiased_topk`**

**Docstring:**
```
Selects topk as in torch.topk but does not bias lower indices when values are equal.
Args:
    values: (np.ndarray) if using numpy, (torch.Tensor) if using torch:
        Values to index into.
    k: (int):
        Number to take.
    dim: (int):
        Dimension to index into (used by Torch)
    sorted: (bool):
        Whether to sort indices.
    largest: (bool):
        Whether to take the largest value.
    axis: (int):
        Axis along which to index into (used by Numpy)
    return_type: (str):
        Whether or use torch or numpy approach

Return:
    topk: (np.ndarray) if using numpy, (torch.Tensor) if using torch:
        topk k values.
    indices: (np.ndarray) if using numpy, (torch.LongTensor) if using torch:
        indices of the topk values.
```

**Parameters:**
- `values`: `Union[np.ndarray, 'torch.Tensor']`
- `k`: `int`
- `dim`
- `sorted`
- `largest`
- `axis`
- `return_type`: `str`

**Returns:** `Union[Tuple[np.ndarray, np.ndarray], Tuple['torch.Tensor', 'torch.LongTensor']]`

---

## **`unbiased_topk`**

**Docstring:**
```
Selects topk as in torch.topk but does not bias lower indices when values are equal.
Args:
    values: (np.ndarray) if using numpy, (torch.Tensor) if using torch:
        Values to index into.
    k: (int):
        Number to take.
    dim: (int):
        Dimension to index into (used by Torch)
    sorted: (bool):
        Whether to sort indices.
    largest: (bool):
        Whether to take the largest value.
    axis: (int):
        Axis along which to index into (used by Numpy)

Return:
    topk: (np.ndarray) if using numpy, (torch.Tensor) if using torch:
        topk k values.
    indices: (np.ndarray) if using numpy, (torch.LongTensor) if using torch:
        indices of the topk values.
```

**Parameters:**
- `values`: `Union[np.ndarray, 'torch.Tensor']`
- `k`: `int`
- `dim`: `int`
- `sorted`: `bool`
- `largest`: `bool`
- `axis`: `int`

**Returns:** `Union[Tuple[np.ndarray, np.ndarray], Tuple['torch.Tensor', 'torch.LongTensor']]`

---

## **`strtobool_with_default`**

**Docstring:**
```
Creates a strtobool function with a default value.

Args:
    default(bool): The default value to return if the string is empty.

Returns:
    The strtobool function with the default value.
```

**Parameters:**
- `default`: `bool`

**Returns:** `Callable[[str], Union[bool, Literal['==SUPRESS==']]]`

---

## **`strtobool`**

**Docstring:**
```
Converts a string to a boolean value.

truth-y values are 'y', 'yes', 't', 'true', 'on', and '1';
false-y values are 'n', 'no', 'f', 'false', 'off', and '0'.

Raises ValueError if 'val' is anything else.
```

**Parameters:**
- `val`: `str`

**Returns:** `Union[bool, Literal['==SUPRESS==']]`

---

## **`get_explorer_root_url_by_network_from_map`**

**Docstring:**
```
Returns the explorer root url for the given network name from the given network map.

Args:
    network(str): The network to get the explorer url for.
    network_map(Dict[str, str]): The network map to get the explorer url from.

Returns:
    The explorer url for the given network.
    Or None if the network is not in the network map.
```

**Parameters:**
- `network`: `str`
- `network_map`: `Dict[str, Dict[str, str]]`

**Returns:** `Optional[Dict[str, str]]`

---

## **`get_explorer_url_for_network`**

**Docstring:**
```
Returns the explorer url for the given block hash and network.

Args:
    network(str): The network to get the explorer url for.
    block_hash(str): The block hash to get the explorer url for.
    network_map(Dict[str, Dict[str, str]]): The network maps to get the explorer urls from.

Returns:
    The explorer url for the given block hash and network.
    Or None if the network is not known.
```

**Parameters:**
- `network`: `str`
- `block_hash`: `str`
- `network_map`: `Dict[str, str]`

**Returns:** `Optional[List[str]]`

---

## **`ss58_address_to_bytes`**

**Docstring:**
```
Converts a ss58 address to a bytes object.
```

**Parameters:**
- `ss58_address`: `str`

**Returns:** `bytes`

---

## **`U16_NORMALIZED_FLOAT`**

**Parameters:**
- `x`: `int`

**Returns:** `float`

---

## **`U64_NORMALIZED_FLOAT`**

**Parameters:**
- `x`: `int`

**Returns:** `float`

---

## **`u8_key_to_ss58`**

**Docstring:**
```
Converts a u8-encoded account key to an ss58 address.

Args:
    u8_key (List[int]): The u8-encoded account key.
```

**Parameters:**
- `u8_key`: `List[int]`

**Returns:** `str`

---

## **`hash`**

**Parameters:**
- `content`
- `encoding`

**Returns:** `None specified`

---

## **`format_error_message`**

**Docstring:**
```
Formats an error message from the Subtensor error information to using in extrinsics.

Args:
    error_message (dict): A dictionary containing the error information from Subtensor.

Returns:
    str: A formatted error message string.
```

**Parameters:**
- `error_message`: `dict`

**Returns:** `str`

---

## **`get_human_readable`**

**Parameters:**
- `num`
- `suffix`

**Returns:** `None specified`

---

## **`millify`**

**Parameters:**
- `n`: `int`

**Returns:** `None specified`

---

## **`convert_blocks_to_time`**

**Docstring:**
```
Converts number of blocks into number of hours, minutes, seconds.
:param blocks: number of blocks
:param block_time: time per block, by default this is 12
:return: tuple containing number of hours, number of minutes, number of seconds
```

**Parameters:**
- `blocks`: `int`
- `block_time`: `int`

**Returns:** `tuple[int, int, int]`

---

## **`tao`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__int__`**

**Parameters:**
- `self`

**Returns:** `int`

---

## **`__float__`**

**Parameters:**
- `self`

**Returns:** `float`

---

## **`__rich__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__str_rao__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__rich_rao__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__ne__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__gt__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__lt__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__le__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__ge__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__add__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__radd__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__sub__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__rsub__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__mul__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__rmul__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__truediv__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__rtruediv__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__floordiv__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__rfloordiv__`**

**Parameters:**
- `self`
- `other`: `Union[int, float, 'Balance']`

**Returns:** `None specified`

---

## **`__nonzero__`**

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`__neg__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__pos__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__abs__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`from_float`**

**Docstring:**
```
Given tao (float), return Balance object with rao(int) and tao(float), where rao = int(tao*pow(10,9))
Args:
    amount: The amount in tao.

Returns:
    A Balance object representing the given amount.
```

**Parameters:**
- `amount`: `float`

**Returns:** `None specified`

---

## **`from_tao`**

**Docstring:**
```
Given tao (float), return Balance object with rao(int) and tao(float), where rao = int(tao*pow(10,9))

Args:
    amount: The amount in tao.

Returns:
    A Balance object representing the given amount.
```

**Parameters:**
- `amount`: `float`

**Returns:** `None specified`

---

## **`from_rao`**

**Docstring:**
```
Given rao (int), return Balance object with rao(int) and tao(float), where rao = int(tao*pow(10,9))

Args:
    amount: The amount in rao.

Returns:
    A Balance object representing the given amount.
```

**Parameters:**
- `amount`: `int`

**Returns:** `None specified`

---

## **`get_ss58_format`**

**Docstring:**
```
Returns the ss58 format of the given ss58 address.
```

**Parameters:**
- `ss58_address`: `str`

**Returns:** `int`

---

## **`is_valid_ss58_address`**

**Docstring:**
```
Checks if the given address is a valid ss58 address.

Args:
    address(str): The address to check.

Returns:
    True if the address is a valid ss58 address for Bittensor, False otherwise.
```

**Parameters:**
- `address`: `str`

**Returns:** `bool`

---

## **`is_valid_ed25519_pubkey`**

**Docstring:**
```
Checks if the given public_key is a valid ed25519 key.

Args:
    public_key(Union[str, bytes]): The public_key to check.

Returns:
    True if the public_key is a valid ed25519 key, False otherwise.
```

**Parameters:**
- `public_key`: `Union[str, bytes]`

**Returns:** `bool`

---

## **`is_valid_bittensor_address_or_public_key`**

**Docstring:**
```
Checks if the given address is a valid destination address.

Args:
    address(Union[str, bytes]): The address to check.

Returns:
    True if the address is a valid destination address, False otherwise.
```

**Parameters:**
- `address`: `Union[str, bytes]`

**Returns:** `bool`

---

## **`create_identity_dict`**

**Docstring:**
```
Creates a dictionary with structure for identity extrinsic. Must fit within 64 bits.

Args:
    display (str): String to be converted and stored under 'display'.
    legal (str): String to be converted and stored under 'legal'.
    web (str): String to be converted and stored under 'web'.
    riot (str): String to be converted and stored under 'riot'.
    email (str): String to be converted and stored under 'email'.
    pgp_fingerprint (str): String to be converted and stored under 'pgp_fingerprint'.
    image (str): String to be converted and stored under 'image'.
    info (str): String to be converted and stored under 'info'.
    twitter (str): String to be converted and stored under 'twitter'.

Returns:
    dict: A dictionary with the specified structure and byte string conversions.

Raises:
ValueError: If pgp_fingerprint is not exactly 20 bytes long when encoded.
```

**Parameters:**
- `display`: `str`
- `legal`: `str`
- `web`: `str`
- `riot`: `str`
- `email`: `str`
- `pgp_fingerprint`: `Optional[str]`
- `image`: `str`
- `info`: `str`
- `twitter`: `str`

**Returns:** `dict`

---

## **`decode_hex_identity_dict`**

**Parameters:**
- `info_dictionary`

**Returns:** `None specified`

---

## **`use_torch`**

**Docstring:**
```
Force the use of torch over numpy for certain operations.
```

**Parameters:**
None

**Returns:** `bool`

---

## **`legacy_torch_api_compat`**

**Docstring:**
```
Convert function operating on numpy Input&Output to legacy torch Input&Output API if `use_torch()` is True.

Args:
    func (function):
        Function with numpy Input/Output to be decorated.
Returns:
    decorated (function):
        Decorated function.
```

**Parameters:**
- `func`

**Returns:** `None specified`

---

## **`_get_real_torch`**

**Parameters:**
None

**Returns:** `None specified`

---

## **`log_no_torch_error`**

**Parameters:**
None

**Returns:** `None specified`

---

## **`_hex_bytes_to_u8_list`**

**Parameters:**
- `hex_bytes`: `bytes`

**Returns:** `None specified`

---

## **`_create_seal_hash`**

**Parameters:**
- `block_and_hotkey_hash_hex`: `bytes`
- `nonce`: `int`

**Returns:** `bytes`

---

## **`_seal_meets_difficulty`**

**Parameters:**
- `seal`: `bytes`
- `difficulty`: `int`

**Returns:** `None specified`

---

## **`_solve_for_nonce_block_cuda`**

**Docstring:**
```
Tries to solve the POW on a CUDA device for a block of nonces (nonce_start, nonce_start + update_interval * tpb
```

**Parameters:**
- `nonce_start`: `int`
- `update_interval`: `int`
- `block_and_hotkey_hash_bytes`: `bytes`
- `difficulty`: `int`
- `limit`: `int`
- `block_number`: `int`
- `dev_id`: `int`
- `tpb`: `int`

**Returns:** `Optional[POWSolution]`

---

## **`_solve_for_nonce_block`**

**Docstring:**
```
Tries to solve the POW for a block of nonces (nonce_start, nonce_end)
```

**Parameters:**
- `nonce_start`: `int`
- `nonce_end`: `int`
- `block_and_hotkey_hash_bytes`: `bytes`
- `difficulty`: `int`
- `limit`: `int`
- `block_number`: `int`

**Returns:** `Optional[POWSolution]`

---

## **`_registration_diff_unpack`**

**Docstring:**
```
Unpacks the packed two 32-bit integers into one 64-bit integer. Little endian.
```

**Parameters:**
- `packed_diff`: `multiprocessing.Array`

**Returns:** `int`

---

## **`_registration_diff_pack`**

**Docstring:**
```
Packs the difficulty into two 32-bit integers. Little endian.
```

**Parameters:**
- `diff`: `int`
- `packed_diff`: `multiprocessing.Array`

**Returns:** `None specified`

---

## **`_hash_block_with_hotkey`**

**Docstring:**
```
Hashes the block with the hotkey using Keccak-256 to get 32 bytes
```

**Parameters:**
- `block_bytes`: `bytes`
- `hotkey_bytes`: `bytes`

**Returns:** `bytes`

---

## **`_update_curr_block`**

**Parameters:**
- `curr_diff`: `multiprocessing.Array`
- `curr_block`: `multiprocessing.Array`
- `curr_block_num`: `multiprocessing.Value`
- `block_number`: `int`
- `block_bytes`: `bytes`
- `diff`: `int`
- `hotkey_bytes`: `bytes`
- `lock`: `multiprocessing.Lock`

**Returns:** `None specified`

---

## **`get_cpu_count`**

**Parameters:**
None

**Returns:** `int`

---

## **`_solve_for_difficulty_fast`**

**Docstring:**
```
Solves the POW for registration using multiprocessing.
Args:
    subtensor
        Subtensor to connect to for block information and to submit.
    wallet:
        wallet to use for registration.
    netuid: int
        The netuid of the subnet to register to.
    output_in_place: bool
        If true, prints the status in place. Otherwise, prints the status on a new line.
    num_processes: int
        Number of processes to use.
    update_interval: int
        Number of nonces to solve before updating block information.
    n_samples: int
        The number of samples of the hash_rate to keep for the EWMA
    alpha_: float
        The alpha for the EWMA for the hash_rate calculation
    log_verbose: bool
        If true, prints more verbose logging of the registration metrics.
Note: The hash rate is calculated as an exponentially weighted moving average in order to make the measure more robust.
Note:
- We can also modify the update interval to do smaller blocks of work,
    while still updating the block information after a different number of nonces,
    to increase the transparency of the process while still keeping the speed.
```

**Parameters:**
- `subtensor`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `output_in_place`: `bool`
- `num_processes`: `Optional[int]`
- `update_interval`: `Optional[int]`
- `n_samples`: `int`
- `alpha_`: `float`
- `log_verbose`: `bool`

**Returns:** `Optional[POWSolution]`

---

## **`_get_block_with_retry`**

**Docstring:**
```
Gets the current block number, difficulty, and block hash from the substrate node.

Args:
    subtensor (:obj:`bittensor.subtensor`, `required`):
        The subtensor object to use to get the block number, difficulty, and block hash.

    netuid (:obj:`int`, `required`):
        The netuid of the network to get the block number, difficulty, and block hash from.

Returns:
    block_number (:obj:`int`):
        The current block number.

    difficulty (:obj:`int`):
        The current difficulty of the subnet.

    block_hash (:obj:`bytes`):
        The current block hash.

Raises:
    Exception: If the block hash is None.
    ValueError: If the difficulty is None.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `netuid`: `int`

**Returns:** `Tuple[int, int, bytes]`

---

## **`_check_for_newest_block_and_update`**

**Docstring:**
```
Checks for a new block and updates the current block information if a new block is found.

Args:
    subtensor (:obj:`bittensor.subtensor`, `required`):
        The subtensor object to use for getting the current block.
    netuid (:obj:`int`, `required`):
        The netuid to use for retrieving the difficulty.
    old_block_number (:obj:`int`, `required`):
        The old block number to check against.
    hotkey_bytes (:obj:`bytes`, `required`):
        The bytes of the hotkey's pubkey.
    curr_diff (:obj:`multiprocessing.Array`, `required`):
        The current difficulty as a multiprocessing array.
    curr_block (:obj:`multiprocessing.Array`, `required`):
        Where the current block is stored as a multiprocessing array.
    curr_block_num (:obj:`multiprocessing.Value`, `required`):
        Where the current block number is stored as a multiprocessing value.
    update_curr_block (:obj:`Callable`, `required`):
        A function that updates the current block.
    check_block (:obj:`multiprocessing.Lock`, `required`):
        A mp lock that is used to check for a new block.
    solvers (:obj:`List[_Solver]`, `required`):
        A list of solvers to update the current block for.
    curr_stats (:obj:`RegistrationStatistics`, `required`):
        The current registration statistics to update.

Returns:
    (int) The current block number.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `netuid`: `int`
- `old_block_number`: `int`
- `hotkey_bytes`: `bytes`
- `curr_diff`: `multiprocessing.Array`
- `curr_block`: `multiprocessing.Array`
- `curr_block_num`: `multiprocessing.Value`
- `update_curr_block`: `Callable`
- `check_block`: `'multiprocessing.Lock'`
- `solvers`: `List[_Solver]`
- `curr_stats`: `RegistrationStatistics`

**Returns:** `int`

---

## **`_solve_for_difficulty_fast_cuda`**

**Docstring:**
```
Solves the registration fast using CUDA
Args:
    subtensor: bittensor.subtensor
        The subtensor node to grab blocks
    wallet: bittensor.wallet
        The wallet to register
    netuid: int
        The netuid of the subnet to register to.
    output_in_place: bool
        If true, prints the output in place, otherwise prints to new lines
    update_interval: int
        The number of nonces to try before checking for more blocks
    tpb: int
        The number of threads per block. CUDA param that should match the GPU capability
    dev_id: Union[List[int], int]
        The CUDA device IDs to execute the registration on, either a single device or a list of devices
    n_samples: int
        The number of samples of the hash_rate to keep for the EWMA
    alpha_: float
        The alpha for the EWMA for the hash_rate calculation
    log_verbose: bool
        If true, prints more verbose logging of the registration metrics.
Note: The hash rate is calculated as an exponentially weighted moving average in order to make the measure more robust.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `output_in_place`: `bool`
- `update_interval`: `int`
- `tpb`: `int`
- `dev_id`: `Union[List[int], int]`
- `n_samples`: `int`
- `alpha_`: `float`
- `log_verbose`: `bool`

**Returns:** `Optional[POWSolution]`

---

## **`_terminate_workers_and_wait_for_exit`**

**Parameters:**
- `workers`: `List[multiprocessing.Process]`

**Returns:** `None`

---

## **`create_pow`**

**Docstring:**
```
Creates a proof of work for the given subtensor and wallet.
Args:
    subtensor (:obj:`bittensor.subtensor.subtensor`, `required`):
        The subtensor to create a proof of work for.
    wallet (:obj:`bittensor.wallet.wallet`, `required`):
        The wallet to create a proof of work for.
    netuid (:obj:`int`, `required`):
        The netuid for the subnet to create a proof of work for.
    output_in_place (:obj:`bool`, `optional`, defaults to :obj:`True`):
        If true, prints the progress of the proof of work to the console
            in-place. Meaning the progress is printed on the same lines.
    cuda (:obj:`bool`, `optional`, defaults to :obj:`False`):
        If true, uses CUDA to solve the proof of work.
    dev_id (:obj:`Union[List[int], int]`, `optional`, defaults to :obj:`0`):
        The CUDA device id(s) to use. If cuda is true and dev_id is a list,
            then multiple CUDA devices will be used to solve the proof of work.
    tpb (:obj:`int`, `optional`, defaults to :obj:`256`):
        The number of threads per block to use when solving the proof of work.
        Should be a multiple of 32.
    num_processes (:obj:`int`, `optional`, defaults to :obj:`None`):
        The number of processes to use when solving the proof of work.
        If None, then the number of processes is equal to the number of
            CPU cores.
    update_interval (:obj:`int`, `optional`, defaults to :obj:`None`):
        The number of nonces to run before checking for a new block.
    log_verbose (:obj:`bool`, `optional`, defaults to :obj:`False`):
        If true, prints the progress of the proof of work more verbosely.
Returns:
    :obj:`Optional[Dict[str, Any]]`: The proof of work solution or None if
        the wallet is already registered or there is a different error.

Raises:
    :obj:`ValueError`: If the subnet does not exist.
```

**Parameters:**
- `subtensor`
- `wallet`
- `netuid`: `int`
- `output_in_place`: `bool`
- `cuda`: `bool`
- `dev_id`: `Union[List[int], int]`
- `tpb`: `int`
- `num_processes`: `int`
- `update_interval`: `int`
- `log_verbose`: `bool`

**Returns:** `Optional[Dict[str, Any]]`

---

## **`decorated`**

**Parameters:**
None

**Returns:** `None specified`

---

## **`__bool__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`is_stale`**

**Docstring:**
```
Returns True if the POW is stale.
This means the block the POW is solved for is within 3 blocks of the current block.
```

**Parameters:**
- `self`
- `subtensor`: `'bittensor.subtensor'`

**Returns:** `bool`

---

## **`create_shared_memory`**

**Docstring:**
```
Creates shared memory for the solver processes to use.
```

**Parameters:**
None

**Returns:** `Tuple[multiprocessing.Array, multiprocessing.Value, multiprocessing.Array]`

---

## **`get_status_message`**

**Parameters:**
- `cls`
- `stats`: `RegistrationStatistics`
- `verbose`: `bool`

**Returns:** `str`

---

## **`update`**

**Parameters:**
- `self`
- `stats`: `RegistrationStatistics`
- `verbose`: `bool`

**Returns:** `None`

---

## **`__enter__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__exit__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`get_random_unused_port`**

**Parameters:**
- `allocated_ports`: `Set`

**Returns:** `None specified`

---

## **`port_in_use`**

**Parameters:**
- `port`: `int`

**Returns:** `bool`

---

## **`int_to_ip`**

**Docstring:**
```
Maps an integer to a unique ip-string
Args:
    int_val  (:type:`int128`, `required`):
        The integer representation of an ip. Must be in the range (0, 3.4028237e+38).

Returns:
    str_val (:tyep:`str`, `required):
        The string representation of an ip. Of form *.*.*.* for ipv4 or *::*:*:*:* for ipv6

Raises:
    netaddr.core.AddrFormatError (Exception):
        Raised when the passed int_vals is not a valid ip int value.
```

**Parameters:**
- `int_val`: `int`

**Returns:** `str`

---

## **`ip_to_int`**

**Docstring:**
```
Maps an ip-string to a unique integer.
arg:
    str_val (:tyep:`str`, `required):
        The string representation of an ip. Of form *.*.*.* for ipv4 or *::*:*:*:* for ipv6

Returns:
    int_val  (:type:`int128`, `required`):
        The integer representation of an ip. Must be in the range (0, 3.4028237e+38).

Raises:
    netaddr.core.AddrFormatError (Exception):
        Raised when the passed str_val is not a valid ip string value.
```

**Parameters:**
- `str_val`: `str`

**Returns:** `int`

---

## **`ip_version`**

**Docstring:**
```
Returns the ip version (IPV4 or IPV6).
arg:
    str_val (:tyep:`str`, `required):
        The string representation of an ip. Of form *.*.*.* for ipv4 or *::*:*:*:* for ipv6

Returns:
    int_val  (:type:`int128`, `required`):
        The ip version (Either 4 or 6 for IPv4/IPv6)

Raises:
    netaddr.core.AddrFormatError (Exception):
        Raised when the passed str_val is not a valid ip string value.
```

**Parameters:**
- `str_val`: `str`

**Returns:** `int`

---

## **`ip__str__`**

**Docstring:**
```
Return a formatted ip string
```

**Parameters:**
- `ip_type`: `int`
- `ip_str`: `str`
- `port`: `int`

**Returns:** `None specified`

---

## **`get_external_ip`**

**Docstring:**
```
Checks CURL/URLLIB/IPIFY/AWS for your external ip.
Returns:
    external_ip  (:obj:`str` `required`):
        Your routers external facing ip as a string.

Raises:
    ExternalIPNotFound (Exception):
        Raised if all external ip attempts fail.
```

**Parameters:**
None

**Returns:** `str`

---

## **`get_formatted_ws_endpoint_url`**

**Docstring:**
```
Returns a formatted websocket endpoint url.
Note: The port (or lack thereof) is left unchanged
Args:
    endpoint_url (str, `required`):
        The endpoint url to format.
Returns:
    formatted_endpoint_url (str, `required`):
        The formatted endpoint url. In the form of ws://<endpoint_url> or wss://<endpoint_url>
```

**Parameters:**
- `endpoint_url`: `str`

**Returns:** `str`

---

## **`_get_errors_from_pallet`**

**Docstring:**
```
Extracts and returns error information from the given pallet metadata.

Args:
    pallet (PalletMetadataV14): The pallet metadata containing error definitions.

Returns:
    dict[str, str]: A dictionary of errors indexed by their IDs.

Raises:
    ValueError: If the pallet does not contain error definitions or the list is empty.
```

**Parameters:**
- `pallet`

**Returns:** `Optional[Dict[str, Dict[str, str]]]`

---

## **`_save_errors_to_cache`**

**Docstring:**
```
Saves error details and unique version identifier to a JSON file.

Args:
    uniq_version (str): Unique version identifier for the Subtensor build.
    errors (dict[str, str]): Error information to be cached.
```

**Parameters:**
- `uniq_version`: `str`
- `errors`: `Dict[str, Dict[str, str]]`

**Returns:** `None specified`

---

## **`_get_errors_from_cache`**

**Docstring:**
```
Retrieves and returns the cached error information from a JSON file, if it exists.

Returns:
        A dictionary containing error information.
```

**Parameters:**
None

**Returns:** `Optional[Dict[str, Dict[str, Dict[str, str]]]]`

---

## **`get_subtensor_errors`**

**Docstring:**
```
Fetches or retrieves cached Subtensor error definitions using metadata.

Args:
    substrate (SubstrateInterface): Instance of SubstrateInterface to access metadata.

Returns:
    dict[str, str]: A dictionary containing error information.
```

**Parameters:**
- `substrate`: `SubstrateInterface`

**Returns:** `Union[Dict[str, Dict[str, str]], Dict[Any, Any]]`

---

## **`_get_version_file_path`**

**Parameters:**
None

**Returns:** `Path`

---

## **`_get_version_from_file`**

**Parameters:**
- `version_file`: `Path`

**Returns:** `Optional[str]`

---

## **`_get_version_from_pypi`**

**Parameters:**
- `timeout`: `int`

**Returns:** `str`

---

## **`get_and_save_latest_version`**

**Parameters:**
- `timeout`: `int`

**Returns:** `str`

---

## **`check_version`**

**Docstring:**
```
Check if the current version of Bittensor is up to date with the latest version on PyPi.
Raises a VersionCheckError if the version check fails.
```

**Parameters:**
- `timeout`: `int`

**Returns:** `None specified`

---

## **`version_checking`**

**Docstring:**
```
Deprecated, kept for backwards compatibility. Use check_version() instead.
```

**Parameters:**
- `timeout`: `int`

**Returns:** `None specified`

---

## **`normalize_max_weight`**

**Docstring:**
```
Normalizes the tensor x so that sum(x) = 1 and the max value is not greater than the limit.
Args:
    x (:obj:`np.float32`):
        Tensor to be max_value normalized.
    limit: float:
        Max value after normalization.
Returns:
    y (:obj:`np.float32`):
        Normalized x tensor.
```

**Parameters:**
- `x`: `Union[NDArray[np.float32], 'torch.FloatTensor']`
- `limit`: `float`

**Returns:** `Union[NDArray[np.float32], 'torch.FloatTensor']`

---

## **`convert_weight_uids_and_vals_to_tensor`**

**Docstring:**
```
Converts weights and uids from chain representation into a np.array (inverse operation from convert_weights_and_uids_for_emit)
Args:
    n: int:
        number of neurons on network.
    uids (:obj:`List[int],`):
        Tensor of uids as destinations for passed weights.
    weights (:obj:`List[int],`):
        Tensor of weights.
Returns:
    row_weights ( np.float32 or torch.FloatTensor ):
        Converted row weights.
```

**Parameters:**
- `n`: `int`
- `uids`: `List[int]`
- `weights`: `List[int]`

**Returns:** `Union[NDArray[np.float32], 'torch.FloatTensor']`

---

## **`convert_root_weight_uids_and_vals_to_tensor`**

**Docstring:**
```
Converts root weights and uids from chain representation into a np.array or torch FloatTensor (inverse operation from convert_weights_and_uids_for_emit)
Args:
    n: int:
        number of neurons on network.
    uids (:obj:`List[int],`):
        Tensor of uids as destinations for passed weights.
    weights (:obj:`List[int],`):
        Tensor of weights.
    subnets (:obj:`List[int],`):
        list of subnets on the network
Returns:
    row_weights ( np.float32 ):
        Converted row weights.
```

**Parameters:**
- `n`: `int`
- `uids`: `List[int]`
- `weights`: `List[int]`
- `subnets`: `List[int]`

**Returns:** `Union[NDArray[np.float32], 'torch.FloatTensor']`

---

## **`convert_bond_uids_and_vals_to_tensor`**

**Docstring:**
```
Converts bond and uids from chain representation into a np.array.
Args:
    n: int:
        number of neurons on network.
    uids (:obj:`List[int],`):
        Tensor of uids as destinations for passed bonds.
    bonds (:obj:`List[int],`):
        Tensor of bonds.
Returns:
    row_bonds ( np.float32 ):
        Converted row bonds.
```

**Parameters:**
- `n`: `int`
- `uids`: `List[int]`
- `bonds`: `List[int]`

**Returns:** `Union[NDArray[np.int64], 'torch.LongTensor']`

---

## **`convert_weights_and_uids_for_emit`**

**Docstring:**
```
Converts weights into integer u32 representation that sum to MAX_INT_WEIGHT.
Args:
    uids (:obj:`np.int64,`):
        Tensor of uids as destinations for passed weights.
    weights (:obj:`np.float32,`):
        Tensor of weights.
Returns:
    weight_uids (List[int]):
        Uids as a list.
    weight_vals (List[int]):
        Weights as a list.
```

**Parameters:**
- `uids`: `Union[NDArray[np.int64], 'torch.LongTensor']`
- `weights`: `Union[NDArray[np.float32], 'torch.FloatTensor']`

**Returns:** `Tuple[List[int], List[int]]`

---

## **`process_weights_for_netuid`**

**Parameters:**
- `uids`: `Union[NDArray[np.int64], 'torch.Tensor']`
- `weights`: `Union[NDArray[np.float32], 'torch.Tensor']`
- `netuid`: `int`
- `subtensor`: `'bittensor.subtensor'`
- `metagraph`: `'bittensor.metagraph'`
- `exclude_quantile`: `int`

**Returns:** `Union[Tuple['torch.Tensor', 'torch.FloatTensor'], Tuple[NDArray[np.int64], NDArray[np.float32]]]`

---

## **`generate_weight_hash`**

**Docstring:**
```
Generate a valid commit hash from the provided weights.

Args:
    address (str): The account identifier. Wallet ss58_address.
    netuid (int): The network unique identifier.
    uids (List[int]): The list of UIDs.
    salt (List[int]): The salt to add to hash.
    values (List[int]): The list of weight values.
    version_key (int): The version key.

Returns:
    str: The generated commit hash.
```

**Parameters:**
- `address`: `str`
- `netuid`: `int`
- `uids`: `List[int]`
- `values`: `List[int]`
- `version_key`: `int`
- `salt`: `List[int]`

**Returns:** `str`

---

## **`solve_cuda`**

**Docstring:**
```
Solves the PoW problem using CUDA.
Args:
    nonce_start: int64
        Starting nonce.
    update_interval: int64
        Number of nonces to solve before updating block information.
    tpb: int
        Threads per block.
    block_and_hotkey_hash_bytes: bytes
        Keccak(Bytes of the block hash + bytes of the hotkey) 64 bytes.
    difficulty: int256
        Difficulty of the PoW problem.
    limit: int256
        Upper limit of the nonce.
    dev_id: int (default=0)
        The CUDA device ID
Returns:
    Tuple[int64, bytes]
        Tuple of the nonce and the seal corresponding to the solution.
        Returns -1 for nonce if no solution is found.
```

**Parameters:**
- `nonce_start`: `np.int64`
- `update_interval`: `np.int64`
- `tpb`: `int`
- `block_and_hotkey_hash_bytes`: `bytes`
- `difficulty`: `int`
- `limit`: `int`
- `dev_id`: `int`

**Returns:** `Tuple[np.int64, bytes]`

---

## **`reset_cuda`**

**Docstring:**
```
Resets the CUDA environment.
```

**Parameters:**
None

**Returns:** `None specified`

---

## **`log_cuda_errors`**

**Docstring:**
```
Logs any CUDA errors.
```

**Parameters:**
None

**Returns:** `str`

---

## **`all_loggers`**

**Docstring:**
```
Generator that yields all logger instances in the application.

Iterates through the logging root manager's logger dictionary and yields all active `Logger` instances. It skips
placeholders and other types that are not instances of `Logger`.

Yields:
    logger (logging.Logger): An active logger instance.
```

**Parameters:**
None

**Returns:** `Generator[logging.Logger, None, None]`

---

## **`all_logger_names`**

**Docstring:**
```
Generate the names of all active loggers.

This function iterates through the logging root manager's logger dictionary and yields the names of all active
`Logger` instances. It skips placeholders and other types that are not instances of `Logger`.

Yields:
    name (str): The name of an active logger.
```

**Parameters:**
None

**Returns:** `Generator[str, None, None]`

---

## **`get_max_logger_name_length`**

**Docstring:**
```
Calculate and return the length of the longest logger name.

This function iterates through all active logger names and determines the length of the longest name.

Returns:
    max_length (int): The length of the longest logger name.
```

**Parameters:**
None

**Returns:** `int`

---

## **`_trace`**

**Parameters:**
- `self`
- `message`: `str`

**Returns:** `None specified`

---

## **`_success`**

**Parameters:**
- `self`
- `message`: `str`

**Returns:** `None specified`

---

## **`formatTime`**

**Docstring:**
```
Override formatTime to add milliseconds.

Args:
    record (logging.LogRecord): The log record.
    datefmt (str, optional): The date format string.

Returns:
    s (str): The formatted time string with milliseconds.
```

**Parameters:**
- `self`
- `record`
- `datefmt`

**Returns:** `str`

---

## **`format`**

**Docstring:**
```
Override format to center the level name.

Args:
    record (logging.LogRecord): The log record.

Returns:
    formated record (str): The formatted log record.
```

**Parameters:**
- `self`
- `record`

**Returns:** `str`

---

## **`set_trace`**

**Docstring:**
```
Sets Trace state.
```

**Parameters:**
- `self`
- `on`: `bool`

**Returns:** `None specified`

---

## **`_configure_handlers`**

**Parameters:**
- `self`
- `config`

**Returns:** `list[stdlogging.Handler]`

---

## **`get_config`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`set_config`**

**Docstring:**
```
Set config after initialization, if desired.
```

**Parameters:**
- `self`
- `config`

**Returns:** `None specified`

---

## **`_create_and_start_listener`**

**Docstring:**
```
A listener to receive and publish log records.

This listener receives records from a queue populated by the main bittensor logger, as well as 3rd party loggers
```

**Parameters:**
- `self`
- `handlers`

**Returns:** `None specified`

---

## **`get_queue`**

**Docstring:**
```
Get the queue the QueueListener is publishing from.

To set up logging in a separate process, a QueueHandler must be added to all the desired loggers.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`_initialize_bt_logger`**

**Docstring:**
```
Initialize logging for bittensor.

Since the initial state is Default, logging level for the module logger is INFO, and all third-party loggers are
silenced. Subsequent state transitions will handle all logger outputs.
```

**Parameters:**
- `self`
- `name`

**Returns:** `None specified`

---

## **`_deinitialize_bt_logger`**

**Docstring:**
```
Find the logger by name and remove the queue handler associated with it.
```

**Parameters:**
- `self`
- `name`

**Returns:** `None specified`

---

## **`_create_file_handler`**

**Parameters:**
- `self`
- `logfile`: `str`

**Returns:** `None specified`

---

## **`register_primary_logger`**

**Docstring:**
```
Register a logger as primary logger

This adds a logger to the _primary_loggers set to ensure
it doesn't get disabled when disabling third-party loggers.
A queue handler is also associated with it.
```

**Parameters:**
- `self`
- `name`: `str`

**Returns:** `None specified`

---

## **`deregister_primary_logger`**

**Docstring:**
```
De-registers a primary logger

This function removes the logger from the _primary_loggers
set and deinitializes its queue handler
```

**Parameters:**
- `self`
- `name`: `str`

**Returns:** `None specified`

---

## **`enable_third_party_loggers`**

**Docstring:**
```
Enables logging for third-party loggers by adding a queue handler to each.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`disable_third_party_loggers`**

**Docstring:**
```
Disables logging for third-party loggers by removing all their handlers.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`_enable_file_logging`**

**Parameters:**
- `self`
- `logfile`: `str`

**Returns:** `None specified`

---

## **`before_transition`**

**Docstring:**
```
Stops listener after transition.
```

**Parameters:**
- `self`
- `event`
- `state`

**Returns:** `None specified`

---

## **`after_transition`**

**Docstring:**
```
Starts listener after transition.
```

**Parameters:**
- `self`
- `event`
- `state`

**Returns:** `None specified`

---

## **`before_enable_default`**

**Docstring:**
```
Logs status before enable Default.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`after_enable_default`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`before_enable_trace`**

**Docstring:**
```
Logs status before enable Trace.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`after_enable_trace`**

**Docstring:**
```
Logs status after enable Trace.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`before_disable_trace`**

**Docstring:**
```
Logs status before disable Trace.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`after_disable_trace`**

**Docstring:**
```
Logs status after disable Trace.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`before_enable_debug`**

**Docstring:**
```
Logs status before enable Debug.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`after_enable_debug`**

**Docstring:**
```
Logs status after enable Debug.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`before_disable_debug`**

**Docstring:**
```
Logs status before disable Debug.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`after_disable_debug`**

**Docstring:**
```
Logs status after disable Debug.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`before_disable_logging`**

**Docstring:**
```
Prepares the logging system for disabling.

This method performs the following actions:
1. Logs an informational message indicating that logging is being disabled.
2. Disables trace mode in the stream formatter.
3. Sets the logging level to CRITICAL for all loggers.

This ensures that only critical messages will be logged after this method is called.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__trace_on__`**

**Docstring:**
```
Checks if the current state is in "Trace" mode.

Returns:
    bool: True if the current state is "Trace", otherwise False.
```

**Parameters:**
- `self`

**Returns:** `bool`

---

## **`success`**

**Docstring:**
```
Wraps success message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`warning`**

**Docstring:**
```
Wraps warning message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`critical`**

**Docstring:**
```
Wraps critical message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`exception`**

**Docstring:**
```
Wraps exception message with prefix and suffix.
```

**Parameters:**
- `self`
- `msg`
- `prefix`
- `suffix`

**Returns:** `None specified`

---

## **`on`**

**Docstring:**
```
Enable default state.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`off`**

**Docstring:**
```
Disables all states.
```

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`set_debug`**

**Docstring:**
```
Sets Debug state.
```

**Parameters:**
- `self`
- `on`: `bool`

**Returns:** `None specified`

---

## **`get_level`**

**Docstring:**
```
Returns Logging level.
```

**Parameters:**
- `self`

**Returns:** `int`

---

## **`__call__`**

**Parameters:**
- `self`
- `config`: `bittensor.config`
- `debug`: `bool`
- `trace`: `bool`
- `record_log`: `bool`
- `logging_dir`: `str`

**Returns:** `None specified`

---

## **`__setitem__`**

**Parameters:**
- `self`
- `key`
- `value`

**Returns:** `None specified`

---

## **`__iter__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`__len__`**

**Parameters:**
- `self`

**Returns:** `None specified`

---

## **`reset`**

**Parameters:**
- `cls`

**Returns:** `None`

---

## **`setup`**

**Parameters:**
- `self`

**Returns:** `None`

---

## **`create_subnet`**

**Parameters:**
- `self`
- `netuid`: `int`

**Returns:** `None`

---

## **`set_difficulty`**

**Parameters:**
- `self`
- `netuid`: `int`
- `difficulty`: `int`

**Returns:** `None`

---

## **`_register_neuron`**

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey`: `str`
- `coldkey`: `str`

**Returns:** `int`

---

## **`_convert_to_balance`**

**Parameters:**
- `balance`: `Union['Balance', float, int]`

**Returns:** `'Balance'`

---

## **`force_register_neuron`**

**Docstring:**
```
Force register a neuron on the mock chain, returning the UID.
```

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey`: `str`
- `coldkey`: `str`
- `stake`: `Union['Balance', float, int]`
- `balance`: `Union['Balance', float, int]`

**Returns:** `int`

---

## **`force_set_balance`**

**Docstring:**
```
Returns:
    Tuple[bool, Optional[str]]: (success, err_msg)
```

**Parameters:**
- `self`
- `ss58_address`: `str`
- `balance`: `Union['Balance', float, int]`

**Returns:** `Tuple[bool, Optional[str]]`

---

## **`do_block_step`**

**Parameters:**
- `self`

**Returns:** `None`

---

## **`_handle_type_default`**

**Parameters:**
- `self`
- `name`: `str`
- `params`: `List[object]`

**Returns:** `object`

---

## **`_get_most_recent_storage`**

**Parameters:**
- `storage`: `Dict[BlockNumber, Any]`
- `block_number`: `Optional[int]`

**Returns:** `Any`

---

## **`_get_axon_info`**

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey`: `str`
- `block`: `Optional[int]`

**Returns:** `AxonInfoDict`

---

## **`_get_prometheus_info`**

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey`: `str`
- `block`: `Optional[int]`

**Returns:** `PrometheusInfoDict`

---

## **`_neuron_subnet_exists`**

**Parameters:**
- `self`
- `uid`: `int`
- `netuid`: `int`
- `block`: `Optional[int]`

**Returns:** `Optional[NeuronInfo]`

---

## **`min_required_stake`**

**Docstring:**
```
As the minimum required stake may change, this method allows us to dynamically
update the amount in the mock without updating the tests
```

**Parameters:**
None

**Returns:** `None specified`

---

## **`query_subnet_info`**

**Parameters:**
- `name`: `str`

**Returns:** `Optional[object]`

---

## **`get_mock_wallet`**

**Parameters:**
- `coldkey`: `'bittensor.Keypair'`
- `hotkey`: `'bittensor.Keypair'`

**Returns:** `None specified`

---

## **`get_mock_keypair`**

**Docstring:**
```
Returns a mock keypair from a uid and optional test_name.
If test_name is not provided, the uid is the only seed.
If test_name is provided, the uid is hashed with the test_name to create a unique seed for the test.
```

**Parameters:**
- `uid`: `int`
- `test_name`: `Optional[str]`

**Returns:** `bittensor.Keypair`

---

## **`get_mock_hotkey`**

**Parameters:**
- `uid`: `int`

**Returns:** `str`

---

## **`get_mock_coldkey`**

**Parameters:**
- `uid`: `int`

**Returns:** `str`

---

## **`check_netuid_set`**

**Parameters:**
- `config`: `'bittensor.config'`
- `subtensor`: `'bittensor.subtensor'`
- `allow_none`: `bool`

**Returns:** `None specified`

---

## **`check_for_cuda_reg_config`**

**Docstring:**
```
Checks, when CUDA is available, if the user would like to register with their CUDA device.
```

**Parameters:**
- `config`: `'bittensor.config'`

**Returns:** `None`

---

## **`get_hotkey_wallets_for_wallet`**

**Parameters:**
- `wallet`

**Returns:** `List['bittensor.wallet']`

---

## **`get_coldkey_wallets_for_path`**

**Parameters:**
- `path`: `str`

**Returns:** `List['bittensor.wallet']`

---

## **`get_all_wallets_for_path`**

**Parameters:**
- `path`: `str`

**Returns:** `List['bittensor.wallet']`

---

## **`filter_netuids_by_registered_hotkeys`**

**Parameters:**
- `cli`
- `subtensor`
- `netuids`
- `all_hotkeys`

**Returns:** `List[int]`

---

## **`normalize_hyperparameters`**

**Docstring:**
```
Normalizes the hyperparameters of a subnet.

Args:
    subnet: The subnet hyperparameters object.

Returns:
    A list of tuples containing the parameter name, value, and normalized value.
```

**Parameters:**
- `subnet`: `bittensor.SubnetHyperparameters`

**Returns:** `List[Tuple[str, str, str]]`

---

## **`_get_delegates_details_from_github`**

**Parameters:**
- `requests_get`
- `url`: `str`

**Returns:** `Dict[str, DelegatesDetails]`

---

## **`get_delegates_details`**

**Parameters:**
- `url`: `str`

**Returns:** `Optional[Dict[str, DelegatesDetails]]`

---

## **`check_choice`**

**Parameters:**
- `self`
- `value`: `str`

**Returns:** `bool`

---

## **`from_json`**

**Parameters:**
- `cls`
- `json`: `Dict[str, any]`

**Returns:** `'DelegatesDetails'`

---

## **`_run`**

**Parameters:**
- `cli`: `'bittensor.cli'`
- `subtensor`: `'bittensor.subtensor'`

**Returns:** `None specified`

---

## **`_get_total_balance`**

**Parameters:**
- `total_balance`: `'bittensor.Balance'`
- `subtensor`: `'bittensor.subtensor'`
- `cli`: `'bittensor.cli'`

**Returns:** `Tuple[List['bittensor.wallet'], 'bittensor.Balance']`

---

## **`_get_hotkeys`**

**Parameters:**
- `cli`: `'bittensor.cli'`
- `all_hotkeys`: `List['bittensor.wallet']`

**Returns:** `List['bittensor.wallet']`

---

## **`_get_key_address`**

**Parameters:**
- `all_hotkeys`: `List['bittensor.wallet']`

**Returns:** `None specified`

---

## **`_process_neuron_results`**

**Parameters:**
- `results`: `List[Tuple[int, List['bittensor.NeuronInfoLite'], Optional[str]]]`
- `neurons`: `Dict[str, List['bittensor.NeuronInfoLite']]`
- `netuids`: `List[int]`

**Returns:** `Dict[str, List['bittensor.NeuronInfoLite']]`

---

## **`_get_neurons_for_netuid`**

**Parameters:**
- `args_tuple`: `Tuple['bittensor.Config', int, List[str]]`

**Returns:** `Tuple[int, List['bittensor.NeuronInfoLite'], Optional[str]]`

---

## **`_get_de_registered_stake_for_coldkey_wallet`**

**Parameters:**
- `args_tuple`

**Returns:** `Tuple['bittensor.Wallet', List[Tuple[str, 'bittensor.Balance']], Optional[str]]`

---

## **`_filter_stake_info`**

**Parameters:**
- `stake_info`: `'bittensor.StakeInfo'`

**Returns:** `bool`

---

## **`overview_sort_function`**

**Parameters:**
- `row`

**Returns:** `None specified`

---

## **`_get_coldkey_wallets_for_path`**

**Parameters:**
- `path`: `str`

**Returns:** `List['bittensor.wallet']`

---

## **`show_delegates_lite`**

**Docstring:**
```
This method is a lite version of the :func:`show_delegates`. This method displays a formatted table of Bittensor network delegates with detailed statistics to the console.

The table is sorted by total stake in descending order and provides
a snapshot of delegate performance and status, helping users make informed decisions for staking or nominating.

This helper function is not intended to be used directly in user code unless specifically required.

Args:
    delegates_lite (List[bittensor.DelegateInfoLite]): A list of delegate information objects to be displayed.
    width (Optional[int]): The width of the console output table. Defaults to ``None``, which will make the table expand to the maximum width of the console.

The output table contains the following columns. To display more columns, use the :func:`show_delegates` function.

- INDEX: The numerical index of the delegate.
- DELEGATE: The name of the delegate.
- SS58: The truncated SS58 address of the delegate.
- NOMINATORS: The number of nominators supporting the delegate.
- VPERMIT: Validator permits held by the delegate for the subnets.
- TAKE: The percentage of the delegate's earnings taken by the network.
- DELEGATE/(24h): The earnings of the delegate in the last 24 hours.
- Desc: A brief description provided by the delegate.

Usage:
    This function is typically used within the Bittensor CLI to show current delegate options to users who are considering where to stake their tokens.

Example usage::

    show_delegates_lite(delegates_lite, width=80)

Note:
    This function is primarily for display purposes within a command-line interface and does not return any values. It relies on the `rich <https://github.com/Textualize/rich>`_ Python library to render
    the table in the console.
```

**Parameters:**
- `delegates_lite`: `List['bittensor.DelegateInfoLite']`
- `width`: `Optional[int]`

**Returns:** `None specified`

---

## **`show_delegates`**

**Docstring:**
```
Displays a formatted table of Bittensor network delegates with detailed statistics to the console.

The table is sorted by total stake in descending order and provides
a snapshot of delegate performance and status, helping users make informed decisions for staking or nominating.

This is a helper function that is called by the :func:`list_delegates` and :func:`my_delegates`, and is not intended
to be used directly in user code unless specifically required.

Args:
    delegates (List[bittensor.DelegateInfo]): A list of delegate information objects to be displayed.
    prev_delegates (Optional[List[bittensor.DelegateInfo]]): A list of delegate information objects from a previous state, used to calculate changes in stake. Defaults to ``None``.
    width (Optional[int]): The width of the console output table. Defaults to ``None``, which will make the table expand to the maximum width of the console.

The output table contains the following columns:

- INDEX: The numerical index of the delegate.
- DELEGATE: The name of the delegate.
- SS58: The truncated SS58 address of the delegate.
- NOMINATORS: The number of nominators supporting the delegate.
- DELEGATE STAKE(τ): The stake that is directly delegated to the delegate.
- TOTAL STAKE(τ): The total stake held by the delegate, including nominators' stake.
- CHANGE/(4h): The percentage change in the delegate's stake over the past 4 hours.
- VPERMIT: Validator permits held by the delegate for the subnets.
- TAKE: The percentage of the delegate's earnings taken by the network.
- NOMINATOR/(24h)/kτ: The earnings per 1000 τ staked by nominators in the last 24 hours.
- DELEGATE/(24h): The earnings of the delegate in the last 24 hours.
- Desc: A brief description provided by the delegate.

Usage:
    This function is typically used within the Bittensor CLI to show current delegate options to users who are considering where to stake their tokens.

Example usage::

    show_delegates(current_delegates, previous_delegates, width=80)

Note:
    This function is primarily for display purposes within a command-line interface and does
    not return any values. It relies on the `rich <https://github.com/Textualize/rich>`_ Python library to render
    the table in the
    console.
```

**Parameters:**
- `delegates`: `List['bittensor.DelegateInfo']`
- `prev_delegates`: `Optional[List['bittensor.DelegateInfo']]`
- `width`: `Optional[int]`

**Returns:** `None specified`

---

## **`fetch_arbitration_stats`**

**Docstring:**
```
Performs a check of the current arbitration data (if any), and displays it through the bittensor console.
```

**Parameters:**
- `subtensor`
- `wallet`

**Returns:** `None specified`

---

## **`allowed_value`**

**Docstring:**
```
Check the allowed values on hyperparameters. Return False if value is out of bounds.
```

**Parameters:**
- `param`: `str`
- `value`: `Union[str, bool, float]`

**Returns:** `Tuple[bool, Union[str, list[float], float]]`

---

## **`_get_coldkey_ss58_addresses_for_path`**

**Docstring:**
```
Get all coldkey ss58 addresses from path.
```

**Parameters:**
- `path`: `str`

**Returns:** `Tuple[List[str], List[str]]`

---

## **`get_wallet_transfers`**

**Docstring:**
```
Get all transfers associated with the provided wallet address.
```

**Parameters:**
- `wallet_address`

**Returns:** `List[dict]`

---

## **`create_transfer_history_table`**

**Docstring:**
```
Get output transfer table
```

**Parameters:**
- `transfers`

**Returns:** `None specified`

---

## **`list_coldkeypub_files`**

**Parameters:**
- `dir_path`

**Returns:** `None specified`

---

## **`_get_hotkey_wallets_for_wallet`**

**Parameters:**
- `wallet`

**Returns:** `List['bittensor.wallet']`

---

## **`format_call_data`**

**Parameters:**
- `call_data`: `'bittensor.ProposalCallData'`

**Returns:** `str`

---

## **`display_votes`**

**Parameters:**
- `vote_data`: `'bittensor.ProposalVoteData'`
- `delegate_info`: `'bittensor.DelegateInfo'`

**Returns:** `str`

---

## **`get_stake_accounts`**

**Docstring:**
```
Get stake account details for the given wallet.

Args:
    wallet: The wallet object to fetch the stake account details for.

Returns:
    A dictionary mapping SS58 addresses to their respective stake account details.
```

**Parameters:**
- `wallet`
- `subtensor`

**Returns:** `Dict[str, Dict[str, Union[str, Balance]]]`

---

## **`get_stakes_from_hotkeys`**

**Docstring:**
```
Fetch stakes from hotkeys for the provided wallet.

Args:
    wallet: The wallet object to fetch the stakes for.

Returns:
    A dictionary of stakes related to hotkeys.
```

**Parameters:**
- `subtensor`
- `wallet`

**Returns:** `Dict[str, Dict[str, Union[str, Balance]]]`

---

## **`get_stakes_from_delegates`**

**Docstring:**
```
Fetch stakes from delegates for the provided wallet.

Args:
    wallet: The wallet object to fetch the stakes for.

Returns:
    A dictionary of stakes related to delegates.
```

**Parameters:**
- `subtensor`
- `wallet`

**Returns:** `Dict[str, Dict[str, Union[str, Balance]]]`

---

## **`get_all_wallet_accounts`**

**Docstring:**
```
Fetch stake accounts for all provided wallets using a ThreadPool.

Args:
    wallets: List of wallets to fetch the stake accounts for.

Returns:
    A list of dictionaries, each dictionary containing stake account details for each wallet.
```

**Parameters:**
- `wallets`
- `subtensor`

**Returns:** `List[Dict[str, Dict[str, Union[str, Balance]]]]`

---

## **`transfer_extrinsic`**

**Docstring:**
```
Transfers funds from this wallet to the destination public key address.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object to make transfer from.
    dest (str, ss58_address or ed25519):
        Destination public key address of reciever.
    amount (Union[Balance, int]):
        Amount to stake as Bittensor balance, or ``float`` interpreted as Tao.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    keep_alive (bool):
        If set, keeps the account alive by keeping the balance above the existential deposit.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `dest`: `str`
- `amount`: `Union[Balance, float]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `keep_alive`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`commit_weights_extrinsic`**

**Docstring:**
```
Commits a hash of the neuron's weights to the Bittensor blockchain using the provided wallet.
This function is a wrapper around the `_do_commit_weights` method, handling user prompts and error messages.
Args:
    subtensor (bittensor.subtensor): The subtensor instance used for blockchain interaction.
    wallet (bittensor.wallet): The wallet associated with the neuron committing the weights.
    netuid (int): The unique identifier of the subnet.
    commit_hash (str): The hash of the neuron's weights to be committed.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
Returns:
    Tuple[bool, str]: ``True`` if the weight commitment is successful, False otherwise. And `msg`, a string
    value describing the success or potential error.
This function provides a user-friendly interface for committing weights to the Bittensor blockchain, ensuring proper
error handling and user interaction when required.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `commit_hash`: `str`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `Tuple[bool, str]`

---

## **`reveal_weights_extrinsic`**

**Docstring:**
```
Reveals the weights for a specific subnet on the Bittensor blockchain using the provided wallet.
This function is a wrapper around the `_do_reveal_weights` method, handling user prompts and error messages.
Args:
    subtensor (bittensor.subtensor): The subtensor instance used for blockchain interaction.
    wallet (bittensor.wallet): The wallet associated with the neuron revealing the weights.
    netuid (int): The unique identifier of the subnet.
    uids (List[int]): List of neuron UIDs for which weights are being revealed.
    weights (List[int]): List of weight values corresponding to each UID.
    salt (List[int]): List of salt values corresponding to the hash function.
    version_key (int): Version key for compatibility with the network.
    wait_for_inclusion (bool, optional): Waits for the transaction to be included in a block.
    wait_for_finalization (bool, optional): Waits for the transaction to be finalized on the blockchain.
    prompt (bool, optional): If ``True``, prompts for user confirmation before proceeding.
Returns:
    Tuple[bool, str]: ``True`` if the weight revelation is successful, False otherwise. And `msg`, a string
    value describing the success or potential error.
This function provides a user-friendly interface for revealing weights on the Bittensor blockchain, ensuring proper
error handling and user interaction when required.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `uids`: `List[int]`
- `weights`: `List[int]`
- `salt`: `List[int]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `Tuple[bool, str]`

---

## **`_check_threshold_amount`**

**Docstring:**
```
Checks if the new stake balance will be above the minimum required stake threshold.

Args:
    stake_balance (Balance):
        the balance to check for threshold limits.

Returns:
    success, threshold (bool, Balance):
        ``true`` if the staking balance is above the threshold, or ``false`` if the
            staking balance is below the threshold.
        The threshold balance required to stake.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `stake_balance`: `Balance`

**Returns:** `Tuple[bool, Balance]`

---

## **`add_stake_extrinsic`**

**Docstring:**
```
Adds the specified amount of stake to passed hotkey ``uid``.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    hotkey_ss58 (Optional[str]):
        The ``ss58`` address of the hotkey account to stake to defaults to the wallet's hotkey.
    amount (Union[Balance, float]):
        Amount to stake as Bittensor balance, or ``float`` interpreted as Tao.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.

Raises:
    bittensor.errors.NotRegisteredError:
        If the wallet is not registered on the chain.
    bittensor.errors.NotDelegateError:
        If the hotkey is not a delegate on the chain.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `Optional[str]`
- `amount`: `Optional[Union[Balance, float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`add_stake_multiple_extrinsic`**

**Docstring:**
```
Adds stake to each ``hotkey_ss58`` in the list, using each amount, from a common coldkey.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object for the coldkey.
    hotkey_ss58s (List[str]):
        List of hotkeys to stake to.
    amounts (List[Union[Balance, float]]):
        List of amounts to stake. If ``None``, stake all to the first hotkey.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block. Flag is ``true`` if any wallet was staked. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58s`: `List[str]`
- `amounts`: `Optional[List[Union[Balance, float]]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`__do_add_stake_single`**

**Docstring:**
```
Executes a stake call to the chain using the wallet and the amount specified.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    hotkey_ss58 (str):
        Hotkey to stake to.
    amount (bittensor.Balance):
        Amount to stake as Bittensor balance object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
Raises:
    bittensor.errors.StakeError:
        If the extrinsic fails to be finalized or included in the block.
    bittensor.errors.NotDelegateError:
        If the hotkey is not a delegate.
    bittensor.errors.NotRegisteredError:
        If the hotkey is not registered in any subnets.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `str`
- `amount`: `'bittensor.Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`__do_remove_stake_single`**

**Docstring:**
```
Executes an unstake call to the chain using the wallet and the amount specified.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    hotkey_ss58 (str):
        Hotkey address to unstake from.
    amount (bittensor.Balance):
        Amount to unstake as Bittensor balance object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
Raises:
    bittensor.errors.StakeError:
        If the extrinsic fails to be finalized or included in the block.
    bittensor.errors.NotRegisteredError:
        If the hotkey is not registered in any subnets.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `str`
- `amount`: `'bittensor.Balance'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`check_threshold_amount`**

**Docstring:**
```
Checks if the remaining stake balance is above the minimum required stake threshold.

Args:
    stake_balance (Balance):
        the balance to check for threshold limits.

Returns:
    success (bool):
        ``true`` if the unstaking is above the threshold or 0, or ``false`` if the
            unstaking is below the threshold, but not 0.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `stake_balance`: `Balance`

**Returns:** `bool`

---

## **`unstake_extrinsic`**

**Docstring:**
```
Removes stake into the wallet coldkey from the specified hotkey ``uid``.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    hotkey_ss58 (Optional[str]):
        The ``ss58`` address of the hotkey to unstake from. By default, the wallet hotkey is used.
    amount (Union[Balance, float]):
        Amount to stake as Bittensor balance, or ``float`` interpreted as Tao.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `Optional[str]`
- `amount`: `Optional[Union[Balance, float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`unstake_multiple_extrinsic`**

**Docstring:**
```
Removes stake from each ``hotkey_ss58`` in the list, using each amount, to a common coldkey.

Args:
    wallet (bittensor.wallet):
        The wallet with the coldkey to unstake to.
    hotkey_ss58s (List[str]):
        List of hotkeys to unstake from.
    amounts (List[Union[Balance, float]]):
        List of amounts to unstake. If ``None``, unstake all.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block. Flag is ``true`` if any wallet was unstaked. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58s`: `List[str]`
- `amounts`: `Optional[List[Union[Balance, float]]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`register_extrinsic`**

**Docstring:**
```
Registers the wallet to the chain.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    netuid (int):
        The ``netuid`` of the subnet to register on.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
    max_allowed_attempts (int):
        Maximum number of attempts to register the wallet.
    cuda (bool):
        If ``true``, the wallet should be registered using CUDA device(s).
    dev_id (Union[List[int], int]):
        The CUDA device id to use, or a list of device ids.
    tpb (int):
        The number of threads per block (CUDA).
    num_processes (int):
        The number of processes to use to register.
    update_interval (int):
        The number of nonces to solve between updates.
    log_verbose (bool):
        If ``true``, the registration process will log more information.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_allowed_attempts`: `int`
- `output_in_place`: `bool`
- `cuda`: `bool`
- `dev_id`: `Union[List[int], int]`
- `tpb`: `int`
- `num_processes`: `Optional[int]`
- `update_interval`: `Optional[int]`
- `log_verbose`: `bool`

**Returns:** `bool`

---

## **`burned_register_extrinsic`**

**Docstring:**
```
Registers the wallet to chain by recycling TAO.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    netuid (int):
        The ``netuid`` of the subnet to register on.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`run_faucet_extrinsic`**

**Docstring:**
```
Runs a continual POW to get a faucet of TAO on the test net.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    max_allowed_attempts (int):
        Maximum number of attempts to register the wallet.
    cuda (bool):
        If ``true``, the wallet should be registered using CUDA device(s).
    dev_id (Union[List[int], int]):
        The CUDA device id to use, or a list of device ids.
    tpb (int):
        The number of threads per block (CUDA).
    num_processes (int):
        The number of processes to use to register.
    update_interval (int):
        The number of nonces to solve between updates.
    log_verbose (bool):
        If ``true``, the registration process will log more information.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`
- `max_allowed_attempts`: `int`
- `output_in_place`: `bool`
- `cuda`: `bool`
- `dev_id`: `Union[List[int], int]`
- `tpb`: `int`
- `num_processes`: `Optional[int]`
- `update_interval`: `Optional[int]`
- `log_verbose`: `bool`

**Returns:** `Tuple[bool, str]`

---

## **`swap_hotkey_extrinsic`**

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `new_wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`_find_event_attributes_in_extrinsic_receipt`**

**Docstring:**
```
Searches for the attributes of a specified event within an extrinsic receipt.

Args:
    response (substrateinterface.base.ExtrinsicReceipt): The receipt of the extrinsic to be searched.
    event_name (str): The name of the event to search for.

Returns:
    list: A list of attributes for the specified event. Returns [-1] if the event is not found.
```

**Parameters:**
- `response`: `'substrateinterface.base.ExtrinsicReceipt'`
- `event_name`: `str`

**Returns:** `list`

---

## **`register_subnetwork_extrinsic`**

**Docstring:**
```
Registers a new subnetwork.

Args:
    wallet (bittensor.wallet):
        bittensor wallet object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If true, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block.
        If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`set_hyperparameter_extrinsic`**

**Docstring:**
```
Sets a hyperparameter for a specific subnetwork.

Args:
    wallet (bittensor.wallet):
        bittensor wallet object.
    netuid (int):
        Subnetwork ``uid``.
    parameter (str):
        Hyperparameter name.
    value (any):
        New hyperparameter value.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block.
        If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `parameter`: `str`
- `value`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`serve_extrinsic`**

**Docstring:**
```
Subscribes a Bittensor endpoint to the subtensor chain.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    ip (str):
        Endpoint host port i.e., ``192.122.31.4``.
    port (int):
        Endpoint port number i.e., ``9221``.
    protocol (int):
        An ``int`` representation of the protocol.
    netuid (int):
        The network uid to serve on.
    placeholder1 (int):
        A placeholder for future use.
    placeholder2 (int):
        A placeholder for future use.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `ip`: `str`
- `port`: `int`
- `protocol`: `int`
- `netuid`: `int`
- `placeholder1`: `int`
- `placeholder2`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`serve_axon_extrinsic`**

**Docstring:**
```
Serves the axon to the network.

Args:
    netuid ( int ):
        The ``netuid`` being served on.
    axon (bittensor.Axon):
        Axon to serve.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `netuid`: `int`
- `axon`: `'bittensor.Axon'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`publish_metadata`**

**Docstring:**
```
Publishes metadata on the Bittensor network using the specified wallet and network identifier.

Args:
    subtensor (bittensor.subtensor):
        The subtensor instance representing the Bittensor blockchain connection.
    wallet (bittensor.wallet):
        The wallet object used for authentication in the transaction.
    netuid (int):
        Network UID on which the metadata is to be published.
    data_type (str):
        The data type of the information being submitted. It should be one of the following: ``'Sha256'``, ``'Blake256'``, ``'Keccak256'``, or ``'Raw0-128'``. This specifies the format or hashing algorithm used for the data.
    data (str):
        The actual metadata content to be published. This should be formatted or hashed according to the ``type`` specified. (Note: max ``str`` length is 128 bytes)
    wait_for_inclusion (bool, optional):
        If ``True``, the function will wait for the extrinsic to be included in a block before returning. Defaults to ``False``.
    wait_for_finalization (bool, optional):
        If ``True``, the function will wait for the extrinsic to be finalized on the chain before returning. Defaults to ``True``.

Returns:
    bool:
        ``True`` if the metadata was successfully published (and finalized if specified). ``False`` otherwise.

Raises:
    MetadataError:
        If there is an error in submitting the extrinsic or if the response from the blockchain indicates failure.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `data_type`: `str`
- `data`: `bytes`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`

**Returns:** `bool`

---

## **`get_metadata`**

**Parameters:**
- `self`
- `netuid`: `int`
- `hotkey`: `str`
- `block`: `Optional[int]`

**Returns:** `str`

---

## **`register_senate_extrinsic`**

**Docstring:**
```
Registers the wallet to chain for senate voting.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`leave_senate_extrinsic`**

**Docstring:**
```
Removes the wallet from chain for senate voting.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`vote_senate_extrinsic`**

**Docstring:**
```
Votes ayes or nays on proposals.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or included in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `proposal_hash`: `str`
- `proposal_idx`: `int`
- `vote`: `bool`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`prometheus_extrinsic`**

**Docstring:**
```
Subscribes an Bittensor endpoint to the substensor chain.

Args:
    subtensor (bittensor.subtensor):
        Bittensor subtensor object.
    wallet (bittensor.wallet):
        Bittensor wallet object.
    ip (str):
        Endpoint host port i.e., ``192.122.31.4``.
    port (int):
        Endpoint port number i.e., `9221`.
    netuid (int):
        Network `uid` to serve on.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block.
        If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `port`: `int`
- `netuid`: `int`
- `ip`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`

**Returns:** `bool`

---

## **`set_weights_extrinsic`**

**Docstring:**
```
Sets the given weights and values on chain for wallet hotkey account.

Args:
    subtensor (bittensor.subtensor):
        Subtensor endpoint to use.
    wallet (bittensor.wallet):
        Bittensor wallet object.
    netuid (int):
        The ``netuid`` of the subnet to set weights for.
    uids (Union[NDArray[np.int64], torch.LongTensor, list]):
        The ``uint64`` uids of destination neurons.
    weights (Union[NDArray[np.float32], torch.FloatTensor, list]):
        The weights to set. These must be ``float`` s and correspond to the passed ``uid`` s.
    version_key (int):
        The version key of the validator.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuid`: `int`
- `uids`: `Union[NDArray[np.int64], 'torch.LongTensor', list]`
- `weights`: `Union[NDArray[np.float32], 'torch.FloatTensor', list]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `Tuple[bool, str]`

---

## **`nominate_extrinsic`**

**Docstring:**
```
Becomes a delegate for the hotkey.

Args:
    wallet (bittensor.wallet): The wallet to become a delegate for.
Returns:
    success (bool): ``True`` if the transaction was successful.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `wait_for_finalization`: `bool`
- `wait_for_inclusion`: `bool`

**Returns:** `bool`

---

## **`delegate_extrinsic`**

**Docstring:**
```
Delegates the specified amount of stake to the passed delegate.

Args:
    wallet (bittensor.wallet): Bittensor wallet object.
    delegate_ss58 (Optional[str]): The ``ss58`` address of the delegate.
    amount (Union[Balance, float]): Amount to stake as bittensor balance, or ``float`` interpreted as Tao.
    wait_for_inclusion (bool): If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool): If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool): If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool): Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.

Raises:
    NotRegisteredError: If the wallet is not registered on the chain.
    NotDelegateError: If the hotkey is not a delegate on the chain.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `delegate_ss58`: `Optional[str]`
- `amount`: `Optional[Union[Balance, float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`undelegate_extrinsic`**

**Docstring:**
```
Un-delegates stake from the passed delegate.

Args:
    wallet (bittensor.wallet): Bittensor wallet object.
    delegate_ss58 (Optional[str]): The ``ss58`` address of the delegate.
    amount (Union[Balance, float]): Amount to unstake as bittensor balance, or ``float`` interpreted as Tao.
    wait_for_inclusion (bool): If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool): If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool): If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool): Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.

Raises:
    NotRegisteredError: If the wallet is not registered on the chain.
    NotDelegateError: If the hotkey is not a delegate on the chain.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `delegate_ss58`: `Optional[str]`
- `amount`: `Optional[Union[Balance, float]]`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`decrease_take_extrinsic`**

**Docstring:**
```
Decrease delegate take for the hotkey.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    hotkey_ss58 (Optional[str]):
        The ``ss58`` address of the hotkey account to stake to defaults to the wallet's hotkey.
    take (float):
        The ``take`` of the hotkey.
Returns:
    success (bool): ``True`` if the transaction was successful.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `Optional[str]`
- `take`: `int`
- `wait_for_finalization`: `bool`
- `wait_for_inclusion`: `bool`

**Returns:** `bool`

---

## **`increase_take_extrinsic`**

**Docstring:**
```
Increase delegate take for the hotkey.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    hotkey_ss58 (Optional[str]):
        The ``ss58`` address of the hotkey account to stake to defaults to the wallet's hotkey.
    take (float):
        The ``take`` of the hotkey.
Returns:
    success (bool): ``True`` if the transaction was successful.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `hotkey_ss58`: `Optional[str]`
- `take`: `int`
- `wait_for_finalization`: `bool`
- `wait_for_inclusion`: `bool`

**Returns:** `bool`

---

## **`root_register_extrinsic`**

**Docstring:**
```
Registers the wallet to root network.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

## **`set_root_weights_extrinsic`**

**Docstring:**
```
Sets the given weights and values on chain for wallet hotkey account.

Args:
    wallet (bittensor.wallet):
        Bittensor wallet object.
    netuids (Union[NDArray[np.int64], torch.LongTensor, List[int]]):
        The ``netuid`` of the subnet to set weights for.
    weights (Union[NDArray[np.float32], torch.FloatTensor, list]):
        Weights to set. These must be ``float`` s and must correspond to the passed ``netuid`` s.
    version_key (int):
        The version key of the validator.
    wait_for_inclusion (bool):
        If set, waits for the extrinsic to enter a block before returning ``true``, or returns ``false`` if the extrinsic fails to enter the block within the timeout.
    wait_for_finalization (bool):
        If set, waits for the extrinsic to be finalized on the chain before returning ``true``, or returns ``false`` if the extrinsic fails to be finalized within the timeout.
    prompt (bool):
        If ``true``, the call waits for confirmation from the user before proceeding.
Returns:
    success (bool):
        Flag is ``true`` if extrinsic was finalized or uncluded in the block. If we did not wait for finalization / inclusion, the response is ``true``.
```

**Parameters:**
- `subtensor`: `'bittensor.subtensor'`
- `wallet`: `'bittensor.wallet'`
- `netuids`: `Union[NDArray[np.int64], 'torch.LongTensor', List[int]]`
- `weights`: `Union[NDArray[np.float32], 'torch.FloatTensor', List[float]]`
- `version_key`: `int`
- `wait_for_inclusion`: `bool`
- `wait_for_finalization`: `bool`
- `prompt`: `bool`

**Returns:** `bool`

---

