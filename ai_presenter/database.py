class Database:
    def __init__(self, actors=None, scenes=None, locations=None, config=None):
        self.actors = actors
        self.scenes = scenes
        self.locations = locations
        self.config = config


class Actor:
    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        self.voice_type = data['voice_type']
        self.age = data['age']
        self.height = data['height']
        self.gender = data['gender']


class Scene:
    def __init__(self, data):
        self.name = data['name']
        self.location = data['location']
        self.actors = data['actors']
        self.dialogue = data['dialogue']


class Location:
    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.lighting = data['lighting']


class Config:
    def __init__(self, data):
        self.ai_config = AIConfig(data['ai_config'])


class AIConfig:
    def __init__(self, data):
        self.chatgptconfig = ChatGPTConfig(data['chatgpt_config'])


class ChatGPTConfig:
    def __init__(self, data):
        self.style = data['style']
