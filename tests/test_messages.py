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
        req = {'role': 'user', 'content': resp}

        messages.update_scenes(req)
        messages.update_scenes(
            {'role': 'assistant', 'content': resp}
            )

        self.assertIn('{\'role\': \'user\', \'content\':',
                      str(messages.construct()))
        self.assertIn('{\'role\': \'assistant\', \'content\':',
                      str(messages.construct()))

        for i in range(30):
            resp = chat.create('fake', 'test')
            req = {'role': 'user', 'content': resp}
            messages.update_scenes(req)
            messages.update_scenes(
                {'role': 'assistant', 'content': resp}
            )

        self.assertLess(messages.count_tokens(
            messages.construct()), MAX_TOKEN_LIMIT)

        self.assertEqual(messages.get_scene_count() % 2, 0)


if __name__ == '__main__':
    unittest.main()
