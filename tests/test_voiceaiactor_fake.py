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
        correct_output = 'name: John Doe\ngender: Gender.male\n' + \
            'age: Age.middle_aged\naccent: Accent.american\n' + \
            'accent strength: 1.99\n' + \
            f'description: {description}\n' + \
            'message: Hi, I\'m an actor\n\n'

        self.assertEqual(output, correct_output)


if __name__ == '__main__':
    unittest.main()
