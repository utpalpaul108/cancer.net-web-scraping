import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'webScraping'

list_of_files = [
    f'src/{project_name}/__init__.py',

    # For Logger
    f'src/{project_name}/logger/__init__.py',

    # For Components
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_extraction.py',

    # For Utils
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',


    # For Pipeline
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/research_and_advocacy_pipeline.py',

    # For Constants
    f'src/{project_name}/constants/__init__.py',

    # For Notebooks
    'notebooks/cancer-types.ipynb',

    # For Local Package
    'setup.py',

    # Required Packages
    'requirements.txt'
]


for filepath in list_of_files:
    
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    print(filedir + "--" + filename)

    if (filedir != '') and (not os.path.exists(filedir)):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} already exists")

    
    
    