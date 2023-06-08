import ai_presenter

def main():
    reader = ai_presenter.Reader('sample.yml')
    db = reader.get_db()
    
    text_fake = ai_presenter.TextFake()
    image_fake = ai_presenter.ImageAIFake()
    voice_fake = ai_presenter.VoiceAIFake()
    generator = ai_presenter.Generators(text_fake, voice_fake, image_fake)
    
    ai = ai_presenter.AIPresenter(db, generator)




if __name__ == '__main__':
    main()