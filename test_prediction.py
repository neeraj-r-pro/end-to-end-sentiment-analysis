from sentiment.pipeline.prediction_pipeline import PredictPipeline

pipeline = PredictPipeline()

review = "This movie was terrible. It was boring, slow, and a complete waste of time."
prediction = pipeline.predict(review)

print("Review:", review)
print("Prediction:", prediction)