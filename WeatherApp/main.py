import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=953ecd78ec9d4d29843143331232806&q={city}"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]['temp_c']
x = f"The current weather in {city} is {w} degrees"
engine = pyttsx3.init()
engine.say(x)
engine.runAndWait()
