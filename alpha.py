       
       
import pyttsx3 # pip install pyttsx3
import requests
import json
friend = pyttsx3.init()

API_URL = 'https://dialogflow.cloud.google.com/v1/integrations/messenger/webhook/51924265-ed03-4e18-8a1c-0cf9fbf9e470/sessions/webdemo-e29d8426-bebd-2643-eef9-ac296b232bf0?platform=webdemo'


while True:
       word = input()
       parameter = {'queryInput': {'text': {'text': word, 'languageCode': "en"}}}
       d = requests.post(API_URL, json=parameter)
       r = json.loads(d.text[4:])['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
       friend.say(r)
       friend.runAndWait()
       

