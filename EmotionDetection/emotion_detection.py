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

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code >= 400:
        raise Exception("Unexpected error from Watson API, got status code: " + str(response.status_code) + "")

    ## Convert JSON
    formatted_response = json.loads(response.text)

    ## Build emotion dictionary
    result = formatted_response['emotionPredictions'][0]['emotion']

    ## Get the dominant_emotion
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion

    return result