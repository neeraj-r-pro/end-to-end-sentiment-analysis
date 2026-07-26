from flask import Flask, render_template, request, jsonify

from sentiment.pipeline.prediction_pipeline import PredictPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from the frontend
        data = request.get_json()

        review = data.get("review", "")

        # Load the prediction pipeline
        predictor = PredictPipeline()

        # Get prediction and confidence
        prediction, confidence = predictor.predict(review)

        print("Prediction:", prediction)
        print("Type:", type(prediction))

       # Model already returns the sentiment as a string
        sentiment = prediction

        # Send the response back to the frontend
        return jsonify({
            "sentiment": sentiment,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)