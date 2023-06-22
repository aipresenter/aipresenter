import unittest
from ai_presenter.voice_ai.fake import VoiceAIFake
from ai_presenter.reader import Reader
from ai_presenter.text_ai.fake import TextFake


class TestVoiceAIFake(unittest.TestCase):
    def testVoiceAIFake(self):
        input = 'tests/text.json'
        output = 'tests/output_file.txt'
        x = Reader('tests/text.yml')
        db = x.get_db()

        voice_fake = VoiceAIFake(db)
        text_fake = TextFake(db)
        with open(input, 'w') as file:
            file.write(text_fake.send("fake text"))

        voice_fake.generate(input, output)

        with open(input, 'r') as input_file:
            in_data = input_file.read()

        with open(output, 'r') as output_file:
            out_data = output_file.read()

        self.assertIn('name', out_data)
        self.assertIn('name', in_data)
        self.assertIn('gender', out_data)
        self.assertIn('age', out_data)
        self.assertIn('age', in_data)
        self.assertIn('accent', out_data)
        self.assertIn('accent strength', out_data)
        self.assertIn('description', out_data)
        self.assertIn('message', in_data)


if __name__ == '__main__':
    unittest.main()
