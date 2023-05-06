
import os
import json
import texts
from botocore.vendored import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BASE_URL = "https://api.telegram.org/bot{}".format(BOT_TOKEN)

def handler(event, context):
    try:
        income = json.loads(event["body"])
        chat_id = income["message"]["chat"]["id"]
        print(chat_id)
        data = {"text": texts.welcome_message, "chat_id": chat_id}
        url = BASE_URL + '/sendMessage'
        print(BASE_URL)
        requests.post(url, data)
    except Exception as e:
        print(e)
    return {"statusCode": 200}

