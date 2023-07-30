import logging
from ai_presenter.text_ai.chat.base import BaseChatGPT
from ai_presenter.text_ai.chat.text_init import PLOT
from ai_presenter.text_ai.chat.messages import Messages


class ScriptChatGPT:
    def __init__(self, chatgpt: BaseChatGPT):
        # chatgpt parameter added for testing purposes
        self.chatgpt = chatgpt
        self.messages = Messages(PLOT)

    def generate(self, plot: str) -> str:
        logging.info("Getting information from Chatgpt...")
        self.messages.update_scenes(request={"role": "user", "content": plot})

        resp = self.chatgpt.create(
            model="gpt-3.5-turbo",
            messages=self.messages.construct(),
        )

        return resp
