from ai_presenter.database import Database
from ai_presenter.text_ai.textbase import TextAi
from ai_presenter.voice_ai.voicebase import VoiceAI
from ai_presenter.image_ai.imagebase import ImageAI
import logging


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
            message += f'{actor.name} is a {actor.age} year old' + \
                f' {actor.gender}, {actor.description}. '
        textai.send(message)

        # go through each scene
        for key, scene in self.database.scenes.items():
            logging.info(f"********* \nWorking on scene: {scene.name} in " +
                         f"{scene.location}")
            message = ''
            for dialogue in scene.dialogue:
                actor = dialogue['actor']
                text = dialogue['text']
                message += f'{actor} says, \"{text}\". '
            message += "Build a scene from this and make sure to" + \
                " include lots of extensive dialogue and details."
            output = textai.send(message)
            logging.info(f'got back from textai: {output}')
        # chatGPT is fricking amazing
        # working idea rn is feed chat gpt the scene in the format of
        # "{character, description}* are at scene in location.
        # {character says, dialogue}*. Build scene from this and make
        # sure to include lots of intense dialogue and details.
        # provide voice ai with input(filename), output(filename),
        # and configuration(which voice)
