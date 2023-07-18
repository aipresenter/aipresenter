import logging
import argparse
import sys
import os
from ai_presenter.ai_presenter import AIPresenter
from ai_presenter.reader import Reader
from ai_presenter.text_ai.fake import TextFake
from ai_presenter.image_ai.fake import ImageAIFake
from ai_presenter.ai_presenter import Generators
from ai_presenter.voice_ai.elevenlabs import ElevenLabs
from ai_presenter.voice_ai.fake import VoiceAIFake
from ai_presenter.text_ai.chatgpt.text import TextChatGPT
from ai_presenter.text_ai.chatgpt.script import ScriptChatGPT


USAGE = '''
Examples:

    python3 main.py --script=myscript.yml
    python3 main.py --help

'''
parser = argparse.ArgumentParser(description='AI Presenter')
parser.add_argument(
    '--script', dest='script',
    default='', help='Path to the YAML script which contains ' +
    'characters and the plot'
)
parser.add_argument(
    '--json', dest='json', type=str, default='',
    help='Path to JSON file that will be used to generate audio'
)
parser.add_argument(
    '--textai', dest='textai', default='fake',
    help='Use chatgpt or fake'
)
parser.add_argument(
    '--voiceai', dest='voiceai', default='fake',
    help='Use elevenlabs or fake'
)
parser.add_argument(
    '--debug', dest='debug', default=False,
    help='Debugging log level'
)
parser.add_argument(
    '--plot', dest='plot',
    default='', help='Plot to send to ChatGPT to create scenes',
)
parser.add_argument(
    '--script-out', dest='scriptout',
    default='', help='Path to the YAML script to write',
)
args = parser.parse_args()


def main():
    if args.plot != '':
        if args.scriptout == '':
            print("Missing output script file")
            sys.exit(1)
        gpt = ScriptChatGPT()
        with open(args.scriptout, 'w') as file:
            file.write(gpt.generate(args.plot) + '\n')
        logging.info("Done")
        sys.exit(0)

    if args.script == '':
        print("Missing script file")
        sys.exit(1)

    valid_text_options = ['chatgpt', 'fake']
    if args.textai not in valid_text_options:
        print("Please provide a valid option:" +
              "chatgpt or fake")
        sys.exit(1)

    valid_voice_options = ['elevenlabs', 'fake']
    if args.voiceai not in valid_voice_options:
        print("Please provide a valid option:" +
              "elevenlabs or fake")
        sys.exit(1)

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("Program starting")
    reader = Reader(args.script)
    db = reader.get_db()

    if args.textai == 'chatgpt':
        textai = TextChatGPT(db)
    else:
        textai = TextFake(db)
    if args.voiceai == 'elevenlabs':
        voiceai = ElevenLabs(db)
    else:
        voiceai = VoiceAIFake(db)

    image_fake = ImageAIFake()
    generator = Generators(textai, voiceai, image_fake)
    ai = AIPresenter(db, generator)

    if args.json != '' and os.path.exists(args.json):
        ai.json_run(args.json)
        sys.exit(0)

    ai.run()


if __name__ == '__main__':
    main()
