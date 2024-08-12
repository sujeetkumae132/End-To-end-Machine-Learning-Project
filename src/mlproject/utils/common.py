import os
from pathlib import Path
from mlproject import logger
import yaml
import typing
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import json
from typing import Any

# read the yaml file frequently i will create a function

@ensure_annotations
def read_yaml_file(file_name:Path) -> ConfigBox:
    
    try:
        with open(file_name) as f:
            content= yaml.safe_load(f)
            logger.info(f"yaml file: {file_name} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
# creating a function to create directory
@ensure_annotations
def create_directories(path:list,verbose=True):
    for p in path:
        os.makedirs(p,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {p}")
            
            

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)     