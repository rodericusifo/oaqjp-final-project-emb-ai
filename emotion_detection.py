import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    request_headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    request_body = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }
    response = requests.post(url, headers=request_headers, json=request_body)
    parsed_response = json.loads(response.text)
    emotions = parsed_response["emotionPredictions"][0]["emotion"]
    dominant_emotion_value = max(emotions.values())
    dominant_emotion = next(
        (key for key, value in emotions.items() if value == dominant_emotion_value),
        None
    )
    emotions["dominant_emotion"] = dominant_emotion
    return emotions
