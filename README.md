# AI Presenter
_aipresenter_ makes it easy to create stories using ChatGPT, for dialogue and scenes, and ElevenLabs, for voice generation. Currently, aipresenter outputs an audio file, but in future releases we would like to output fully integrated video slideshow stories.

## Usage

### Setup
1. Open your terminal or command prompt
2. Create a new directory to house the _aipresenter_ project.

```
mkdir example_project
```

3. Move into that directory

```
cd example_project
```

4. Clone the project's main branch

```
git clone git@github.com:aipresenter/aipresenter.git
```

5. Move into the aipresenter directory
```
cd aipresenter
```

6. Create your virtual environment
```
python3 -m venv venv; source venv/bin/activate
```

7. Update your virtual environment
```
pip install -r requirements.txt
```

8. Create environment variables for the api keys.
```
export CHATGPT_APIKEY=your_chatgpt_api_key
export ELEVENLABS_APIKEY=your_elevenlabs_api_key
```

### Command options
Use `--help` to bring up an option menu:

```
python3 main.py --help
```

Through this interface, _aipresenter_ can be used for:
* script generation from a plot
* dialogue generation from a script
* audio generation from dialogue

## Examples

### script generation
In this example, the plot is used by chatgpt to create a script and return it as `myscript.yml`

```
python3 main.py \
--plot="a plot with 3 scenes about a space war around Europa" \
--script-out=myscript.yml
```

### dialogue and audio generation
In this example, the script is used by chatgpt to generate dialogue, which includes a narrator due to the parameter `--narrator`, then used by elevenlabs to generate an mp3 file of the dialogue

```
python3 main.py \
  --script=myscript.yml \
  --textai=chatgpt \
  --voiceai=elevenlabs \
  --narrator
```

## Audio Examples

#### War over Europa
[![Europa](https://cdn.discordapp.com/attachments/1115278505689747507/1129067341678919810/wimplo517_Spaceship_wars_around_Europa_with_Jupiter_in_the_back_b2ad6e41-0eb6-4977-ace0-bcf6c394fdd3.png)](https://drive.google.com/file/d/1VXl-hQV5pbZoS-pMY3vkvwldIrAKNFbI/view?usp=drive_link)

#### Ants vs Wasps
[![Ants vs Wasps](https://cdn.discordapp.com/attachments/1115278505689747507/1129578047071338606/wimplo517_ants_vs_wasps_in_a_dramatic_style_of_the_film_300_by__555a4ba3-85ea-4cc3-a0f1-52be685dc01d.png)](https://drive.google.com/file/d/1DAtsAJvJv49_SOeqppkgL0rclYAPyRXu/view?usp=drive_link)
