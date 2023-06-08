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