import yaml
from ai_presenter.database import Database, Actor, Scene
from ai_presenter.config.config import Config


class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self.actors = {}
        self.scenes = {}
        with open(self.file_path, 'r') as file:
            self.data = yaml.safe_load(file)
        self.config = Config(self.data['config'])
        for actor in self.data['actors']:
            a = Actor(actor)
            self.actors[a.name] = a
        for scene in self.data['scenes']:
            s = Scene(scene)
            self.scenes[s.name] = s

    def get_actors(self):
        return self.actors

    def get_scenes(self):
        return self.scenes

    def _get_data_element(self, element):
        return self.data[element]

    def get_db(self):
        return Database(config=self.config,
                        actors=self.actors,
                        scenes=self.scenes,
                        alldata=self.data)

    def print(self):
        yaml.dump(self.data, default_flow_style=False)
