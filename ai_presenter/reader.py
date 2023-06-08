import yaml
from ai_presenter.database import Database
from ai_presenter.database import Actor
from ai_presenter.database import Scene
from ai_presenter.database import Location
        
class Reader:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self.actors = {}
        self.scenes = {}
        self.locations = {}
        with open(self.file_path, 'r') as file:
            self.data = yaml.safe_load(file)
        for actor in self.data['actors']:
            a = Actor(actor)
            self.actors[a.name] = a
        for scene in self.data['scenes']:
            s = Scene(scene)
            self.scenes[s.name] = s
        for location in self.data['locations']:
            loc = Location(location)
            self.locations[loc.name] = loc
            
        
    def get_actors(self):
        return self.actors 
        
    
    def get_scenes(self):
        return self.scenes
    
    
    def get_locations(self):
        return self.locations 
        
    
    def _get_data_element(self, element):
        return self.data[element]
    
    
    def get_db(self):
        return Database(self.actors, self.scenes, self.locations)
       
    
    def print(self):
        yaml.dump(self.data, default_flow_style=False)