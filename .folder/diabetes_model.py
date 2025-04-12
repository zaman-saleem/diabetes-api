import pandas as pd                 # data handling
import numpy as np                  # numerical calculation
from sklearn.model_selection import train_test_split         #Dataset divide train and testing
from sklearn.linear_model import LogisticRegression         # Logistic regression model use
from sklearn.preprocessing import StandardScaler        #data normalization standard scaler
import pickle                   # model save library
from sklearn.metrics import confusion_matrix       #model evaluation confusion matrix

df = pd.read_csv("C:\\Users\\DELL\\Downloads\\archive (3)\\diabetes.csv")    #load file
df.head()          #chk first five rows
df.info()           #chk datatype and missing value

X = df.drop(columns=['Outcome'])             # features
y = df['Outcome']                            # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  #train test split

X_train.to_csv("X_train.csv", index=False)  # Training Features save
X_test.to_csv("X_test.csv", index=False)  # Testing Features save
y_train.to_csv("y_train.csv", index=False)  # Training Labels save
y_test.to_csv("y_test.csv", index=False)  # Testing Labels save

scaler = StandardScaler()               #standard scaler create object
X_train = scaler.fit_transform(X_train)  # Training data normalize
X_test = scaler.transform(X_test)          #testing data normalize

model = LogisticRegression()         #create logistic regression model
model.fit(X_train, y_train)           #training data model train

with open("logistic_model.pkl", "wb") as file:             #create new file & save model
    pickle.dump(model,file)                                  # this file save and use

with open("logistic_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)
print("Model loaded successfully!")

y_pred = loaded_model.predict(X_test)  # Test dataset par model predict kar raha hai
print("Predictions:", y_pred[:10])         #first 10 ten prediction value check

cm = confusion_matrix(y_test, y_pred)  # Real vs Predicted values matrix
print("\nConfusion Matrix:")
print(cm)





