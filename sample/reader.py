import yaml

class Actor:
    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        self.voice_type = data['voice_type']
        self.age = data['age']
        self.height = data['height']
        
class Reader:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self.actors = {}
        with open(self.file_path, 'r') as file:
            self.data = yaml.safe_load(file)
        for actor in self.data['actors']:
            a = Actor(actor)
            self.actors[a.name] = a
            
        
    def get_actors(self):
        return self.actors 
        
    
    def get_scenes(self):
        return self._get_data_element('scenes') 
    
    
    def get_locations(self):
        return self._get_data_element('locations') 
        
    
    def _get_data_element(self, element):
        return self.data[element]
    
    
    def print(self):
        yaml.dump(self.data, default_flow_style=False)