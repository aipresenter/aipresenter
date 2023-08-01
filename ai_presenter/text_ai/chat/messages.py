import tiktoken

# the absolute maximum number of tokens that
# can be used in a message for a chatgpt api call
MAX_TOKEN_LIMIT = 4096

# the number of tokens allowed in a message for a chatgpt api call
# before old scenes start getting deleted in order to keep addition
# of new scenes from going over the MAX_TOKEN_LIMIT
SOFT_TOKEN_LIMIT = 2500


class Messages:
    def __init__(self, gpt_initializer):
        self.gpt_setup = gpt_initializer
        self.scenes = []
        self.requests = []
        self.responses = []
        self.max_token_limit = MAX_TOKEN_LIMIT
        self.soft_token_limit = SOFT_TOKEN_LIMIT

    def update_scenes(self, scene):
        self.token_check()
        if scene['role'] == 'assistant':
            self.responses.append(scene)
        if scene['role'] == 'user':
            self.requests.append(scene)
        self.scenes.append(scene)

    def token_check(self):
        while sum(self.count_tokens(scene) for scene in self.requests
                  and self.responses) > self.soft_token_limit:
            self.responses.pop(0)
            self.requests.pop(0)

    def construct(self):
        construct = self.gpt_setup
        for i in range(self.requests.__len__()):
            construct += self.requests[i]
            construct += self.responses[i]
        return construct

    def count_tokens(self, message):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(str(message)))

    def get_scene_count(self):
        return self.scenes.__len__()
