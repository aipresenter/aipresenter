# import json
import logging
import requests
from ai_presenter.database import Database
from ai_presenter.generators import Generators
from elevenlabs.api import Voices
from elevenlabs import set_api_key
# from ai_presenter.voice_ai.base import VoiceConfig


class AIPresenter:
    def __init__(self, db: Database, g: Generators):
        self.database = db
        self.generator = g

    def run(self):
        config = self.database.get_config()
        text_ai_file = config.get_ai_config().get_text_ai_filename()
        voice_ai_file = config.get_ai_config().get_voice_ai_filename()

        with open(text_ai_file, 'w') as file:
            textai = self.generator.get_text()
            for key, scene in self.database.scenes.items():
                logging.info(f"Working on scene: {scene.name} in " +
                             f"{scene.location}")

                output = textai.generate(scene)
                file.write(output + '\n')
                logging.info(f'got back from textai: {output}')

        # Generate voice ai
        # chr_db = {}
        #  for line in file:
        #   chr_db
        voiceai = self.generator.get_voice()
        voiceai.generate(text_ai_file, voice_ai_file)


    def clear_voices(self):
        file = open("test_clear_voices.txt", "w")
        
        config = self.database.get_config()
        key = config.get_ai_config().get_elevenlabs_api_key()
        
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