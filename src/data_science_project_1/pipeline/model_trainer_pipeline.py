from src.data_science_project_1.config.configuration import ConfigurationManager
from src.data_science_project_1.components.model_trainer import ModelTrainer    
from src.data_science_project_1 import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()  # Create an instance of ConfigurationManager to read the configuration files
        model_trainer_config = config.get_model_trainer_config()  # Get the model trainer configuration
        model_trainer = ModelTrainer(config=model_trainer_config)  # Create an instance of ModelTrainer with the model trainer configuration
        model_trainer.train()  # Start the model training process

        logger.info(f"{STAGE_NAME} completed successfully.")