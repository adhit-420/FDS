import pickle


class RFModel:
    def __init__(self):
        self.model = self.load_model("./app/api/models/rf_model.pkl")
        self.vectorizer = self.load_model("./app/api/models/vectorizer.pkl")

    def load_model(self, model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model

    def predict(self, input_data):
        # Use the loaded model to make predictions on the input data
        input_vectorized = self.vectorizer.transform(input_data)
        predictions = self.model.predict(input_vectorized)
        return predictions

    def predict_proba(self, input_data):
        input_vectorized = self.vectorizer.transform(input_data)
        predictions = self.model.predict_proba(input_vectorized)
        return predictions
