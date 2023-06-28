import unittest
import os
from ai_presenter.ai_presenter import AIPresenter
from ai_presenter.reader import Reader
from ai_presenter.text_ai.base import TextAi
from ai_presenter.voice_ai.base import VoiceAI
from ai_presenter.database import Database, Scene
from ai_presenter.generators import Generators


class TestTextAi(TextAi):
    def __init__(self, db: Database, expected_text: str):
        self.expected_text = expected_text
        self.counter = 0
        super().__init__(db)

    def generate(self, s: Scene) -> str:
        self.counter += 1
        return self.expected_text


class TestVoiceAI(VoiceAI):
    def __init__(self, db: Database):
        super().__init__(db)

    def generate(self, input_file, output_file):
        with open(input_file, 'r') as file:
            text = file.read()

        with open(output_file, 'w') as file:
            file.write(text)


class TestAiPresenter(unittest.TestCase):
    def testAiPresenter(self):
        '''
        this test is using fake generator classes to copy
        information from one file to another to compare them
        '''

        reader = Reader('tests/text.yml')
        scenes = reader.get_scenes()
        db = reader.get_db()
        expected = 'HELLO WORLD!'
        text_tester = TestTextAi(db, expected)
        voice_tester = TestVoiceAI(db)
        gen = Generators(text_tester, voice_tester, None)

        presenter = AIPresenter(db, gen)
        presenter.run()
        text_ai_file = db.get_config().get_ai_config().get_text_ai_filename()
        voice_ai_file = db.get_config().get_ai_config().get_voice_ai_filename()

        self.assertTrue(os.path.exists(text_ai_file))
        self.assertEqual(text_tester.counter, len(scenes))
        with open(text_ai_file, 'r') as file:
            for line in file:
                self.assertEqual(expected, line.strip())

        self.assertTrue(os.path.exists(voice_ai_file))
        with open(voice_ai_file, 'r') as file:
            for line in file:
                self.assertEqual(expected, line.strip())


if __name__ == '__main__':
    unittest.main()
