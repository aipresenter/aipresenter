from ai_presenter.database import Database
from ai_presenter.generators import Generators
import logging


class AIPresenter:
    def __init__(self, db: Database, g: Generators):
        self.database = db
        self.generator = g

    def run(self):
        config = self.database.get_config()
        text_ai_file = config.get_ai_config().get_text_ai_filename()

        with open(text_ai_file, 'w') as file:
            textai = self.generator.get_text()
            for key, scene in self.database.scenes.items():
                logging.info(f"Working on scene: {scene.name} in " +
                             f"{scene.location}")

                output = textai.generate(scene)
                file.write(output + '\n')
                logging.info(f'got back from textai: {output}')

        # Generate voice ai
        voiceai = VoiceAI(self.database)
        voiceconfig = VoiceConfig()
        voiceai.generate('text_ai.txt', 'voice_ai.txt', voiceconfig)
