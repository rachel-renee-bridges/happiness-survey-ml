from happiness_survey_ml.src.data.load_data import load_acme_data
from happiness_survey_ml.src.features.select_features import get_all_features, get_selected_features
from happiness_survey_ml.src.models.train_model import split_data, train_logistic_model, predict_and_score, feature_importance

# 1. Load the dataset
df = load_acme_data()
print("Data loaded successfully.")

# 2. Select features and target
# Using selected features
X, y = get_selected_features(df)
feature_names = ['X1', 'X2', 'X5']

# If you want to use all features instead, uncomment these lines:
# X, y = get_all_features(df)
# feature_names = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']

print("Features selected.")

# 3. Split the data
X_train, X_test, y_train, y_test = split_data(X, y)
print("Data split into train and test sets.")

# 4. Train the logistic regression model
model = train_logistic_model(X_train, y_train)
print("Model trained.")

# 5. Predict and calculate F1 score
y_pred, f1 = predict_and_score(model, X_test, y_test)

# 6. Show feature importance
feature_importance(model, feature_names)
