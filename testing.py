import requests
import json
import bittensor as bt
from template.protocol import ValidatorRequest


def walk_commands():
    buff = ""
    key_dict = {}
    header = ""
    
    def walk(command_dict, key_dict, header):
        ignored = ["aliases", "help"]
        
        for key, value in command_dict.items():
            if isinstance(value, dict):
                walk(value, key_dict, header)
            else:
                if key in ignored:
                    continue
                if key == "aliases":
                    continue
                if key == "name":
                    print("")
                    print(f"{value.upper()}")
                    header = value.upper()
                    key_dict[header] = {}
                    continue
                key_dict[header][key] = value
                print(f"    {key}")
                print(f"        {value}")

    walk(bt.ALL_COMMANDS, key_dict, header)
    with open("data/commands.json", "w") as f:
        f.write(key_dict)


walk_commands()
