from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import Iterator, Voice
import logging


class VoiceAIActor:
    def __init__(self, config: VoiceConfig):
        self.name = config.name
        self.gender = config.gender
        self.description = config.description
        self.age = config.age
        self.accent = config.accent
        self.accent_strength = config.accent_strength

    def says(self, message, emotion) -> (bytes | Iterator[bytes]):
        logging.info(f'{self.config.name} says {message} in a {emotion} way')

    def __get_voice(self, emotion) -> Voice:
        logging.info(f'I am {self.name}. I am a {self.age} year old ' +
                     f'{self.gender} with a {self.accent} accent. I am ' +
                     f'currently speaking in a {emotion} tone because I' +
                     f' am {emotion}')


class VoiceAI:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def generate(self, input_file, output_file):
        logging.info("VoiceAI generating")

    def new_actor(self, config):
        logging.info("New actor created")
