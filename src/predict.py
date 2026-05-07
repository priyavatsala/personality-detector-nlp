import joblib

# load saved model
model = joblib.load("model.pkl")

# load saved vectorizer
vectorizer = joblib.load("vectorizer.pkl")


def predict_personality(text):

    # convert text into tf-idf features
    text_vector = vectorizer.transform([text])

    # predict personality
    prediction = model.predict(text_vector)

    return prediction[0]