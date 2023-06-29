from elevenlabs.api import Voices
from elevenlabs import set_api_key
import os

key = os.getenv("ELEVENLABS_APIKEY_2")
set_api_key(key)
voices = Voices.from_api()
file = open("test_clear_voices.txt", 'w')

for voice in voices:
    if voice.category != 'premade':
        print(voice, file=file)
