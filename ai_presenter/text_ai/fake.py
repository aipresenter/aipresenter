import logging
import json
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database


class TextFake(TextAi):
    def __init__(self, db: Database):
        super().__init__(db)

    def generate(self, text) -> str:
        logging.info(f"textfake: Sending {text}")
        dialogue = {
            "characters": [
                {
                    "name": "John Doe",
                    "personality": "authoritative and stubborn",
                    "emotion": "stubborn"
                },
                {
                    "name": "Jane Smith",
                    "personality": "boisterous and foolheaded",
                    "emotion": "cheerful"
                },
                {
                    "name": "Michael Johnson",
                    "personality": "determined and informative",
                    "emotion": "calm"
                }
            ],
            "dialogue": [
                {
                    "speaker": "John Doe",
                    "message": "Immanuel, I must say, your taste in " +
                    "bagels is utterly appalling!",
                    "emotion": "indignant"
                },
                {
                    "speaker": "Jane Smith",
                    "message": "Oh, Don Luis, my friend, you're " +
                    "missing out on the joy of adventurous flavors!",
                    "emotion": "enthusiastic"
                },
                {
                    "speaker": "Michael Johnson",
                    "message": "The argument continues heatedly",
                    "emotion": "descriptive"
                }
            ]
        }
        return json.dumps(dialogue)
