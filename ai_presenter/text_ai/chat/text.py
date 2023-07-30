import json
import logging
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database, Scene
from ai_presenter.tools.json_trim import json_trim
from ai_presenter.text_ai.chat.base import BaseChatGPT
from ai_presenter.text_ai.chat.text_init import INIT_NARRATOR
from ai_presenter.text_ai.chat.text_init import INIT_NO_NARRATOR
from ai_presenter.text_ai.chat.messages import Messages


# in the __init__ for this class,
# add openai.api_key = config.get_ai_config().get_chatgpt_api_key()
class TextChatGPT(TextAi):
    def __init__(self, db: Database, use_narrator: bool, chatgpt: BaseChatGPT):
        # chatgpt parameter added for testing purposes
        self.chatgpt = chatgpt
        self.db = db
        logging.debug(f'Narrator is {use_narrator}')
        if use_narrator:
            self.messages = Messages(INIT_NARRATOR)
        else:
            self.messages = Messages(INIT_NO_NARRATOR)
        self.user_message = {}
        self.user_message['actors'] = self.db.get_data()['actors']

    def generate(self, s: Scene) -> str:
        self.user_message['scene'] = s.to_map()
        self.messages.update_scenes(
            {"role": "user", "content": json.dumps(self.user_message)}
        )
        resp = self.chatgpt.create(
            model="gpt-3.5-turbo",
            messages=self.messages.construct(),
        )
        # clear for next time
        # self.messages = []
        self.user_message = {}

        self.messages.update_scenes(
            {"role": "assistant", "content": resp}
        )
        logging.info("Recieved " + resp)
        resp = json_trim(resp)
        try:
            return json.dumps(json.loads(resp))
        except Exception:
            print(json.dumps(json.loads(resp)), file="debug.txt")
            print("\n")
            return "{}"
