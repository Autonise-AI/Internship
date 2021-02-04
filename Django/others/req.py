import requests
import json

data = {
    "name" : "xyz",
    "num" : 123
}

url = "https://webhook.site/95f083ec-9fe8-4b6c-a01d-0472b2fef0d6"

r = requests.post(url=url, json=data)

print(r.text)