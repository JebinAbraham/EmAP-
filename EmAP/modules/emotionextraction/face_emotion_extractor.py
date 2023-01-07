from deepface import DeepFace

def detect_emotions(image_path):

    # Use the DeepFace library to detect the emotions in the image
    emotions = DeepFace.analyze(image_path, actions=['emotion'])

    # Extract the list of emotions from the results
    emotions_list = emotions['emotion']

    return emotions_list

results = detect_emotions(r'data\processed_data\jebintest\splitframes\clip_000\frame_001.jpg')
#save the result as json file
import json
with open(r'data\Video_Output.json', 'w') as fp:
    json.dump(results, fp)
