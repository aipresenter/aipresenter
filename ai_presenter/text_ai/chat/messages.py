# import logging
# import openai
import tiktoken
import json

global MAX_TOKEN_LIMIT
global SOFT_TOKEN_LIMIT
MAX_TOKEN_LIMIT = 4096
SOFT_TOKEN_LIMIT = 2500


class Messages:
    def __init__(self, gpt_initializer):
        self.gpt_setup = gpt_initializer
        self.scenes = []
        self.max_token_limit = MAX_TOKEN_LIMIT
        self.soft_token_limit = SOFT_TOKEN_LIMIT

    def update_scenes(self, scene):
        self.token_check()
        s = {"role": "user", "content": json.dumps(scene)}
        self.scenes.append(s)

    def token_check(self):
        while sum(self.count_tokens(scene)
                  for scene in self.scenes) > self.soft_token_limit:
            self.scenes.pop(0)

    def construct(self):
        return self.gpt_setup + self.scenes

    def count_tokens(self, message):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(str(message)))
