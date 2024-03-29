from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
from ai_presenter.tools.age_converter import age_converter
from packages.elevenlabs.elevenlabs import Iterator, Voice
import json
import logging


class VoiceAIActor:
    def __init__(self, config: VoiceConfig):
        self.name = config.name
        self.gender = config.gender
        self.description = config.description
        self.age = config.age
        self.accent = config.accent
        self.accent_strength = config.accent_strength

    # .says takes the message and generates audio from that message
    # note: for the real voiceaiactor class, the elevenlabs generate
    # methods return raw data called audio which can be manipulated before
    # saving to a file(ie. concatenation)
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
        self.characters = {}

    def generate(self, input_file, output_file, db):
        logging.info("VoiceAI generating")

    def new_actor(self, config) -> VoiceAIActor:
        logging.info("New actor created")

    def create_character_db(self, line: str):
        json_string = line.strip()
        data = json.loads(json_string)

        for message in data['dialogue']:
            name = message['speaker']

            if name not in self.characters:
                logging.info(f"creating character {name}")
                try:
                    age = age_converter(self.actors[name].age)
                    character_config = VoiceConfig(name,
                                                   self.actors[name].gender,
                                                   age,
                                                   self.actors[name].accent,
                                                   1.99,
                                                   self.actors[name].
                                                   description)
                    self.characters[name] = self.new_actor(character_config)
                except Exception:
                    character_config = VoiceConfig(name,
                                                   'male',
                                                   'middle_aged',
                                                   "british",
                                                   1.99,
                                                   f"This is the {name}")
                    self.characters[name] = self.new_actor(character_config)
        return data

    def get_new_voices(self) -> list[Voice]:
        return []
