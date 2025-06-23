from src.data_science_project_1.config.configuration import ConfigurationManager
from src.data_science_project_1.components.data_validation import DataValidation
from src.data_science_project_1 import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def intiate_data_validation(self):

        config = ConfigurationManager() # Create an instance of ConfigurationManager to read the configuration files
        data_validation_config = config.get_data_validation_config() # Get the data ingestion configuration
        data_validation = DataValidation(config= data_validation_config) # Create an instance of DataValidation with the data validation configuration
        data_validation.validate_all_columns()

        logger.info(f"{STAGE_NAME} completed successfully.")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataValidationTrainingPipeline() # Create an instance of DataValidationTrainingPipeline
        obj.intiate_data_validation() # Start the data validation process
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e) # Log any exceptions that occur during the data validation process
        raise e # Raise the exception to stop the execution