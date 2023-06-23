from ai_presenter.database import Database


class TextAi:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def send(self, text) -> str:
        pass
