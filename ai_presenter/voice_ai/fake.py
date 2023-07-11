from ai_presenter.voice_ai.base import VoiceAI, VoiceAIActor
from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import Iterator, Voice
import logging


class VoiceAIActorFake(VoiceAIActor):
    def __init__(self, config: VoiceConfig):
        super().__init__(config)

    def says(self, message) -> (bytes | Iterator[bytes]):
        logging.info(f'VoiceAIActorFake: {self.name} ' +
                     f'says {message}')

        audio = f'name: {self.name}\ngender: {self.gender}\n' + \
            f'age: {self.age}\naccent: {self.accent}\n' + \
            f'accent strength: {self.accent_strength}\n' + \
                f'description: {self.description}\n' + \
                f'message: {message}\n\n'
        return audio

    def __get_voice(self) -> Voice:
        logging.info(f'I am {self.name}. I am a {self.age} year old ' +
                     f'{self.gender} with a {self.accent} accent.')


class VoiceAIFake(VoiceAI):
    def __init__(self, db: Database):
        super().__init__(db)

    def new_actor(self, config):
        return VoiceAIActorFake(config)

    def generate(self, input_file: str, output_file: str):
        logging.info(f'VoiceAIFake: Opening input file: {input_file} and ' +
                     'extracting scene info')

        audio = ''
        with open(input_file, 'r') as file:
            for line in file:
                data = self.create_character_db(line)
                for message in data['dialogue']:
                    name = message['speaker']
                    text = message['message']
                    logging.info('VoiceAIFake: Stitching together audio')
                    audio += self.characters[name].says(text)

        logging.info('VoiceAIFake: Generating audio file')
        with open(output_file, 'w') as out:
            out.write(audio)

        logging.info(f'VoiceAIFake: Closing input file: {input_file}')
        logging.info(f"VoiceAIFake: generated audio found in {output_file}")

    def __create_character_db(self, input_file: str):
        return super().__create_character_db(input_file)
