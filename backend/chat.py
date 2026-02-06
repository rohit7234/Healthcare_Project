import pickle
import random
import json
import os

class ChatBot:
    def __init__(self, model_path='model_data.pkl'):
        self.model_path = model_path
        self.model = None
        self.intents = None
        self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            print(f"Error: Model file {self.model_path} not found. Please run train.py first.")
            return

        with open(self.model_path, 'rb') as f:
            data = pickle.load(f)
            self.model = data["model"]
            self.intents = data["intents"]

    def get_response(self, text):
        if not self.model:
            return "Error: Model not loaded."

        try:
            predicted_tag = self.model.predict([text])[0]
            probs = self.model.predict_proba([text])
            confidence = max(probs[0])
            
            # Find response for tag
            for intent in self.intents['intents']:
                if intent['tag'] == predicted_tag:
                    return random.choice(intent['responses'])
            
            return "I seem to be having trouble processing that."

        except Exception as e:
            print(f"Error during prediction: {e}")
            return "Sorry, something went wrong processing your request."

if __name__ == "__main__":
    bot = ChatBot()
    print(bot.get_response("Hello"))
    print(bot.get_response("I have a fever"))
