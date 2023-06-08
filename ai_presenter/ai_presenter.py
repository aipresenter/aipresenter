from ai_presenter.database import Database


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
    
    
    
class Generators:
    
    def __init__(self, t: TextAi, v: VoiceAI, i: ImageAI):
        self.text_ai = t
        self.voice_ai = v
        self.image_ai = i
    
    
    def get_text(self) -> TextAi:
        return self.text_ai
    
    
    def get_image(self) -> ImageAI:
        return self.image_ai
    
    
    def get_voice(self) -> VoiceAI:
        return self.voice_ai
    
    
class AIPresenter:
    def __init__(self, db: Database, g: Generators):
        pass
    
    
    def run(self):
        pass