from ai_presenter.database import Database
import logging


class TextAi:
    def __init__(self, db: Database):
        self.actors = db.actors
        self.scenes = db.scenes
        self.locations = db.locations

    def generate(self):
        pass
    
    def send(self, text) -> str:
        pass


class TextFake(TextAi):
    def __init__(self, db: Database):
        super().__init__(db)

    def generate(self):
        pass
    
    def send(self, text) -> str:
        logging.info(f"textfake: Sending {text}")
        return "text fake hehe"


class TextChatGPT(TextAi):
    def __init__(self, db: Database):
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
        self.database = db
        self.generator = g

    def run(self):
        logging.info("it runs")
        textai = self.generator.get_text()
        textai.send(self.database.config.ai_config.chatgptconfig.style)
        
        message = ''
        for key, actor in self.database.actors.items():
            message += f'{actor.name} is a {actor.age} year old {actor.gender}, {actor.description}. '
        textai.send(message)
        
        # go through each scene
        for key, scene in self.database.scenes.items():
            logging.info(f"** Working on scene:{scene.name} in {scene.location}")
            message = ''
            for dialogue in scene.dialogue:
                actor = dialogue['actor']
                text = dialogue['text']
                message += f'{actor} says, {text}. '
            message += 'Build a scene from this and make sure to include lots of extensive dialogue and details.'
            output = textai.send(message)
            logging.info(f'got back from textai: {output}')
        # chatGPT is fricking amazing
        # working idea rn is feed chat gpt the scene in the format of
        # "{character, description}* are at scene in location.
        # {character says, dialogue}*. Build scene from this and make
        # sure to include lots of intense dialogue and details.
