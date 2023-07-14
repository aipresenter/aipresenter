from ai_presenter.config.chatgpt import ChatGPTConfig
from ai_presenter.config.defaults import TEXT_AI_FILE, VOICE_AI_FILE
from ai_presenter.config.env_vars import ELEVENLABS_APIKEY, CHATGPT_APIKEY


class AIConfig:
    def __init__(self, data):
        try:
            self.text_ai_filename = data['text_ai_filename']
        except Exception:
            self.text_ai_filename = TEXT_AI_FILE

        try:
            self.voice_ai_filename = data['voice_ai_filename']
        except Exception:
            self.voice_ai_filename = VOICE_AI_FILE

    def get_text_ai_filename(self) -> str:
        return self.text_ai_filename

    def get_voice_ai_filename(self) -> str:
        return self.voice_ai_filename

    def get_elevenlabs_api_key(self) -> str:
        if ELEVENLABS_APIKEY is None or ELEVENLABS_APIKEY == '':
            raise Exception("Elevenlabs api key missing." +
                            " Use envar ELEVENLABS_APIKEY")
        return ELEVENLABS_APIKEY

    def get_chatgpt_api_key(self) -> str:
        if CHATGPT_APIKEY is None or CHATGPT_APIKEY == '':
            raise Exception("Chatgpt api key missing." +
                            " Use envar CHATGPT_APIKEY")
        return CHATGPT_APIKEY
