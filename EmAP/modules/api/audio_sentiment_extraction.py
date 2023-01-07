import requests
# from modules.credentials import ASSEMBLYAI_APIKEY
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": "ri63ls05jk-eb27-47c7-ab81-d6be6f97f2e9",
    "sentiment_analysis": True
}
headers = {
    "authorization": "8ee11693dacb490c8f8bc7087dcb8873"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())