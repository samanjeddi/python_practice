import requests
import pyttsx3

engine = pyttsx3.init()
url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

price = data["bitcoin"]["usd"]

engine.say(f"Bitcoin price: ${price}")
print(f"Bitcoin price: ${price}")
engine.runAndWait()