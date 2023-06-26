import json
import os
import openai
import logging
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database
from ai_presenter.tools.json_trim import json_trim
# import ai_presenter.config.env_vars


class TextChatGPT(TextAi):
    def __init__(self, db: Database):
        self.db = db
        openai.api_key = os.getenv("CHATGPT_APIKEY")
        # config = self.db.get_config()
        # openai.api_key = config.get_ai_config().get_chatgpt_api_key()

    def send(self, text) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": text}
            ]
        )
        resp = completion.choices[0].message.content
        logging.info("Recieved " + resp)
        resp = json_trim(resp)
        try:
            return json.dumps(json.loads(resp))
        except Exception:
            return "{}"
