import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # Configure logging


project_name = "data_science_project_1"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",            # for package initialization
    f"src/{project_name}/components/__init__.py", # for components to be imported 
    f"src/{project_name}/utils/__init__.py",      # for utility functions
    f"src/{project_name}/utils/common.py",        # common utility functions
    f"src/{project_name}/config/__init__.py",     # configuration package
    f"src/{project_name}/config/configuration.py",     # configuration management
    f"src/{project_name}/pipeline/__init__.py",    # for pipeline components
    f"src/{project_name}/entity/__init__.py",       # for entity management
    f"src/{project_name}/entity/config_entity.py",  # configuration entities
    f"src/{project_name}/constants/__init__.py",    # constants for the project
    "config/config.yaml",                     # main configuration file
    "params.yaml",                        # parameters for the project
    "schema.yaml",                        # schema for data validation
    "main.py",                          # main entry point for the project
    "Dockerfile",                         # Dockerfile for containerization
    "setup.py",                          # setup script for packaging
    "reseach/research.ipynb",          # Jupyter notebook for research
    "templates/index.html",          # HTML template for web interface
]


for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir!="":
        # Create directory if it does not exist 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file : {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists and is not empty, skipping creation.")

