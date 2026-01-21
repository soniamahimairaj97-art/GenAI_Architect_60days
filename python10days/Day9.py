#Module ->Install ->Import

import requests
import  time
time.sleep(5)

response = requests.get("https://httpbin.org/get")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
################################
import emoji

print(emoji.emojize("Python is :thumbs_up:"))


