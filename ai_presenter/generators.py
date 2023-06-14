from ai_presenter.text_ai.textbase import TextAi
from ai_presenter.voice_ai.voicebase import VoiceAI
from ai_presenter.image_ai.imagebase import ImageAI


class Generators:
    def __init__(self, t: TextAi, v: VoiceAI, i: ImageAI):
        self.text_ai = t
        self.voice_ai = v
        self.image_ai = i

    def get_text(self) -> TextAi:
        return self.text_ai

    def get_image(self) -> ImageAI:
        return self.image_ai

    def get_voice(self) -> VoiceAI:
        return self.voice_ai
