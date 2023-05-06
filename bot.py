
import os
import json
import texts
import urllib3

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BASE_URL = "https://api.telegram.org/bot{}".format(BOT_TOKEN)

def handler(event, context):
    try:
        http = urllib3.PoolManager()
        income = json.loads(event["body"])
        chat_id = income["message"]["chat"]["id"]
        data = {"text": texts.welcome_message, "chat_id": chat_id}
        body = json.dumps(data)
        url = BASE_URL + "/sendMessage"
        print(url)
        http.request("POST", url, body)
    except Exception as e:
        print(str(e))
    return {"statusCode": 200}

