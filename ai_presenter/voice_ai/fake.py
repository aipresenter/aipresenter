from ai_presenter.voice_ai.base import VoiceAI
from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
import logging


class VoiceAIFake(VoiceAI):
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
    def generate(self, input_file: str, output_file: str, c: VoiceConfig):
        logging.info('Setting voice configuration')

        logging.info(f'VoiceAIFake: Opening input file: {input_file} and ' +
                     'extracting send info')
        # with open(input_file, 'r') as input:
        #    text = input.read()

        logging.info('VoiceAIFake: Generating audio file')

        with open(output_file, 'w') as out:
            out.write()

        logging.info(f'VoiceAIFake: Closing input file: {input_file}')
        logging.info(f"VoiceAIFake: generated audio found in {output_file}")
        return out
