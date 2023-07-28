import logging
import json
from ai_presenter.text_ai.chat.base import BaseChatGPT


class FakeChatGPT(BaseChatGPT):
    def __init__(self):
        super().__init__()

    def create(self, model='', messages=None):
        logging.debug('chatgpt: got all info')
        dialogue = {
            "dialogue": [
                {
                    "speaker": "John Doe",
                    "message": "Listen, Michael. We know you're involved" +
                    "in this. Just tell us the truth and it will go" +
                    "easier for you."
                },
                {
                    "speaker": "Jane Smith",
                    "message": "John's right, Michael. We have evidence" +
                    "against you. It's better if you cooperate and confess."
                },
                {
                    "speaker": "Michael Johnson",
                    "message": "I swear, I didn't do anything! You've got" +
                    "the wrong person! I demand to speak to my lawyer!"
                },
                {
                    "speaker": "John Doe",
                    "message": "Alright, Michael. If you're innocent, we'll" +
                    "find out. But until then, you're staying right here."
                }
            ]
        }

        try:
            return json.dumps(dialogue)
        except Exception:
            return "{}"
