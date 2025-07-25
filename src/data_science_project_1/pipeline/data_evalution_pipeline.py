from src.data_science_project_1.config.configuration import ConfigurationManager
from src.data_science_project_1.components.model_evalution import ModelEvaluation
from src.data_science_project_1 import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()  # Create an instance of ConfigurationManager to read the configuration files
        model_evaluation_config = config.get_model_evaluation_config()  # Get the model evaluation configuration
        model_evaluation = ModelEvaluation(config=model_evaluation_config)  # Create an instance of ModelEvaluation with the model evaluation configuration
        model_evaluation.log_into_mlflow()  # Start the model evaluation process

        logger.info(f"{STAGE_NAME} completed successfully.")