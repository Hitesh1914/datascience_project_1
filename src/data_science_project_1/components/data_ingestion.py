# This file is part of the Data Science Project 1
# It contains the Data Ingestion component that handles downloading and extracting data from a specified source URL
import os
import urllib.request as request
from src.data_science_project_1 import logger
import zipfile

from src.data_science_project_1.entity.config_entity import (DataIngestionConfig)

### Component - Data Ingestion Configuration

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config  # config is an instance of DataIngestionConfig class that contains the data ingestion configuration

    def download_file(self):
        # Logic to download data from self.config.source_URL and save it to self.config.local_data_file
        if not os.path.exists(self.config.local_data_file):
            filename, headers =  request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file {filename} with headers {headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists. Skipping download.")

    def extract_zip_file(self):
        # Logic to extract the zip file from self.config.local_data_file to self.config.unzip_dir
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)  # Ensure the unzip directory exists

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to {unzip_path}")
