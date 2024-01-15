import os
from box.exceptions import BoxValueError
import yaml
from cnn_Classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml files and return 

    Args:
        path_to_yaml (Path): path to input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaede successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple directories list to be created 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"jason file is saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) _COnfigBox:
    """load json file data
    
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: any, path: path):
    """save binary files

    Args:
        data (any): data to be saved as binary
        path (path): path to binary files
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file is saved: {path}")
    
@ensure_annotations
def load_bin(pack: Path) -> Any:
    """load binary data

    Args:
        pack (Path): Path to binary file

    Returns:
        Any: object sored in the file
    """
    data= joblib.load(path)
    logger.info(f"binary fiel loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of he file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

@ensure_annotations
def decode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()
        
@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())