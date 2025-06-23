import os 
from src.data_science_project_1 import logger
import pandas as pd 

from src.data_science_project_1.entity.config_entity import DataValidationConfig # DataValidationConfig is a class that defines the data validation configuration


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config # 

    def validate_all_columns(self) -> bool: # validate_all_columns is a method that validates all the columns in the data against the schema
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir) # read the data from the unzipped directory
            logger.info("Reading data from the unzipped directory")
            all_cols = list(data.columns) # get all the columns from the data
            
            all_schema = self.config.all_schema.keys() # get all the columns from the schema
            
            for col in all_cols:
                if col not in all_schema:
                    logger.info(f"Column {col} is not in the schema")
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    logger.info("All columns are present in the schema")
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status # return the validation status
        except Exception as e:
            logger.exception(f"Exception occurred while validating all columns: {e}")
            raise e