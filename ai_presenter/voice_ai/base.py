from ai_presenter.database import Database
from ai_presenter.config.voice import VoiceConfig
import logging


class VoiceAI:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def generate(self, input_file, output_file, c: VoiceConfig):
        logging.info("VoiceAI generating")
