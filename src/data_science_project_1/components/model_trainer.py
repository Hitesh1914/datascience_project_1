import pandas as pd
import os
from src.data_science_project_1 import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.data_science_project_1.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        
        self.config = config

    def train(self):
        logger.info("Loading training and testing data")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop(columns=[self.config.target_column], axis=1)  # axis=1 indicates that we are dropping a column, not a row
        test_x = test_data.drop(columns=[self.config.target_column], axis=1)  # drop the target column from the training and testing data
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        
        lr = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42  # random_state is set for reproducibility
        )                                        # ElasticNet is a linear regression model that combines L1 and L2 regularization
        logger.info("Training the model")
        lr.fit(train_x, train_y)         # fit method trains the model on the training data

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))  # joblib is used to save the model to a file
        logger.info(f"Model is saved at {self.config.root_dir}/{self.config.model_name}")
