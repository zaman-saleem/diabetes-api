import pandas as pd       #data handling
import numpy as np               #numerical calculation
from sklearn.model_selection import train_test_split      # split divide two parts train and test
from sklearn.datasets import fetch_california_housing      # fetch california housing dataset
from sklearn.linear_model import Ridge                    #Ridge regression model use
import pickle                                      #save and load
from sklearn.metrics import mean_absolute_percentage_error     # evaluate model performance

data = fetch_california_housing()        #load california housing dataset
X = pd.DataFrame(data.data, columns=data.feature_names)       # features(X)
Y = pd.DataFrame(data.target, columns=["Target"])        # Target(Y)

# train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#train test csv files save
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
Y_train.to_csv("Y_train.csv", index=False)
Y_test.to_csv("Y_test.csv", index=False)

print("Train and Test datasets saved successfully!")

ridge_model = Ridge(alpha=1.0)

ridge_model.fit(X_train, Y_train)

train_score = ridge_model.score(X_train, Y_train)
test_score = ridge_model.score(X_test, Y_test)

print(f"Training Score (R^2): {train_score:.4f}")
print(f"Testing Score (R^2): {test_score:.4f}")

with open("ridge_model.pkl", "wb") as file:
    pickle.dump(ridge_model, file)

print("Model saved successfully as ridge_model.pkl!")

with open("ridge_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

print("Model loaded successfully!")

Y_pred = loaded_model.predict(X_test)

print("First 5 Predictions:", Y_pred[:5])

mape = mean_absolute_percentage_error(Y_test, Y_pred)

print(f"Mean Absolute Percentage Error (MAPE): {mape:.4f}")




