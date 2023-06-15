from ai_presenter.text_ai.base import TextAi
from ai_presenter.voice_ai.base import VoiceAI
from ai_presenter.image_ai.base import ImageAI


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
