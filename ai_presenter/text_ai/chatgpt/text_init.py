global INIT_NARRATOR
global INIT_NO_NARRATOR
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
