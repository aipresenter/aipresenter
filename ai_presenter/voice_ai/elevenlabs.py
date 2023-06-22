from ai_presenter.voice_ai.base import VoiceAI, VoiceAIActor
from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import generate, save, Iterator, VoiceDesign, Voice
import json
import logging


class VoiceAIActorElevenLabs(VoiceAIActor):
    def __init__(self, config: VoiceConfig):
        super().__init__(config)

        sample_text = f'I am {self.name}. I am a {self.age} year old ' + \
            f'{self.gender} with a {self.accent} accent.' + \
            f'I am {self.name}. I am a {self.age} year old ' + \
            f'{self.gender} with a {self.accent} accent.'
        self.voice_design = VoiceDesign(name=self.name,
                                        text=sample_text, gender=self.gender,
                                        age=self.age, accent=self.accent,
                                        accent_strength=self.accent_strength)

    # .says takes the message and generates audio from that message
    # note: for the real voiceaiactor class, the elevenlabs generate
    # methods return raw data called audio which can be manipulated before
    # saving to a file(ie. concatenation)
    def says(self, message, emotion) -> (bytes | Iterator[bytes]):
        logging.info(f'{self.name} says {message} in a {emotion} way')
        audio = generate(text=message, model="eleven_monolingual_v1",
                         voice=self.__get_voice(emotion))
        return audio

    def __get_voice(self, emotion) -> Voice:
        logging.info(f"Designing voice for {self.name}")
        return Voice.from_design(self.voice_design)


class ElevenLabs(VoiceAI):
    def __init__(self, db: Database):
        super().__init__(db)

    def new_actor(self, config):
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
        logging.info('Generating audio file')
        with open(input_file) as file:
            data = json.load(file)

        narrator_config = VoiceConfig()
        narrator = self.new_actor(narrator_config)
        audio = narrator.says()
        # need suggestions as to format of json
        # as well as parsing it

        for key, message in data['dialogue'].items():
            character_config = VoiceConfig()
            character = self.new_actor(character_config)
            audio += character.says(message.message, message.emotion)

        save(audio, output_file)
