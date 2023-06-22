from ai_presenter.database import Database
from ai_presenter.generators import Generators
import logging
from ai_presenter.voice_ai.base import VoiceAI


class AIPresenter:
    def __init__(self, db: Database, g: Generators):
        self.database = db
        self.generator = g

    def run(self):
        self.__run_text_ai()
        self.__run_voice_ai()

    def __run_text_ai(self):
        logging.info("running text ai")
        # calls get_text and puts it into textai
        textai = self.generator.get_text()
        # sends textai to chatgtp config
        textai.send(self.database.config.ai_config.chatgptconfig.style)
        # creates a message string variable
        message = ''
        # goes through each actor
        for key, actor in self.database.actors.items():
            message += f'{actor.name} is a {actor.age} year old' + \
                f' {actor.gender}, {actor.description}.'
        # sends message to ai in given format
        textai.send(message)

        config = self.database.get_config()
        text_ai_file = config.get_ai_config().get_text_ai_filename()

        with open(text_ai_file, 'w') as file:
            textai = self.generator.get_text()
            for key, scene in self.database.scenes.items():
                logging.info(f"******** \nWorking on scene: {scene.name} in " +
                             f"{scene.location}")
                output = self.__get_scene_text(scene, textai)
                file.write(output + '\n')
                logging.info(f'got back from textai: {output}')

    def __run_voice_ai(self):
        voiceai = VoiceAI(self.database)
        voiceai.generate('text_ai.txt', 'voice_ai.txt')

    def __get_scene_text(self, scene, textai):
        # go through each scene
        message = ''
        for dialogue in scene.dialogue:
            actor = dialogue['actor']
            text = dialogue['text']
            message += f'{actor} says, \"{text}\". '
            message += "Build a scene from this and make sure to " + \
                "include lots of extensive dialogue and " + \
                "details, and return a JSON of the " + \
                "dialogue containing the characters (their " + \
                "name and personality, and emotion), and the dialogue " + \
                "(speaker, message, and the emotion)"

        output = textai.send(message)
        return output
        # chatGPT is fricking amazing
        # working idea rn is feed chat gpt the scene in the format of
        # "{character, description}* are at scene in location.
        # {character says, dialogue}*. Build scene from this and make
        # sure to include lots of intense dialogue and details.
        # provide voice ai with input(filename), output(filename),
        # and configuration(which voice)
