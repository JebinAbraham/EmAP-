import soundfile as sf
import os
from transformers import Wav2Vec2Processor
from transformers import AutoModelForCTC
from conversationalnlp.models.wav2vec2 import Wav2Vec2Predict
from conversationalnlp.models.wav2vec2 import ModelLoader
from conversationalnlp.utils import *
import numpy as np

audioheaderpath = os.path.join(os.getcwd(), "temp")

pretrained_model = "codenamewei/speech-to-text"

processor = Wav2Vec2Processor.from_pretrained(pretrained_model)

model = AutoModelForCTC.from_pretrained(pretrained_model)

modelloader = ModelLoader(model, processor)

predictor = Wav2Vec2Predict(modelloader)


def speech_to_text(audiofile):
    """
    audiofile: str
    """
    # Load audio file and convert to desired format
    audio, sample_rate = sf.read(audiofile)

    # Check if audio file has a single channel
    if audio.ndim == 1:
        # Increase length of input by repeating the audio data
        audio = np.tile(audio, (2, 1)).T

    audio = (sample_rate, audio)

    audiofiles = [audiofile]
    predictiontexts = predictor.predictfiles(audiofiles)

    filetext = predictiontexts["predicted_text"][0] + "\n" + \
               predictiontexts["corrected_text"][0]

    return filetext


text = speech_to_text(r"data\processed_data\Abintest\splitaudio\clip_000.wav")
print(text)
