import requests
import os 
from dotenv import load_dotenv
import re

load_dotenv()
api_key = os.getenv('ELEVEN_LABS')

url = "https://api.elevenlabs.io/v1/text-to-speech/qPZaK0RbhNPDKEShnhKf"  # This URL might be different; refer to the ElevenLabs documentation

file_path = './study_guide.md'

with open(file_path, 'r', encoding='utf-8') as file:
    markdown_content = file.read()
plain_text_content = re.sub(r'\W+', ' ', markdown_content)

CHUNK_SIZE = 1024


headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key
}

data = {
  "text": plain_text_content,  # Use the content read from the file
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print("Audio generated successfully and saved to output.mp3")
else:
    print("Failed to generate audio:", response.text)
