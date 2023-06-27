import unittest
from ai_presenter.voice_ai.fake import VoiceAIActorFake
from ai_presenter.config.voice import VoiceConfig
from elevenlabs import Gender, Age, Accent


class TestVoiceAIActorFake(unittest.TestCase):
    def testVoiceAIActorFake(self):
        description = "A charismatic detective"
        config = VoiceConfig('John Doe', Gender.male, Age.middle_aged,
                             Accent.american, 1.99, description)
        actor = VoiceAIActorFake(config)

        output = actor.says("Hi, I'm an actor", "Determined")

        self.assertIn('name', output)
        self.assertIn('gender', output)
        self.assertIn('age', output)
        self.assertIn('accent', output)
        self.assertIn('accent strength', output)
        self.assertIn('description', output)
        self.assertIn('message', output)


if __name__ == '__main__':
    unittest.main()
