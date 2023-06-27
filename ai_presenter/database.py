from ai_presenter.config.config import Config


class Database:
    def __init__(
            self, actors=None, scenes=None,
            locations=None, config=None, alldata=None
            ):
        self.actors = actors
        self.scenes = scenes
        self.locations = locations
        self.config = config
        self.alldata = alldata

    def get_config(self) -> Config:
        return self.config

    def get_data(self):
        return self.alldata


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
        self.name = data['location']
        self.location = data['location']
        self.actors = data['characters']
        self.plot = data['plot']
        self.alldata = data

    def to_map(self):
        return self.alldata


class Location:
    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.lighting = data['lighting']
