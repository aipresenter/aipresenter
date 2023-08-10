import tiktoken
import logging

# the absolute maximum number of tokens that
# can be used in a message for a chatgpt api call
MAX_TOKEN_LIMIT = 4096

# the number of tokens allowed in a message for a chatgpt api call
# before old scenes start getting deleted in order to keep addition
# of new scenes from going over the MAX_TOKEN_LIMIT
SOFT_TOKEN_LIMIT = 2500


class Messages:
    def __init__(self, gpt_initializer: list):
        self.gpt_setup = gpt_initializer
        self.requests = []
        self.responses = []
        self.max_token_limit = MAX_TOKEN_LIMIT
        self.soft_token_limit = SOFT_TOKEN_LIMIT

# scene expected in format of:
# {"role": "user"/"assistant", "content": json.dumps(self.user_message)}
    def append(self, scene: dict):
        self.token_check()

        if scene['role'] == 'assistant':
            self.responses.append(scene)
        elif scene['role'] == 'user':
            self.requests.append(scene)
        else:
            raise Exception('Invalid role. Expected user or assistant')

    def token_check(self):
        while sum(self.count_tokens(scene) for scene in self.requests
                  and self.responses) > self.soft_token_limit:
            logging.debug(f"Messages.token_check: Popping")
            self.responses.pop(0)
            self.requests.pop(0)

    def invariant(self) -> bool:
        return len(self.requests) >= len(self.responses)

# return example:
# {"role": "system", "content": "You do something"}
# {"role": "user", "content": json.dumps(example_request)}
# {"role": "assistant", "content": json.dumps(example_response)}
# {"role": "user", "content": json.dumps(self.user_message_request)}
# {"role": "assistant", "content": json.dumps(self.user_message_response)}
    def construct(self) -> list:
        construct = self.gpt_setup
        # len(responsees) because responses will always be less
        # than or equal to requests
        for i in range(len(self.responses)):
            construct.append(self.requests[i])
            construct.append(self.responses[i])
        logging.debug(f'Messages.construct: Returning {construct}')
        return construct

    def count_tokens(self, message: dict):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(str(message)))

    def get_scene_count(self):
        return len(self.requests) + len(self.responses)
