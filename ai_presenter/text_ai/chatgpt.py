import os
import openai
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database


class TextChatGPT(TextAi):
    def __init__(self, db: Database):
        pass

    def generate(self):
        openai.api_key = os.getenv("CHATGPT_APIKEY")
        completion  = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.}
            ]
        )
        
