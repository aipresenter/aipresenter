from dotenv import load_dotenv
load_dotenv()
import os

ELEVENLABS_APIKEY = os.getenv('ELEVENLABS_APIKEY')
CHATGPT_APIKEY = os.getenv('CHATGPT_APYKEY')
