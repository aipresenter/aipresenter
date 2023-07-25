import openai
import logging
import json
from ai_presenter.config.env_vars import get_chatgpt_api_key


class ChatFake:
    def __init__(self) -> None:
        openai.api_key = get_chatgpt_api_key()

    def create(self, model='', messages=None):
        logging.debug('chatgpt: got all info')
#         print(json.dumps(messages))
        return json.dumps(messages)
