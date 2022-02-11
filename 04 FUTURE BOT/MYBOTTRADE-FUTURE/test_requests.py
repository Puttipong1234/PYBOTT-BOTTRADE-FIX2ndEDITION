import requests
import json

url = 'http://127.0.0.1:5000/signals'
heroku_url = "https://xxxxxxxxxxxx.herokuapp.com/signals" # webhook
ข้อมูลตัวอย่าง = {
            'ACTION': 'OPEN SHORT',
            'AMOUNT_COIN' : '100.00',
            'LEV' : '30',
            'SYMBOL' : 'DOGEUSDT',
            'PASSWORD': "xxxxxx"
            }

ข้อมูลตัวอย่าง = json.dumps(ข้อมูลตัวอย่าง)

# x = requests.post(url, data = ข้อมูลตัวอย่าง)
x = requests.post(heroku_url, data = ข้อมูลตัวอย่าง)

print(x.text)