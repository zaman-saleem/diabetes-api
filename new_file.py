import pickle

model = {"example": "test"}  # Dummy model

with open("logistic_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")