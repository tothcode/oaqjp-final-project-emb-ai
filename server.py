"""
Emotion Detection Server
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index_page():
    """
    Renders the index.html template for the root URL.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects the emotion in a given text using the emotion_detector
    function from EmotionDetection module.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (f"For the given statement, the system response is 'anger': {res['anger']}, "
            f"'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and "
            f"'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
