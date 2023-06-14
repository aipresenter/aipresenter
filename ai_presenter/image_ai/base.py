from ai_presenter.database import Database


class ImageAI:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def generate(self):
        pass
