import yaml

class Reader:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.actors = {}
        self.scenes = {}
        self.locations = {}
    
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = yaml.safe_load(file)
                return self.data
        except FileNotFoundError:
            return "File not found."
        
        
    def get_actors(self):
        i = 0
        for actor in self.data['actors']:
            self.actors[i] = actor
            i = i + 1
        return self.actors
                 
    def get_scenes(self):
        i = 0
        for scene in self.data['scenes']:
            self.scenes[i] = scene
            i = i + 1
        return self.scenes 
    
    def get_locations(self):
        i = 0
        for location in self.data['locations']:
            self.locations[i] = location
            i = i + 1
        return self.locations 
        
    ## def print(self):