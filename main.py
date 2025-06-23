# Description: Main entry point for the data science project.
# This script initializes the data ingestion pipeline and starts the data ingestion process.
from src.data_science_project_1 import logger
from src.data_science_project_1.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.data_science_project_1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()  # Create an instance of DataIngestionTrainingPipeline
    obj.intiate_data_ingestion()  # Start the data ingestion process
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)  # Log any exceptions that occur during the data ingestion process
    raise e  # Raise the exception to stop the execution

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()  # Create an instance of DataValidationTrainingPipeline
    obj.intiate_data_validation()  # Start the data validation process
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e  # Raise the exception to stop the execution