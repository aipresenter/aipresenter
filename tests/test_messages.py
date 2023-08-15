import unittest
from ai_presenter.text_ai.chat.messages import Messages
from ai_presenter.text_ai.chat.messages import MAX_TOKEN_LIMIT
from ai_presenter.text_ai.chat.text_init import INIT_NARRATOR
from ai_presenter.text_ai.chat.fake import FakeChatGPT


class TestMessages(unittest.TestCase):
    def testMessages(self):
        chat = FakeChatGPT()
        messages = Messages(INIT_NARRATOR)
        # tests if new messages class contains just
        # init and that responses and requests are equal
        self.assertEqual(messages.construct(), INIT_NARRATOR)

        buffer = chat.create()
        req = {'role': 'user', 'content': buffer}
        resp = {'role': 'assistant', 'content': buffer}
        testlist = []
        testlist += INIT_NARRATOR
        testlist.append(req)

        messages.append(req)
        print(messages.construct())
        self.assertCountEqual(messages.construct(), testlist)
        messages.append(resp)

        # tests that responses and requests were updated correctly
        self.assertIn('{\'role\': \'user\', \'content\':',
                      str(messages.construct()))
        self.assertIn('{\'role\': \'assistant\', \'content\':',
                      str(messages.construct()))

        for i in range(30):
            messages.append(req)
            messages.append(resp)

        # tests that max token limit isn't breached
        # and that scene popping works correctly
        self.assertLess(messages.count_tokens(
            messages.construct()), MAX_TOKEN_LIMIT)

        # tests that requests and responses are same
        # length after multiple scene pops


if __name__ == '__main__':
    unittest.main()
