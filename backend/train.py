import json
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

def train_model():

    with open('intents.json', 'r') as f:
        intents = json.load(f)

    corpus = []
    tags = []

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            corpus.append(pattern)
            tags.append(intent['tag'])

    model = Pipeline([
        ('vect', CountVectorizer(ngram_range=(1, 2), stop_words='english')),
        ('tfidf', TfidfTransformer()),
        ('clf', LogisticRegression(random_state=42, C=100.0, max_iter=500))
    ])

    print("Training model...")
    model.fit(corpus, tags)
    print("Model trained successfully.")

    data = {
        "model": model,
        "intents": intents
    }

    with open('model_data.pkl', 'wb') as f:
        pickle.dump(data, f)
    
    print("Model saved to model_data.pkl")

if __name__ == "__main__":
    train_model()
