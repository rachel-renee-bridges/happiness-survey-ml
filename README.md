# ACME Happiness Survey ML Project

## Project Overview
This project trains logistic regression models on the ACME Happiness Survey 2020 dataset. 
The goal is to predict overall happiness (Y) based on survey features.

There are two notebooks included:

1. `01_explore_all_features.ipynb` – Uses all features (X1-X6) to train a logistic regression model.
2. `02_explore_selected_features.ipynb` – Uses selected features (X1, X2, X5) to train a logistic regression model.

## Project Structure

- 02_requirements.txt → list of Python libraries required
- 03_data/: Dataset folders
    - 01_raw/: Original CSV files
    - 02_interim/: Temporary files during processing (optional)
    - 03_processed/: Cleaned datasets (optional)
    - 04_external/: External datasets (optional)
- 04_notebooks/: Jupyter notebooks
- 05_src/: Reusable Python code
    - 01_happiness_survey_ml/data/: Load and clean datasets
    - 02_features/: Feature selection and transformation
    - 03_models/: Train and evaluate models
- 06_references/: Research references
