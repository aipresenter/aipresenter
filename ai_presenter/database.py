import logging
import random
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
        try:
            self.name = data['name']
        except KeyError:
            self.name = random.choice(['Alice', 'Bob', 'Charlie'])

        try:
            self.description = data['description']
        except KeyError:
            self.description = random.choice(['An angry antihero',
                                              'A happy hero',
                                              'An evil villain'])

        try:
            self.voice_type = data['voice_type']
        except KeyError:
            self.voice_type = random.choice(['Soprano',
                                             'Alto', 'Tenor', 'Bass'])

        try:
            self.age = int(data['age'])
        except (KeyError, TypeError, ValueError):
            self.age = random.randint(20, 50)

        try:
            self.height = data['height']
        except KeyError:
            self.height = random.choice(['5 feet 8 inches',
                                         '6 feet', '3 feet 2 inches'])

        try:
            self.gender = data['gender']
        except KeyError:
            self.gender = random.choice(['male', 'female'])

        try:
            self.accent = data['accent']
        except KeyError:
            self.accent = random.choice(['american',
                                         'british', 'indian'])
        logging.debug(f'actor: name:{self.name} gender:{self.gender}')


class Scene:
    def __init__(self, data):
        try:
            self.location = data['location']
        except KeyError:
            self.location = random.choice(['Inside', 'Outside',
                                           'The Void'])

        try:
            self.actors = data['characters']
        except KeyError:
            self.actors = random.choice(['Alice', 'Bob', 'Charlie'])

        try:
            self.plot = data['plot']
        except KeyError:
            self.plot = random.choice(['An unexpected twist',
                                       'The introduction of a new villain',
                                       'The story flips on its head'])

        self.alldata = data
        logging.info(f'scene: {self.location}')

    def to_map(self):
        return self.alldata


class Location:
    def __init__(self, data):
        try:
            self.name = data['name']
        except KeyError:
            self.name = random.choice(['Inside', 'Outside',
                                       'The last place you would expect'])

        try:
            self.type = data['type']
        except KeyError:
            self.type = random.choice(['interior', 'exterior'])

        try:
            self.lighting = data['lighting']
        except KeyError:
            self.lighting = random.choice(['Dimly lit',
                                           'Well lit',
                                           'Pitch black'])

        logging.info(f'location: name:{self.name} type:{self.type}')
