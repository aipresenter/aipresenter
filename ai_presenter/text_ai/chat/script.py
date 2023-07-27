import logging
from ai_presenter.text_ai.chat.base import BaseChatGPT


class ScriptChatGPT:
    def __init__(self, chatgpt: BaseChatGPT):
        # chatgpt parameter added for testing purposes
        self.chatgpt = chatgpt
        self.messages = [
            {
                "role": "system",
                "content": "You create plots with " +
                "characters and output in YAML",
            },
            {
                "role": "user",
                "content": "a plot with 4 scenes about a " +
                "space war in Europa",
            },
            {
                "role": "assistant",
                "content": '''
config:
  ai_config:
    text_ai_filename: europa.txt
    voice_ai_filename: europa.mp3
    chatgpt_config:
      style: you are a suspenseful storyteller
actors:
  - name: Captain Ryan Thompson
    description: fearless leader of a space fleet
    voice_type: unused
    age: 40
    height: 6 feet
    gender: male
    accent: american
  - name: Lieutenant Ava Ramirez
    description: brilliant pilot and strategist
    voice_type: unused
    age: 23
    height: 5 feet 5 inches
    gender: female
    accent: american
  - name: Sergeant Marcus Chen
    description: skilled technician and weapons expert
    voice_type: unused
    age: 55
    height: 5 feet 10 inches
    gender: male
    accent: english
  - name: Dr. Sophia Collins
    description: brilliant scientist specializing in alien life forms
    voice_type: unused
    age: 36
    height: 5 feet 8 inches
    gender: female
    accent: british
locations:
  - name: Spaceship Bridge
    type: interior
    lighting: Dimly lit
scenes:
  - location: Spaceship Bridge
    characters:
      - Captain Ryan Thompson
      - Lieutenant Ava Ramirez
      - Sergeant Marcus Chen
      - Dr. Sophia Collins
    plot: The team receives a distress signal from a research outpost.
  - location: Europa's Orbit
    characters:
      - Captain Ryan Thompson
      - Lieutenant Ava Ramirez
      - Dr. Sophia Collins
    plot: As they approach Europa, their ship is attacked by unknown alien.
  - location: Europa's Surface
    characters:
      - Captain Ryan Thompson
      - Sergeant Marcus Chen
      - Dr. Sophia Collins
    plot: The team lands on Europa's icy surface and makes their way.
  - location: Europa Research Outpost
    characters:
      - Captain Ryan Thompson
      - Lieutenant Ava Ramirez
      - Sergeant Marcus Chen
      - Dr. Sophia Collins
    plot: They reach the research outpost, but they find it's been overrun.
'''
            },
        ]

    def generate(self, plot: str) -> str:
        logging.info("Getting information from Chatgpt...")
        self.messages.append(
            {"role": "user", "content": plot},
        )

        resp = self.chatgpt.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )

        return resp
