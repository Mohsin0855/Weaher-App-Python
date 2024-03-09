# Weather App

This is a simple weather app that retrieves and speaks the current weather information for a given city using the WeatherAPI.

**How to Use**
- Make sure you have Python installed on your system.
- Install the required libraries by running:
``` bash 
pip install requests pyttsx3
```
- Run the ```bash weather_app.py ``` script.
- Enter the name of the city when prompted.
- The app will fetch the current weather information and speak it out loud.

**Dependencies**

- requests
- pyttsx3
 
**Usage**

The app prompts the user to enter a city name. It then fetches the current weather information from the WeatherAPI and speaks out the following details:

- City
- Country
- Latitude
-Longitude
- Local Time
- Weather Condition
- Wind Speed (kph)
- Wind Degree
  
**API Key**
  
Make sure to replace the API key in the URL with your own WeatherAPI key to use the service.
