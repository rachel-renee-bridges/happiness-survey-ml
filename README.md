## ACME Happiness Survey ML Project

## Project Overview
This project trains and compares multiple machine learning models — Logistic Regression (LR), Decision Tree (DT), and Random Forest (RF) — on the ACME Happiness Survey 2020 dataset.
The goal is to predict overall happiness (Y) based on survey features.

## Included Notebooks

Logistic Regression (LR)

explore_all_features-LR.ipynb – Uses all features (X1–X6) to train a Logistic Regression model.

explore_selected_features-LR.ipynb – Uses selected features (X1, X2, X5) to train a Logistic Regression model.

Decision Tree (DT)

explore_all_features-DT.ipynb – Uses all features (X1–X6) to train a Decision Tree model.

explore_selected_features-DT.ipynb – Uses selected features (X1, X2, X5) to train a Decision Tree model.

Random Forest (RF)

explore_all_features-RF.ipynb – Uses all features (X1–X6) to train a Random Forest model.

explore_selected_features-RF.ipynb – Uses selected features (X1, X2, X5) to train a Random Forest model.  

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

