# AI Presenter
_aipresenter_ makes it easy to create stories using ChatGPT, for dialogue and scenes, and ElevenLabs, for voice generation. Currently, aipresenter outputs an audio file, but in future releases we would like to output fully integrated video slideshow stories.

## Usage

### Setup
```
python3 -m venv venv
python -m venv venv; source venv/bin/activate
```

### Command options
Use --help to bring up an option menu:
```
python3 main.py --help
```
Through this interface, _aipresenter_ can be used for:
* script generation from a plot
* dialouge generation from a script
* audio generation from dialogue

### Example of script generation
```
python3 main.py --plot="a plot with 3 scenes about a space war around Europa" --script-out=myscript.yml
```

### Example of dialogue and audio generation
```
python3 main.py --script=myscript.yml --textai=chatgpt --voiceai=elevenlabs
--narrator
```

## Audio Examples

#### War over Europa
[![Europa](https://cdn.discordapp.com/attachments/1115278505689747507/1129067341678919810/wimplo517_Spaceship_wars_around_Europa_with_Jupiter_in_the_back_b2ad6e41-0eb6-4977-ace0-bcf6c394fdd3.png)](https://drive.google.com/file/d/1VXl-hQV5pbZoS-pMY3vkvwldIrAKNFbI/view?usp=drive_link)

#### Ants vs Wasps
[![Ants vs Wasps](https://cdn.discordapp.com/attachments/1115278505689747507/1129578047071338606/wimplo517_ants_vs_wasps_in_a_dramatic_style_of_the_film_300_by__555a4ba3-85ea-4cc3-a0f1-52be685dc01d.png)](https://drive.google.com/file/d/1DAtsAJvJv49_SOeqppkgL0rclYAPyRXu/view?usp=drive_link)
