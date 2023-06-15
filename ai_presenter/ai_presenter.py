from ai_presenter.database import Database
from ai_presenter.generators import Generators
import logging


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

        with open('text_ai.txt', 'w') as file:
            textai = self.generator.get_text()
            for key, scene in self.database.scenes.items():
                logging.info(f"******** \nWorking on scene: {scene.name} in " +
                             f"{scene.location}")
                output = AIPresenter.generate_ai(self, scene, textai)
                file.write(output + '\n')
                logging.info(f'got back from textai: {output}')
            # Write a newline character at the end of the file
            file.write("\n")

    def generate_ai(self, scene, textai):
        # go through each scene
        message = ''
        for dialogue in scene.dialogue:
            actor = dialogue['actor']
            text = dialogue['text']
            message += f'{actor} says, \"{text}\". '
        message += "Build a scene from this and make sure to" + \
            " include lots of extensive dialogue and details."
        output = textai.send(message)
        return output
        # chatGPT is fricking amazing
        # working idea rn is feed chat gpt the scene in the format of
        # "{character, description}* are at scene in location.
        # {character says, dialogue}*. Build scene from this and make
        # sure to include lots of intense dialogue and details.
        # provide voice ai with input(filename), output(filename),
        # and configuration(which voice)
