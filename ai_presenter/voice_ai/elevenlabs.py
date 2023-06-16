from ai_presenter.voice_ai.base import VoiceAI
from ai_presenter.database import Database, VoiceConfig
import logging


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
        pass
