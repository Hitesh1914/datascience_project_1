# common utities for the data science project

import os 
import yaml
from src.data_science_project_1 import logger
import json
import joblib   # for saving and loading models
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns 
    Args:
        path_to_yaml(str): path like input to the YAML file.
    Raises:
        ValueError: If the file is not found or if there is an error reading the YAML file.
        e: empty file or not in the correct format.
    Returns:
        ConfigBox: A ConfigBox object containing the content of the YAML file.
        """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty or not in the correct format.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    
    """
    for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its content as a ConfigBox.
    
    Args:
        path (Path): Path to the JSON file.
    
    Returns:
        ConfigBox: Content of the JSON file as a ConfigBox object    
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)

    logger.info(f"JSON file loaded successfully: {path} loaded successfully.")
    return ConfigBox(content)

@ensure_annotations
def save_model(path: Path, model: Any):
    """Saves a model to a specified path using joblib.
    
    Args:
        path (Path): Path where the model will be saved.
        model (Any): The model to be saved.
    
    """
    joblib.dump(value=model,filename= path)
    logger.info(f"Model saved at: {path}")

@ensure_annotations
def load_model(path: Path) -> Any:
    """Loads a model from a specified path using joblib.
    
    Args:
        path (Path): Path from where the model will be loaded.
    
    Returns:
        Any: The loaded model.
    
    """
    model = joblib.load(filename=path)
    logger.info(f"Model loaded from: {path}")
    return model