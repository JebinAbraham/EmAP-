
import time 
import requests 
ASSEMBLYAI_APIKEY = "8ee11693dacb490c8f8bc7087dcb8873"
UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"

api_key = ASSEMBLYAI_APIKEY
headers = {"authorization": api_key, "content-type": "application/json"}

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data

upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=read_file(r'data\test\TestAudio.wav'))
audio_url = upload_response.json()["upload_url"]

transcript_request = {'audio_url': audio_url}
transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
_id = transcript_response.json()["id"]

while True:
    polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)

    if polling_response.json()['status'] == 'completed':
    #save the file in processed_data folder
       with open(f'{_id}.txt', 'w') as f:
           f.write(polling_response.json()['text'])
       print('Transcript saved to', _id, '.txt')
       break
    elif polling_response.json()['status'] == 'error':
        raise Exception("Transcription failed. Make sure a valid API key has been used.")
    else:
       print("Transcription queued or processing ...")
    time.sleep(5)

import requests
# from modules.credentials import ASSEMBLYAI_APIKEY
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": audio_url,
    "sentiment_analysis": True
}
headers = {
    "authorization": "8ee11693dacb490c8f8bc7087dcb8873"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())