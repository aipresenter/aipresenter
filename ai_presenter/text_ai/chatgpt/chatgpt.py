import openai
import os
import logging


class ChatGPT:
    def __init__(self) -> None:
        openai.api_key = os.getenv("CHATGPT_APIKEY")

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
