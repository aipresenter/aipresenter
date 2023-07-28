import unittest
from ai_presenter.text_ai.chat.messages import Messages
from ai_presenter.text_ai.chat.messages import MAX_TOKEN_LIMIT
from ai_presenter.text_ai.chat.text_init import INIT_NARRATOR
from ai_presenter.text_ai.chat.fake import FakeChatGPT


class TestMessages(unittest.TestCase):
    def testMessages(self):
        chat = FakeChatGPT()
        messages = Messages(INIT_NARRATOR)
        self.assertEqual(messages.construct(), INIT_NARRATOR)

        resp = chat.create('fake', 'test')
        messages.update_scenes(resp)
        self.assertIn('{\'role\': \'user\', \'content\':',
                      str(messages.construct()))

        for i in range(30):
            resp = chat.create('fake', 'test')
            messages.update_scenes(resp)

        self.assertLess(messages.count_tokens(
            messages.construct()), MAX_TOKEN_LIMIT)


if __name__ == '__main__':
    unittest.main()
