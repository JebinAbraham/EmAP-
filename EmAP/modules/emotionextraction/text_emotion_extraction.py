#https://huggingface.co/michellejieli/emotion_text_classifier

from transformers import pipeline # type: ignore

def detect_emotions(text):
    classifier = pipeline("text-classification", model="michellejieli/emotion_text_classifier")
    emotion = classifier(text)
    return emotion

results = detect_emotions("I am happy")
#save the result as json file
import json
with open(r'data\Text_Output.json', 'w') as fp:
    json.dump(results, fp)