import openai
import logging
from ai_presenter.config.env_vars import get_chatgpt_api_key


class BaseChatGPT:
    def __init__(self):
        openai.api_key = get_chatgpt_api_key()

    def create(self, model='', messages=None):
        logging.debug('chatgpt: got all info')
        pass
