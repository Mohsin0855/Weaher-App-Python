import requests
import json
import pyttsx3

city = input("Enter the name of City:\n")
url = f"http://api.weatherapi.com/v1/current.json?key=5b6afb5d43b84e70a6d185105240803&q={city}"
r = requests.get(url)

weather_data = json.loads(r.text)
city_name = weather_data["location"]["name"]
country = weather_data["location"]["country"]
latitude = weather_data["location"]["lat"]
longitude = weather_data["location"]["lon"]
local_time = weather_data["location"]["localtime"]
condition = weather_data["current"]["condition"]["text"]
wind_kph = weather_data["current"]["wind_kph"]
wind_degree = weather_data["current"]["wind_degree"]

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Speak the information
print(f"City: {city_name}")
engine.say(f"City: {city_name}")

print(f"Country: {country}")
engine.say(f"Country: {country}")

print(f"Latitude: {latitude}")
engine.say(f"Latitude: {latitude}")

print(f"Longitude: {longitude}")
engine.say(f"Longitude: {longitude}")

print(f"Local Time: {local_time}")
engine.say(f"Local Time: {local_time}")

print(f"Weather Condition: {condition}")
engine.say(f"Weather Condition: {condition}")

print(f"Wind Speed (kph): {wind_kph}")
engine.say(f"Wind Speed (kph): {wind_kph}")

print(f"Wind Degree: {wind_degree}")
engine.say(f"Wind Degree: {wind_degree}")

# Run and wait for the speech to finish
engine.runAndWait()








