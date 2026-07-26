from sentiment.pipeline.prediction_pipeline import PredictPipeline

pipeline = PredictPipeline()

reviews = [
    "This movie was terrible. It was boring, slow, and a complete waste of time.",
    "Great movie",
    "I loved this movie",
    "Amazing acting",
    "Worst movie ever",
]

for review in reviews:
    prediction, confidence = pipeline.predict(review)

    print(f"\nReview: {review}")
    print(f"Prediction: {prediction}")
    print(f"Confidence: {confidence:.4f}")