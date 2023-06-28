# To be moved to tools(or some other directory later) directory

import requests

url = "https://api.elevenlabs.io/v1/voices/<voice-id>"

headers = {
  "Accept": "application/json",
  "xi-api-key": "<xi-api-key>"
}

response = requests.delete(url, headers=headers)

print(response.text)