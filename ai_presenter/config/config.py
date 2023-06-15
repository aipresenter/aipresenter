from ai_presenter.config.ai import AIConfig


class Config:
    def __init__(self, data):
        self.ai_config = AIConfig(data['ai_config'])
