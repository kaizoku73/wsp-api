import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("ACCESS_TOKEN")
version = os.getenv("VERSION")
user = os.getenv("USER_NUMBER")
number_id = os.getenv("PHONE_NUMBER_ID")


#To check the template message
def send_template():
    url = f"https://graph.facebook.com/{version}/{number_id}/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": user,
        "type": "template",
        "template": { "name": "hello_world", "language": { "code": "en_US" } }
    }

    response = requests.post(url=url, headers=headers, json=data)
    return response

response = send_template()
print(response.status_code)
print(response.json())

#To check the text message
def send_message():
    url = f"https://graph.facebook.com/{version}/{number_id}/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": user,
        "type": "text",
        "text": {
            "preview_url": "true",
            "body": "As requested, here'\''s the link to our latest product: https://www.meta.com/quest/quest-3/"
        }
        }
    
    response = requests.post(url=url, headers=headers, json=data)
    return response

txt_res = send_message()
print(txt_res.status_code)
print(txt_res.json())