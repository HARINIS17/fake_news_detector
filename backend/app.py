from flask import Flask, request, jsonify, render_template
import pickle
import re

app = Flask(__name__)  # 👈 IMPORTANT

# load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    news = data.get("news", "")

    cleaned = re.sub(r'[^a-zA-Z ]', '', news.lower())
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    return jsonify({"prediction": "REAL" if prediction == 0 else "FAKE"})

if __name__ == "__main__":
    app.run(debug=True)
