import unittest
from ai_presenter.voice_ai.fake import VoiceAIFake
from ai_presenter.reader import Reader


class TestVoiceAIFake(unittest.TestCase):
    def testVoiceAIFake(self):
        input = 'tests/text.yml'
        output = 'tests/output_file.txt'
        x = Reader('tests/text.yml')
        db = x.get_db()

        fake = VoiceAIFake(db)
        fake.generate(input, output)

        with open(input, 'r') as input_file:
            in_data = input_file.read()

        with open(output, 'r') as output_file:
            out_data = output_file.read()

        self.assertEqual(out_data, in_data)


if __name__ == '__main__':
    unittest.main()
