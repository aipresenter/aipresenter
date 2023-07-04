# import json
import logging
from ai_presenter.database import Database
from ai_presenter.generators import Generators
from elevenlabs.api import Voices
from elevenlabs import set_api_key


class AIPresenter:
    def __init__(self, db: Database, g: Generators):
        self.database = db
        self.generator = g

    def run(self):
        # self.__clear_voices()
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

# potentially might move to VoiceAI class, but stays here for now
    def __clear_voices(self):
        # file = open("test_clear_voices.txt", "w")

        config = self.database.get_config()
        key = config.get_ai_config().get_elevenlabs_api_key()

        set_api_key(key)
        voices = Voices.from_api()
        for voice in voices:
            # conditions true if voice is generated and not narrator
            if voice.category == 'generated' and voice.name != 'narrator':
                # delete generated voices that aren't narrator
                # this keeps voices list for each run clean because it is
                # called in run before work is done
                voice.delete()
                logging.info("Cleared voice")

        logging.info("Successfully cleared all voices")
