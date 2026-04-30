import json
import requests

def emotion_detector(text_to_analyze):
    """
    This function takes a text input and uses a Watson API to detect emotions in the text.
    It returns a dictionary with emotion scores and the dominant emotion.
    """

    ## Call API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=payload, headers=headers,timeout=10)

    ## Convert JSON
    formatted_response = json.loads(response.text)

    ## Build emotion dictionary
    result = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
    }

    ## Get the dominant_emotion
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion

    return result