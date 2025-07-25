## This module defines the configuration entity for data ingestion in a data science project.

from dataclasses import dataclass
from pathlib import Path


# dataclasses: a way to define classes that are primarily used to store data (don't have much logic and self-contained)
# classes are used to define the structure of an object
@dataclass
class DataIngestionConfig:
    # define the attributes of the class
    # Path is a class from pathlib module that represents a filesystem path (tak same as config.yaml file)
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path        #from the config yaml file 
    train_data_path: Path
    test_data_path: Path
    model_name: str    
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params :dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str