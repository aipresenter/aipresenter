
# VoiceConfig can have passed in name, gender, age,
# accent, and accent_strength and have these initialized
class VoiceConfig:
    def __init__(self, name='', gender='', age='', accent='',
                 accent_strength=0, description=''):
        self.name = name
        self.gender = gender
        self.age = age
        self.accent = accent
        self.accent_strength = accent_strength
        self.description = description
