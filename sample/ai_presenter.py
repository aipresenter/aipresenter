from sample.database import Database


class TextAi:
    def __init__ (self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations


    def generate(self):
        pass


class TextFake(TextAi):
    def __init__ (self):
        pass


    def generate(self):
        pass


class TextChatGPT(TextAi):
    def __init__ (self, db: Database):
        pass


    def generate(self):
        pass
    
    
class VoiceAI:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations
    
    
    def generate(self):
        pass
    
    
class ImageAI:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations
        
        
    def generate(self):
        pass
    
    
class VoiceAIFake(VoiceAI):
    def __init__(self):
        pass
    
    
    def generate(self):
        pass
    
    
class ImageAIFake(ImageAI):
    def __init__(self):
        pass
    
    
    def generate(self):
        pass    
    
    
    
class Generator:
    
    def __init__(self, t: TextAi, v: VoiceAI, i: ImageAI):
        self.text_ai = t
        self.voice_ai = v
        self.image_ai = i
    
    
    def get_text(self):
        return self.text_ai.generate()
    
    
    def get_image(self):
        return self.image_ai.generate()
    
    
    def get_voice(self):
        return self.voice_ai.generate()