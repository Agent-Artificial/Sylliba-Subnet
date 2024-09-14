import os
import json
import requests
from pathlib import Path
from loguru import logger
import subprocess


def get_module(module_name: str):
    with open("modules/data/module_registar.json", "r") as f:
        module_dict = json.load(f)
    module_data = module_dict[module_name]
    
    try:
        response = requests.get(f"{module_data['url']}{module_data['endpoint']}")
        logger.debug(response.status_code)
        module = f"import os\n{response.text.split('import os')[1]}"
        module = module.replace('', "")
        module = module.replace("\\n", " \n")
        module = module.replace("\\", "").strip()
        paths = module_data['path'].split("/")
        module = f"{module.split('subprocess.run(command, check=True)')[0]}\nsubprocess.run(command, check=True)"
        folder_path = Path().cwd()
        for path in paths:
            folder_path = folder_path / path / ""
            folder_path.mkdir(parents=True, exist_ok=True)
        logger.debug(folder_path)
        logger.debug(module)
        with open(f"{folder_path}/setup_{module_data['name']}.py", "w") as f:
            f.write(module)
    except Exception as e:
        logger.error(f"Failed to install module: {e}\n{folder_path}")
    return module_data
        
    
def install_module(module_name):
    command = ["python", "-m", "venv", ".venv"]
    subprocess.run(command, check=True)
    command = ["python", "-m", f"modules.{module_name}.setup_{module_name}"]
    subprocess.run(command, check=True)
    
    
def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("module_name")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    module_name = parse_args().module_name
    install_module(module_name)
    