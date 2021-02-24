import pyttsx3
import requests

# get grid from: https://api.weather.gov/points/36.7627,-119.7988
weather_request = requests.get('https://api.weather.gov/gridpoints/HNX/51,101/forecast')

# kludgy but works!!
weather_request_periods = weather_request.json()['properties']['periods']
engine = pyttsx3.init()
engine.runAndWait()

engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)

engine.say('The weather is currently: ')
engine.say(weather_request_periods[0]['detailedForecast'].replace('mph', 'miles per hour'))

engine.say('The weather tomorrow is: ')
engine.say(weather_request_periods[1]['detailedForecast'].replace('mph', 'miles per hour'))

engine.runAndWait()
