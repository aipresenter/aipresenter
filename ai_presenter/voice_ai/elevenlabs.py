from ai_presenter.voice_ai.base import VoiceAI, VoiceAIActor
from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import generate, save, Iterator, VoiceDesign, Voice
from elevenlabs import set_api_key
from elevenlabs.api import Voices
import logging


class VoiceAIDefaultActorElevenLabs(VoiceAIActor):
    def __init__(self, config: VoiceConfig, voice: Voice):
        # this is for the narrator
        super().__init__(config)
        self.voice = voice

    # .says takes the message and generates audio from that message
    # note: for the real voiceaiactor class, the elevenlabs generate
    # methods return raw data called audio which can be manipulated before
    # saving to a file(ie. concatenation)
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

    # .says takes the message and generates audio from that message
    # note: for the real voiceaiactor class, the elevenlabs generate
    # methods return raw data called audio which can be manipulated before
    # saving to a file(ie. concatenation)
    def says(self, message) -> (bytes | Iterator[bytes]):
        logging.info(f'{self.name} says {message}')
        audio = generate(text=message, model="eleven_monolingual_v1",
                         voice=self.voice)
        return audio


class ElevenLabs(VoiceAI):
    def __init__(self, db: Database):
        super().__init__(db)
        set_api_key(db.get_config().get_ai_config().get_elevenlabs_api_key())

    def new_actor(self, config) -> VoiceAIActor:
        if config.name == 'narrator':
            voice = self.__find_voice(config.name)
            return VoiceAIDefaultActorElevenLabs(
                config, voice)
        return VoiceAIActorElevenLabs(config)

    # make narrator actor
    # open file and create a new actor for each character
    # for each line of dialogue, input it into actor.says
    # actor.says returns audio output
    # this is concatenated with previous actor.says outputs
    # output file opened and audio output is written to output_file
    # this is saved into output file
    # return output file

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

    def __find_voice(self, name) -> Voice:
        voices = Voices.from_api()

        # need ideas on what to do if narrator character isn't found
        # just for control of code flow
        for voice in voices:
            if voice.name == name:
                return voice
