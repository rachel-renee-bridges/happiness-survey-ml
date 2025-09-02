# ACME Happiness Survey ML Project

## Project Overview
This project trains logistic regression models on the ACME Happiness Survey 2020 dataset.  
The goal is to predict overall happiness (Y) based on survey features.

There are two notebooks included:

- `explore_all_features.ipynb` – Uses all features (X1–X6) to train a logistic regression model.  
- `explore_selected_features.ipynb` – Uses selected features (X1, X2, X5) to train a logistic regression model.  

## Project Structure

- data/: Dataset folders  
  - raw/: Original CSV files  
- notebooks/: Jupyter notebooks  
- references/: Research references  
- requirements.txt: List of Python libraries required  
- src/: Reusable Python code  
  - data/: Load and clean datasets  
  - features/: Feature selection and transformation  
  - main/: Calls all defined functions to execute the workflow  
  - models/: Train and evaluate models  

