from dotenv import load_dotenv
import os

load_dotenv()

ELEVENLABS_APIKEY = os.getenv('ELEVENLABS_APIKEY')
CHATGPT_APIKEY = os.getenv('CHATGPT_APIKEY')


def get_elevenlabs_api_key() -> str:
    if ELEVENLABS_APIKEY is None or ELEVENLABS_APIKEY == '':
        raise Exception("Elevenlabs api key missing." +
                        " Use envar ELEVENLABS_APIKEY")
    return ELEVENLABS_APIKEY


def get_chatgpt_api_key() -> str:
    if CHATGPT_APIKEY is None or CHATGPT_APIKEY == '':
        raise Exception("Chatgpt api key missing." +
                        " Use envar CHATGPT_APIKEY")
    return CHATGPT_APIKEY
