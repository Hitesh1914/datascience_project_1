# logging file for the project
# This file is used to initialize the data science project package and set up the logging configuration.
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # Configure logging

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log") # Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True) # Create log directory if it does not exist

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file               
        logging.StreamHandler(sys.stdout)  # Also log to console
    ]
)

logger = logging.getLogger("ds_project_logger")  # Create a logger for the current module