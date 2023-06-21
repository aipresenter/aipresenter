from dotenv import load_dotenv
import os

load_dotenv()

ELEVENLABS_APIKEY = os.getenv('ELEVENLABS_APIKEY')
CHATGPT_APIKEY = os.getenv('CHATGPT_APYKEY')
