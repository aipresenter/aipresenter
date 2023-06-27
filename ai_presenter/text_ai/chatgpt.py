import json
import os
import openai
import logging
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database, Scene
from ai_presenter.tools.json_trim import json_trim
# import ai_presenter.config.env_vars


class TextChatGPT(TextAi):
    def __init__(self, db: Database):
        self.db = db
        self.messages = [
            {
                "role": "system",
                "content": "You will be provided with a set of characters, " +
                "their description, and a scene in JSON format. " +
                "Create dialogue using the plot and characters " +
                "provided and return it in JSON format."
            },
            {
                "role": "assistant",
                "content": '{"dialogue": [{"speaker": "John", ' +
                '"message": "Tim, I must say, your taste in ' +
                'bagels is utterly appalling!"},{"speaker": ' +
                '"Tim", "message": "John, you are right."}]}'
            }

        ]

        self.user_message = {}
        self.user_message['actors'] = self.db.get_data()['actors']

        openai.api_key = os.getenv("CHATGPT_APIKEY")
        # config = self.db.get_config()
        # openai.api_key = config.get_ai_config().get_chatgpt_api_key()

    def generate(self, s: Scene) -> str:
        self.user_message['scene'] = s.to_map()
        self.messages.append(
            {"role": "user", "content": json.dumps(self.user_message)}
        )
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        # clear for next time
        self.messages = []
        self.user_message = {}

        resp = completion.choices[0].message.content
        logging.info("Recieved " + resp)
        resp = json_trim(resp)
        try:
            return json.dumps(json.loads(resp))
        except Exception:
            return "{}"
