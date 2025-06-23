import os 
from src.data_science_project_1 import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.data_science_project_1.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        #logger.info(f"Data Transformation Config: {self.config}")
    '''
    NOTE: you can add different transformation methods here, such as scaling, encoding, PCA, etc.
    You can perform all kinds of EDA in ML cycle here before passing this data to the model training phase.
     
    For this example, we will just split the data into train and test sets because data is already clean and preprocessed.
    '''
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path) # read the data from the data_path

        ## Split the data into train and test sets
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)    

        logger.info(f"Train and test data saved at {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape, test.shape)