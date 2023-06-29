from ai_presenter.database import Database, Scene


class TextAi:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def generate(self, s: Scene) -> str:
        pass
