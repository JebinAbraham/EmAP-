#https://huggingface.co/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition

import torch
from transformers import AutoProcessor, AutoModelForAudioClassification, Wav2Vec2FeatureExtractor  # type: ignore
import numpy as np
from pydub import AudioSegment

# https://github.com/ehcalabres/EMOVoice
# the preprocessor was derived from https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english
# processor1 = AutoProcessor.from_pretrained("ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition")
# ^^^ no preload model available for this model (above), but the `feature_extractor` works in place
model1 = AutoModelForAudioClassification.from_pretrained("ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition")
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("facebook/wav2vec2-large-xlsr-53")

def predict_emotion(audio_file):
    if not audio_file:
        # I fetched some samples with known emotions from here: https://www.fesliyanstudios.com/royalty-free-sound-effects-download/poeple-crying-252
        audio_file = 'mp3/dude-crying.mp3'
    sound = AudioSegment.from_file(audio_file)
    sound = sound.set_frame_rate(16000)
    sound_array = np.array(sound.get_array_of_samples())
    # this model is VERY SLOW, so best to pass in small sections that contain 
    # emotional words from the transcript. like 10s or less.
    # how to make sub-chunk  -- this was necessary even with very short audio files 
    # test = torch.tensor(input.input_values.float()[:, :100000])

    input = feature_extractor(
        raw_speech=sound_array,
        sampling_rate=16000,
        padding=True,
        return_tensors="pt")

    result = model1.forward(input.input_values.float())
    # making sense of the result 
    id2label = {
        "0": "angry",
        "1": "calm",
        "2": "disgust",
        "3": "fearful",
        "4": "happy",
        "5": "neutral",
        "6": "sad",
        "7": "surprised"
    }
    interp = dict(zip(id2label.values(), list(round(float(i),4) for i in result[0][0])))
    return interp

file_path = r"data\25.wav"
result = predict_emotion(file_path)

#save the result as json file
import json
with open(r'data\Audio_Output.json', 'w') as fp:
    json.dump(result, fp)
