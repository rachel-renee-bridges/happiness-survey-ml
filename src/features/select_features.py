# Select all or selected features from the dataset

def get_all_features(df):
    # Select all features X1-X6 and target Y
    X = df[['X1', 'X2', 'X3', 'X4', 'X5', 'X6']]
    y = df['Y']
    return X, y

def get_selected_features(df):
    # Select only features X1, X2, X5 and target Y
    X = df[['X1', 'X2', 'X5']]
    y = df['Y']
    return X, y
