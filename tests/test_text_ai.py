import unittest
from ai_presenter.text_ai.chat.fake import FakeChatGPT
from ai_presenter.text_ai.chat.text import TextChatGPT
from ai_presenter.reader import Reader


class TestTextAI(unittest.TestCase):
    def testTextAi(self):
        r = Reader('tests/text.yml')
        db = r.get_db()
        fakegpt = FakeChatGPT()
        textai = TextChatGPT(db, True, fakegpt)
        # check if messages is recieving proper input
        for scene in db.scenes:
            output = textai.generate(scene)
            output
            # why is chatgpt now returning the sample respnse as
            # the first scene?
            # why is chatgpt repeating scenes
            # added messages and thats when poop hit the fan
            # even during runs when messages did not pop, chatgpt still
            # returned sample input as first scene and repeated scenes
            # therefore popping scenes is not what is causing chatgpt
            # to repeat scenes/other funky business
            # given that append() and construct() are the methods used
            # 100% of all runs, error must be in there

        # check if messages is popping correctly
        # check if messages is updating the list properly


if __name__ == '__main__':
    unittest.main()
