import pandas as pd
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from src.data_science_project_1.entity.config_entity import ModelEvaluationConfig
from src.data_science_project_1.utils.common import read_yaml, create_directories, save_json

#os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/hiteshkumavat0/datascience_project_1.mlflow"  # Replace with your DagsHub MLflow tracking URI
#os.environ["MLFLOW_TRACKING_USERNAME"] = "hiteshkumavat0"
#os.environ["MLFLOW_TRACKING_PASSWORD"] = "65ca0a30d83edf7b0fe7e1049d0fc7bbfdedadba"   ## Commented becazse it is not secure to hardcode credentials in the code.
from pathlib import Path 

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):        
        # Calculate evaluation metrics
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2


    def log_into_mlflow(self):
        # Load the test data
        test_data = pd.read_csv(self.config.test_data_path)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]
        
         # Load the model
        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            # Make predictions
            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            #Saving metrics as local file
            scores = {"rmse": rmse, "mae": mae,"r2": r2}
            save_json(path= Path(self.config.metric_file_name), data=scores)

            
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2) 

            # Model registry does not work with local files, so we need to save the model in a different way
            if tracking_url_type_store != "file":
                # Register the model in the MLflow Model Registry
                #Ther are other ways to use the model registtry , which depends on the use case
                #Please refer to the MLflow documentation for more details
                # https://www.mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name= "ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")