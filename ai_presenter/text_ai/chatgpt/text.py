import json
import logging
from ai_presenter.text_ai.base import TextAi
from ai_presenter.database import Database, Scene
from ai_presenter.tools.json_trim import json_trim
from ai_presenter.text_ai.chatgpt.chatgpt import ChatGPT
# import ai_presenter.config.env_vars


# in the __init__ for this class,
# add openai.api_key = config.get_ai_config().get_chatgpt_api_key()
class TextChatGPT(TextAi):
    def __init__(self, db: Database):
        self.chatgpt = ChatGPT(db)
        self.db = db
        self.messages = [
            {
                "role": "system",
                "content": "You will be provided with a set of characters, " +
                "their description, and a scene in JSON format. " +
                "Create dialogue using the plot and characters " +
                "provided and return it in JSON format.  Add a narrator" +
                " with key 'narrator' describing the characters, scene," +
                " and emotions."
            },
            {
                "role": "user",
                "content": '{"characters":[{"name":"Max Doe",' +
                '"description":"A charismatic detective",' +
                '"voice_type":"Baritone","age":35,"height":' +
                '"6 feet","gender":"male"},{"name":"Joana Smith",' +
                '"description":"A brilliant scientist","voice_type":' +
                '"Soprano","age":28,"height":"5 feet 8 inches","gender"' +
                ':"female"}],"scene":{"location":"Lobby","characters"' +
                ':["Max Doe","Joana Smith"],"plot":"Max Doe thinks ' +
                'he is right."}}'
            },
            {
                "role": "assistant",
                "content": '{"dialogue":[{"speaker":"narrator","message": ' +
                '"Max stood close to Joana."},{"speaker":"Max Doe",' +
                '"message":"Joana, I must say, your taste in bagels is ' +
                'utterly appalling!"},{"speaker":"Joana Smith",' +
                '"message":"Max, you are right."},{"speaker":"narrator",' +
                '"message":"Finally Max was happy."}]}'
            }

        ]

        self.user_message = {}
        self.user_message['actors'] = self.db.get_data()['actors']

    def generate(self, s: Scene) -> str:
        self.user_message['scene'] = s.to_map()
        self.messages.append(
            {"role": "user", "content": json.dumps(self.user_message)}
        )
        resp = self.chatgpt.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        # clear for next time
        # self.messages = []
        self.user_message = {}

        self.messages.append(
            {"role": "assistant", "content": resp}
        )
        logging.info("Recieved " + resp)
        resp = json_trim(resp)
        try:
            return json.dumps(json.loads(resp))
        except Exception:
            return "{}"
