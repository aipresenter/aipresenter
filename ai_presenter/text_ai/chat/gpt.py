import openai
import logging
from ai_presenter.config.env_vars import get_chatgpt_api_key
from ai_presenter.text_ai.chat.base import BaseChatGPT


class ChatGPT(BaseChatGPT):
    def __init__(self):
        super().__init__()
        openai.api_key = get_chatgpt_api_key()

    def create(self, model='', messages=None):
        full_resp = ""

        count = 5
        while count > 0:
            count -= 1
            completion = openai.ChatCompletion.create(
                model=model,
                messages=messages,
            )

            resp = completion.choices[0].message.content
            finish_reason = completion.choices[0].finish_reason
            full_resp += resp

            logging.debug(">> Recieved: " + resp)
            logging.debug(">> Have: " + full_resp)
            logging.debug(">> finish_reason: " +
                          completion.choices[0].finish_reason)
            if finish_reason == 'stop':
                logging.debug('chatgpt: got all info')
                return full_resp

            elif finish_reason == 'length':
                logging.debug('chatgpt: need more info, retrying, usage:' +
                              f'{completion.choices[0].usage} count:{count}')
                messages += [
                    {"role": "assistant", "content": resp},
                ]
            else:
                raise Exception("finish reason is " + finish_reason)
        raise Exception('Tried too many times to talk to ChatGPT')
