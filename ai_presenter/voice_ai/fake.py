from ai_presenter.voice_ai.base import VoiceAI, VoiceAIActor
from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
import logging


# This new idea changes the way generate could work, see lines 55 to 59
class VoiceAIActorFake(VoiceAIActor):
    def __init__(self, config: VoiceConfig):
        super().__init__(config)

    def says(self, message, emotion, filename):
        # .says takes the message and generates audio from that message
        # this audio gets saved to a file
        # personally don't think says needs a file passed to it bc
        # note: for the real voiceaiactor class, the elevenlabs generate
        # methods return raw data called audio which can be manipulated before
        # saving to a file(ie. concatenation)
        logging.info(f'{self.config.name} says {message} in a {emotion} way')
        # return message


class VoiceAIFake(VoiceAI):
    def __init__(self, db: Database):
        super().__init__(db)

    def new_actor(self, config):
        return VoiceAIActorFake(config)

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
    def generate(self, input_file: str, output_file: str, c: VoiceConfig):
        logging.info('Setting voice configuration')

        logging.info(f'VoiceAIFake: Opening input file: {input_file} and ' +
                     'extracting send info')
        with open(input_file, 'r') as input:
            text = input.read()

        logging.info('VoiceAIFake: Generating audio file')

        with open(output_file, 'w') as out:
            out.write(text)

        logging.info(f'VoiceAIFake: Closing input file: {input_file}')
        logging.info(f"VoiceAIFake: generated audio found in {output_file}")

    # generate could instead be a series of voiceaiactor.says() calls
    # which return the audio data/messages. This can then be concatenated
    # together and saved to given file
    # generate wouldn't need voice config passed in anymore because says
    # method in voiceaiactor already has it
