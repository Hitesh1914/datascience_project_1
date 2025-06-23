from src.data_science_project_1.config.configuration import ConfigurationManager
from src.data_science_project_1.components.data_transformation import DataTransformation
from src.data_science_project_1 import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def intiate_data_transformation(self):
        # This function initiates the data transformation process by checking the status of data validation and then performing train-test splitting.
        # It reads the status from the status.txt file in the artifacts/data_validation directory and if
        try:                  
            with open("artifacts/data_validation/status.txt", "r") as f: # Open the status.txt file in the artifacts/data_validation directory
                status = f.read().split(" ")[-1] # Read the status from the status.txt file in the artifacts/data_validation directory
                if status == "True": # If the status is True, it means the data validation was successful and we can proceed with data transformation
                    config = ConfigurationManager()  # Create an instance of ConfigurationManager to read the configuration
                    data_transformation_config = config.get_data_transformation_config()  # Get the data transformation configuration
                    data_transformation = DataTransformation(config=data_transformation_config)  # Create an instance of DataTransformation with the data transformation configuration
                    data_transformation.train_test_splitting()  # Perform the train-test splitting
                else:
                    raise Exception("your data schema is not valid. Cannot proceed with Data Transformation.")
        
        except Exception as e:
                    print(e)