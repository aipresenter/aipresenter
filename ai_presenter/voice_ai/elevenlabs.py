from ai_presenter.voice_ai.base import VoiceAI, VoiceAIActor
from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import generate, Iterator, VoiceDesign, Voice
import logging


class VoiceAIActorElevenLabs(VoiceAIActor):
    def __init__(self, config: VoiceConfig):
        super().__init__(config)

    # .says takes the message and generates audio from that message
    # note: for the real voiceaiactor class, the elevenlabs generate
    # methods return raw data called audio which can be manipulated before
    # saving to a file(ie. concatenation)
    def says(self, message, emotion) -> (bytes | Iterator[bytes]):
        logging.info(f'{self.config.name} says {message} in a {emotion} way')
        audio = generate(text=message, model="eleven_monolingual_v1",
                         voice=self.__get_voice(emotion))
        return audio

    def __get_voice(self, emotion) -> Voice:
        sample_text = f'I am {self.name}. I am a {self.age} year old ' + \
                        f'{self.gender} with a {self.accent} accent. I am' + \
                        f' currently speaking in a {emotion} tone because' + \
                        f' I am {emotion}'

        voice_design = VoiceDesign(name=self.name,
                                   text=sample_text,
                                   gender=self.gender, age=self.age,
                                   accent=self.accent,
                                   accent_strength=self.accent_strength)
        return Voice.from_design(voice_design)


class ElevenLabs(VoiceAI):
    def __init__(self, db: Database):
        super().__init__(db)

    # sets up config
    # opens the file
    # reads the file; do you need to read the file to send it?
    # sends text in file voice ai
    # depending on design decision, can send up to ""
    # or just read in one voice of narrator
    # if option 2, MAYBE remove voice type from user provided file
    # ai does its thingy and returns voice data
    # output file opened and voice data is written to output_file
    # this is saved into output file
    # return output file

    def generate(self, input_file, output_file, c: VoiceConfig):
        logging.info('Generating audio file')
