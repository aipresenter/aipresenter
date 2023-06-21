from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
import logging


class VoiceAIActor:
    def __init__(self, config: VoiceConfig):
        self.config = config

    def says(self, message, emotion, filename):
        logging.info(f'{self.config.name} says {message} in a {emotion} way')


class VoiceAI:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def generate(self, input_file, output_file, c: VoiceConfig):
        logging.info("VoiceAI generating")

    def new_actor(self, config):
        logging.info("New actor created")
