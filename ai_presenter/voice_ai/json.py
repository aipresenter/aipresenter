import logging
import json
from ai_presenter.tools.age_converter import age_converter
from ai_presenter.voice_ai.base import VoiceAIActor
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import generate, save, Iterator, VoiceDesign, Voice
from elevenlabs import set_api_key
from elevenlabs.api import Voices
from ai_presenter.config.env_vars import get_elevenlabs_api_key

class VoiceAIDefaultActorElevenLabs(VoiceAIActor):
    def __init__(self, config: VoiceConfig, voice: Voice):
        super().__init__(config)
        # this is for a premade character
        self.voice = voice

    def says(self, message) -> (bytes | Iterator[bytes]):
        logging.info(f'{self.name} says {message}')
        audio = generate(text=message, model="eleven_monolingual_v1",
                         voice=self.voice)
        return audio


class VoiceAIActorElevenLabs(VoiceAIActor):
    def __init__(self, config: VoiceConfig):
        super().__init__(config)

        # this is for a generated character
        self.sample_text = f'I am {self.name}. I am a {self.age} year old ' + \
            f'{self.gender} with a {self.accent} accent.' + \
            f'I am {self.name}. I am a {self.age} year old ' + \
            f'{self.gender} with a {self.accent} accent.'

        logging.info(f"designing a voice for {self.name} gender:{self.gender}")
        self.voice_design = VoiceDesign(name=self.name,
                                        text=self.sample_text,
                                        gender=self.gender,
                                        age=self.age, accent=self.accent,
                                        accent_strength=self.accent_strength)

        self.voice = Voice.from_design(self.voice_design)

    def says(self, message) -> (bytes | Iterator[bytes]):
        logging.info(f'{self.name} says {message}')
        audio = generate(text=message, model="eleven_monolingual_v1",
                         voice=self.voice)
        return audio

    def get_voice(self) -> Voice:
        return self.voice


class JSON:
    def __init__(self):
        set_api_key(get_elevenlabs_api_key())
        # list that keeps track of new voices created in this run
        self.generated_voices = []
        self.voices = Voices.from_api()
        self.characters = {}
        self.actors = []

    def new_actor(self, config: VoiceConfig) -> VoiceAIActor:
        voice = self.__find_voice(config.name)
        if voice is not None:
            # if voice exits, use that voice
            return VoiceAIDefaultActorElevenLabs(config, voice)

        # if voice doesn't exist generate voice
        actor = VoiceAIActorElevenLabs(config)
        # save each new actor's voice that gets generated into a list
        self.generated_voices.append(actor.get_voice())
        return actor

    def generate(self, input_file: str, output_file: str):
        logging.info('ElevenLabs: Generating audio file')

        audio = bytes()
        with open(input_file, 'r') as file:
            for line in file:
                # load characters in character db
                data = self.create_character_db(line)

                # now go through dialogue and create audio
                for message in data['dialogue']:
                    name = message['speaker']
                    text = message['message']
                    logging.info('ElevenLabs: Stitching together audio')
                    audio += self.characters[name].says(text)
        logging.info(f"ElevenLabs: Audio can be found in {output_file}")
        save(audio, output_file)
        self.__clear_voices()

    def __find_voice(self, name: str) -> Voice:
        for voice in self.voices:
            if voice.name.lower() == name.lower():
                return voice
        return None

    def get_generated_voices(self) -> list[Voice]:
        return self.generated_voices

    def __clear_voices(self):
        # gets the generated voices created during this iteration of
        # AI Presenter, and the for loop deletes each of these voices
        # but not voices that were present before this run of the program
        voices = self.get_generated_voices()
        for voice in voices:
            voice.delete()
            logging.info(f"Deleted voice: {voice.name.lower()}")

        logging.info("Successfully cleared voices generated")

    def fill_actors(self):
        pass

    def create_character_db(self, line: str):
        json_string = line.strip()
        data = json.loads(json_string)
        self.fill_actors()

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