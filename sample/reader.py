import yaml

class Actor:
    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        self.voice_type = data['voice_type']
        self.age = data['age']
        self.height = data['height']
        
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
            l = Location(location)
            self.locations[l.name] = l
            
        
    def get_actors(self):
        return self.actors 
        
    
    def get_scenes(self):
        return self.scenes
    
    
    def get_locations(self):
        return self.locations 
        
    
    def _get_data_element(self, element):
        return self.data[element]
    
    
    def print(self):
        yaml.dump(self.data, default_flow_style=False)