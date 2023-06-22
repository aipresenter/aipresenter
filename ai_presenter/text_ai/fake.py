import logging
import json
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database


class TextFake(TextAi):
    def __init__(self, db: Database):
        super().__init__(db)

    def generate(self):
        pass

    def send(self, text) -> str:
        logging.info(f"textfake: Sending {text}")
        dialogue = {
            "characters": [
                {
                    "name": "Don Luis",
                    "personality": "authoritative and stubborn",
                    "emotion": "stubborn"
                },
                {
                    "name": "Immanuel",
                    "personality": "boisterous and foolheaded",
                    "emotion": "cheerful"
                }
            ],
            "dialogue": [
                {
                    "speaker": "Don Luis",
                    "message": "Immanuel, I must say, your taste in " +
                    "bagels is utterly appalling!",
                    "emotion": "indignant"
                },
                {
                    "speaker": "Immanuel",
                    "message": "Oh, Don Luis, my friend, you're " +
                    "missing out on the joy of adventurous flavors!",
                    "emotion": "enthusiastic"
                }
            ]
        }
        return json.dumps(dialogue)
