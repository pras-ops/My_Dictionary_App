import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "DRTA"

list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/.ci.yml",
    f"__init__.py",
    f"data/data",
    f"src/__init__.py",
    f"src/main.py",
    f"src/dictionary.py",
    f"tests/__init__.py",
    f"tests/test_dictionary.py",
    "requirements.txt",
    "setup.py",
    "app.py"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")