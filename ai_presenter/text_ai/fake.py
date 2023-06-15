from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database
import logging


class TextFake(TextAi):
    def __init__(self, db: Database):
        super().__init__(db)

    def generate(self):
        pass

    def send(self, text) -> str:
        logging.info(f"textfake: Sending {text}")
        return text
