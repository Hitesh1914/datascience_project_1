from src.data_science_project_1.constants import * # constants.py is a module that contains constants used in the project
from src.data_science_project_1.utils.common import read_yaml, create_directories
from src.data_science_project_1.entity.config_entity import (DataIngestionConfig) # DataIngestionConfig is a class that defines the data ingestion configuration

class ConfigurationManager:
    def __init__(self,
                 config_file_path= CONFIG_FILE_PATH, # CONFIG_FILE_PATH is a constant that contains the path to the config.yaml file
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(config_file_path) # read_yaml is a function that reads a YAML file and returns the data as a dictionary
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_roots]) # artifacts_root is the root directory where all the artifacts will be stored

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # data_ingestion is a key in the config dictionary that contains the data ingestion configuration
        create_directories([config.root_dir]) # create the root directory for data ingestion if it

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir, # root_dir is the directory where the data will be stored
            source_URL=config.source_URL,   # source_URL is the URL where the data can be downloaded from
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config # return an instance of DataIngestionConfig class with the data ingestion configuration
