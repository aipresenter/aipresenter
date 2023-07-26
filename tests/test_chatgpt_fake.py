import unittest
from ai_presenter.text_ai.chat.fake import FakeChatGPT
from ai_presenter.text_ai.chat.text import TextChatGPT
from ai_presenter.reader import Reader


class TestFakeChatGPT(unittest.TestCase):
    def testFakeChatGPT(self):
        reader = Reader('tests/text.yml')
        db = reader.get_db()
        fake = FakeChatGPT()
        chatgpt = TextChatGPT(db, True, fake)

        for scene in db.scenes:
            output = chatgpt.generate(scene)
            self.assertNotEqual(output, {})


if __name__ == '__main__':
    unittest.main()
