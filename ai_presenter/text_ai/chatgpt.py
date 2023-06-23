import json
import openai
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database
import ai_presenter.config.env_vars


class TextChatGPT(TextAi):
    def __init__(self, db: Database):
        self.db = db
        config = self.db.get_config()
        openai.api_key = config.get_ai_config().get_chatgpt_api_key()

    def send(self, text) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": text}
            ]
        )
        return json.dumps(json.loads(completion))
