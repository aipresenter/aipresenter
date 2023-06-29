import logging
import argparse
import sys
from ai_presenter.ai_presenter import AIPresenter
from ai_presenter.reader import Reader
# from ai_presenter.text_ai.fake import TextFake
from ai_presenter.image_ai.fake import ImageAIFake
from ai_presenter.ai_presenter import Generators
from ai_presenter.voice_ai.elevenlabs import ElevenLabs
from ai_presenter.text_ai.chatgpt import TextChatGPT

USAGE = '''
Examples:

    python3 main.py --script=myscript.yml
    python3 main.py --help

'''
parser = argparse.ArgumentParser(description='AI Presenter')
parser.add_argument(
    '--script', dest='script', required=True,
    default='', help='Path to the YAML script which contains ' +
    'characters and the plot'
)
args = parser.parse_args()

if args.script == '':
    print("Missing user")
    sys.exit(1)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Program starting")
    reader = Reader(args.script)
    db = reader.get_db()

    text_fake = TextChatGPT(db)
    image_fake = ImageAIFake()
    voice_fake = ElevenLabs(db)
    generator = Generators(text_fake, voice_fake, image_fake)

    ai = AIPresenter(db, generator)

    ai.run()


if __name__ == '__main__':
    main()
