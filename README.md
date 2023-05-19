# End-to-End ML Project Agenda

## 1. Set up the GitHub Repository
- Create a new repository on GitHub.
- Clone the repository to your local machine using Git.

## 2. Set up a new environment
- Open a command terminal.
- Create a new virtual environment using Conda: `conda create -n venv python=3.8 -y`.
- Activate the virtual environment: `conda activate venv/`.

## 3. Project Structure
- Create a `setup.py` and `requirements.txt` file.
- Install project dependencies: `pip install -r requirements.txt`.
- Create an `src` folder and add an `__init__.py` file to each folder.
- Create a `components` folder:
  - Inside the `components` folder, create the following files:
    - `data_ingestion.py`
    - `data_transformation.py`
    - `model_trainer.py`
- Create a `pipeline` folder:
  - Inside the `pipeline` folder, create the following files:
    - `predict_pipeline.py`
    - `train_pipeline.py`
- Create a file for exception handling: `exception.py` and `logger.py`.
- Create client or cloud-related files in `utils.py`.

## Troubleshooting: "No .egg-info directory found" error
- Check the package you are trying to install and ensure it is available.
- Verify that the `setup.py` file is correctly defined.
- Save the virtual environment by going to File -> Save All.

