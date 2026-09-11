import pandas as pd
import numpy as np
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score,precision_score,recall_score, f1_score)
import pickle

mlflow.set_tracking_uri("http://127.0.0.1:5000")


# Read dataset
data = pd.read_csv(r"D:\TYDS42A\MLPracticals\testing\data\water_potability.csv")


# Split the data into training and testing sets
train_data, test_data = train_test_split(data,test_size=0.20,random_state=42)


# Function to fill missing values with median
def fill_missing_with_median(df):

    df = df.copy()

    for column in df.columns:

        if df[column].isnull().any():

            median_value = df[column].median()

            df[column] = df[column].fillna(median_value)

    return df


# Fill missing values with median
train_processed_data = fill_missing_with_median(train_data)
test_processed_data = fill_missing_with_median(test_data)


# Import Random Forest
from sklearn.ensemble import RandomForestClassifier

# Separate features and target
X_train = train_processed_data.iloc[:, :-1].values
y_train = train_processed_data.iloc[:, -1].values

X_test = test_processed_data.iloc[:, :-1].values
y_test = test_processed_data.iloc[:, -1].values


# Number of estimators
n_estimators = 500


# Start MLflow run
with mlflow.start_run():

    # Create Random Forest classifier
    clf = RandomForestClassifier( n_estimators=n_estimators,random_state=42)

    # Train the model
    clf.fit(X_train, y_train)


    # Save the trained model
    pickle.dump(
        clf,
        open("model.pkl", "wb")
    )


    # Make predictions
    y_pred = clf.predict(X_test)


    # Calculate evaluation metrics
    acc = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred)

    recall = recall_score(
        y_test,
        y_pred)

    f1_score_value = f1_score(
        y_test,
        y_pred)


    # Log metrics in MLflow
    mlflow.log_metric("acc", acc)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1-score", f1_score_value)


    # Log parameter
    mlflow.log_param(
        "n_estimators",
        n_estimators
    )


    # Print results
    print("acc", acc)
    print("precision", precision)
    print("recall", recall)
    print("f1-score", f1_score_value)