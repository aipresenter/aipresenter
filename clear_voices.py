# to be added to tools(or some other directory) later

import requests
from elevenlabs import Voices, Voice, set_api_key
from ai_presenter.ai_presenter import AIPresenter
import os

def clear_voices(ai_presenter: AIPresenter):
    file = open("test_clear_voices.txt", "w")
    config = ai_presenter.database.get_config()
    key = os.getenv('ELEVENLABS_APIKEY_2')
    # config.get_ai_config().get_elevenlabs_api_key()
    set_api_key(key)
    voices = Voices.from_api()
    print(voices)
    for voice in voices:
        if voice.category != 'premade':
            id_num = voice.voice_id
            url = "https://api.elevenlabs.io/v1/voices/" + id_num

            headers = {
            "Accept": "application/json",
            "xi-api-key": key
            }



            response = requests.delete(url, headers=headers)

            print(response.text, file=file)