global INIT_NARRATOR
global INIT_NO_NARRATOR
global PLOT
INIT_NARRATOR = [
            {
                "role": "system",
                "content": "You will be provided with a set of characters, " +
                "their description, and a scene in JSON format. " +
                "Create dialogue using the plot and characters " +
                "provided and return it in JSON format.  Add a narrator" +
                " with key 'narrator' describing the characters, scene," +
                " and emotions."
            },
            {
                "role": "user",
                "content": '{"characters":[{"name":"Max Doe",' +
                '"description":"A charismatic detective",' +
                '"voice_type":"Baritone","age":35,"height":' +
                '"6 feet","gender":"male"},{"name":"Joana Smith",' +
                '"description":"A brilliant scientist","voice_type":' +
                '"Soprano","age":28,"height":"5 feet 8 inches","gender"' +
                ':"female"}],"scene":{"location":"Lobby","characters"' +
                ':["Max Doe","Joana Smith"],"plot":"Max Doe thinks ' +
                'he is right."}}'
            },
            {
                "role": "assistant",
                "content": '{"dialogue":[{"speaker":"narrator","message": ' +
                '"Max stood close to Joana."},{"speaker":"Max Doe",' +
                '"message":"Joana, I must say, your taste in bagels is ' +
                'utterly appalling!"},{"speaker":"Joana Smith",' +
                '"message":"Max, you are right."},{"speaker":"narrator",' +
                '"message":"Finally Max was happy."}]}'
            }

        ]

INIT_NO_NARRATOR = [
            {
                "role": "system",
                "content": "You will be provided with a set of characters, " +
                "their description, and a scene in JSON format. " +
                "Create dialogue using the plot and characters " +
                "provided and return it in JSON format."
            },
            {
                "role": "user",
                "content": '{"characters":[{"name":"Max Doe",' +
                '"description":"A charismatic detective",' +
                '"voice_type":"Baritone","age":35,"height":' +
                '"6 feet","gender":"male"},{"name":"Joana Smith",' +
                '"description":"A brilliant scientist","voice_type":' +
                '"Soprano","age":28,"height":"5 feet 8 inches","gender"' +
                ':"female"}],"scene":{"location":"Lobby","characters"' +
                ':["Max Doe","Joana Smith"],"plot":"Max Doe thinks ' +
                'he is right."}}'
            },
            {
                "role": "assistant",
                "content": '{"dialogue":[{"speaker":"Max Doe",' +
                '"message":"Joana, I must say, your taste in bagels is ' +
                'utterly appalling!"},{"speaker":"Joana Smith",' +
                '"message":"Max, you are right."}]}'
            }

        ]

PLOT = [
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
    age: middle_aged
    height: 6 feet
    gender: male
    accent: american
  - name: Lieutenant Ava Ramirez
    description: brilliant pilot and strategist
    voice_type: unused
    age: young
    height: 5 feet 5 inches
    gender: female
    accent: american
  - name: Sergeant Marcus Chen
    description: skilled technician and weapons expert
    voice_type: unused
    age: old
    height: 5 feet 10 inches
    gender: male
    accent: english
  - name: Dr. Sophia Collins
    description: brilliant scientist specializing in alien life forms
    voice_type: unused
    age: middle_aged
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
