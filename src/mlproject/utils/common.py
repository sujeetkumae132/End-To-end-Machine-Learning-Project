import os
from pathlib import path
from mlproject import logger
import yaml
import typing
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import json

# read the yaml file frequently i will create a function

@ensure_annotations
def read_yaml_file(file_name) -> ConfigBox:
    
    try:
        with open(file_name) as f:
            content= yaml.safe_load(f)
            logger.info(f"yaml file: {file_name} loaded successfully")
            return content
    
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
            
            