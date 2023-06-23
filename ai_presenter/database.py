from ai_presenter.config.config import Config


class Database:
    def __init__(self, actors=None, scenes=None, locations=None, config=None):
        self.actors = actors
        self.scenes = scenes
        self.locations = locations
        self.config = config

    def get_config(self) -> Config:
        return self.config


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
