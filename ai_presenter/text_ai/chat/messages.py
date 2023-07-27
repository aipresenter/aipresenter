import logging
import openai
import tiktoken
from ai_presenter.tools.json_trim import json_trim
from ai_presenter.text_ai.chat.base import BaseChatGPT


class Messages:
    def __init__(self, chat_model: BaseChatGPT, gpt_initializer):
        self.gpt_setup = gpt_initializer
        self.scenes = []
        self.max_token_limit = 4096
        self.soft_token_limit = 3000
    
    def update_scenes(self, scene):
        self.token_check()
        self.scenes.append(scene)
    
    def token_check(self):
        while sum(self.count_tokens(scene) 
                  for scene in self.scenes) > self.soft_token_limit:
            self.scenes.pop(0)
    
    def response(self):
        return json_trim(self.gpt_setup) + json_trim(self.scenes)
    
    def count_tokens(self, message):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(message))
