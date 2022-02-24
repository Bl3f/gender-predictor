import flask
from flask import Flask, escape, request
import pandas as pd
import joblib
from unidecode import unidecode

app = Flask(__name__)

model = joblib.load('model.v1.pickle')

FEMALE = 0
MALE = 1


def encoder(names):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"

    features = pd.DataFrame()
    for letter in alphabet:
        features[letter] = (
            names.apply(unidecode).str.upper().str.count(letter).astype(int)
        )

    return features


@app.route('/')
def hello():
    return f'Hello, this is the gender-predictor!'


@app.route('/predict')
def predict():
    name = request.args.get("name")

    results = model.predict(encoder(pd.Series([name])))
    prediction = results[0]
    gender = "FEMALE" if prediction == FEMALE else "MALE"

    return flask.jsonify({"gender": gender, "name": name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
