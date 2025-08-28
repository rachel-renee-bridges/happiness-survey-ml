from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

# Split the dataset into train and test sets
def split_data(X, y, test_size=0.1, random_state=20, shuffle=True):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

# Train a logistic regression model
def train_logistic_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

# Predict and calculate F1 score
def predict_and_score(model, X_test, y_test):
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    print("F1 Score:", f1)
    return y_pred, f1

# Print feature importance using your original while loop
def feature_importance(model, features):
    print("Feature Importance:")
    coefficients = model.coef_[0]
    i = 0
    while i < len(features):
        feature_name = features[i]
        coef_value = coefficients[i]
        print(feature_name, ":", round(coef_value, 2))
        i += 1
