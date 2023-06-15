from ai_presenter.config.chatgpt import ChatGPTConfig


class AIConfig:
    def __init__(self, data):
        self.chatgptconfig = ChatGPTConfig(data['chatgpt_config'])
