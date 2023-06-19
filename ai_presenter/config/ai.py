from ai_presenter.config.chatgpt import ChatGPTConfig
import ai_presenter.config.defaults


class AIConfig:
    def __init__(self, data):
        ai_presenter.config.defaults.TEXT_AI_FILE = data['text_ai_filename']
        ai_presenter.config.defaults.VOICE_AI_FILE = data['voice_ai_filename']
        self.chatgptconfig = ChatGPTConfig(data['chatgpt_config'])
