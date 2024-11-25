from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Dectection")

@app.get("/")
def emotion_detector_page():
    return render_template("index.html")

@app.get("/emotionDetector")
def emotion_detector_process():
    text_to_analyze = request.args.get("textToAnalyze")
    response_emotion_detector = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response_emotion_detector['anger']}, "
        f"'disgust': {response_emotion_detector['disgust']}, "
        f"'fear': {response_emotion_detector['fear']}, "
        f"'joy': {response_emotion_detector['joy']} and "
        f"'sadness': {response_emotion_detector['sadness']}. "
        f"The dominant emotion is {response_emotion_detector['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)