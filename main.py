from ai_presenter.ai_presenter import AIPresenter
from ai_presenter.reader import Reader
from ai_presenter.ai_presenter import TextFake
from ai_presenter.ai_presenter import ImageAIFake
from ai_presenter.ai_presenter import Generators
from ai_presenter.ai_presenter import VoiceAIFake
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Program starting")
    reader = Reader('sample.yml')
    db = reader.get_db()

    text_fake = TextFake(db)
    image_fake = ImageAIFake()
    voice_fake = VoiceAIFake()
    generator = Generators(text_fake, voice_fake, image_fake)

    ai = AIPresenter(db, generator)

    ai.run()


if __name__ == '__main__':
    main()
