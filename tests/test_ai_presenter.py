import unittest
import os
from ai_presenter.ai_presenter import AIPresenter
from ai_presenter.reader import Reader
from ai_presenter.text_ai.base import TextAi
from ai_presenter.voice_ai.base import VoiceAI
from ai_presenter.database import Database
from ai_presenter.generators import Generators


class TestTextAi(TextAi):
    def __init__(self, db: Database, expected_text: str):
        self.expected_text = expected_text
        self.counter = 0
        super().__init__(db)

    def send(self, text) -> str:
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
        # this variable is used to counteract the calls made
        # during run setup to text_ai not counting scenes
        setup_calls = 2

        reader = Reader('tests/text.yml')
        # actors = reader.get_actors()
        scenes = reader.get_scenes()
        # loc = reader.get_locations()
        db = reader.get_db()
        expected = 'HELLO WORLD!'
        text_tester = TestTextAi(db, expected)
        voice_tester = TestVoiceAI(db)
        gen = Generators(text_tester, voice_tester, None)

        presenter = AIPresenter(db, gen)
        # self.assertFalse(os.path.exists('text_ai.txt'))
        presenter.run()
        self.assertTrue(os.path.exists('text_ai.txt'))
        self.assertEqual(text_tester.counter, len(scenes) + setup_calls)
        with open('text_ai.txt', 'r') as file:
            for line in file:
                self.assertEqual(expected, line.strip())

        self.assertTrue(os.path.exists('text_ai.txt'))
        with open('voice_ai.txt', 'r') as file:
            for line in file:
                self.assertEqual(expected, line.strip())


if __name__ == '__main__':
    unittest.main()
