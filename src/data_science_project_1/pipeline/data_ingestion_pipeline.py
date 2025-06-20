 
from src.data_science_project_1.config.configuration import ConfigurationManager
from src.data_science_project_1.components.data_ingestion import DataIngestion
from src.data_science_project_1 import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def intiate_data_ingestion(self):

        config = ConfigurationManager() # Create an instance of ConfigurationManager to read the configuration files
        data_ingestion_config = config.get_data_ingestion_config() # Get the data ingestion configuration
        data_ingestion = DataIngestion(config=data_ingestion_config) # Create an instance of DataIngestion with the data ingestion configuration
        data_ingestion.download_file() # Download the file from the source URL
        data_ingestion.extract_zip_file() # Extract the downloaded zip file to the specified directory
        logger.info(f"{STAGE_NAME} completed successfully.")


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline() # Create an instance of DataIngestionTrainingPipeline
        obj.intiate_data_ingestion() # Start the data ingestion process
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e) # Log any exceptions that occur during the data ingestion process
        raise e # Raise the exception to stop the execution