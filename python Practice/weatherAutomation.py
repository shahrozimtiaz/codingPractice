import requests
from datetime import datetime
from emailSender import emailSender

url = "http://api.openweathermap.org/data/2.5/weather?"
apiKey = '2fb48d44dbe0883d7540cfc4023a472d'
city = 'Leesburg,US'

querystring = {'appid': apiKey, 'units': 'imperial', "q": city}
print("Running..")
response = requests.get( url, params=querystring).json()

info = ['name','weather','main','wind',]

city_name = response['name']
weather = str(response['main']['temp']) + "F " + response['weather'][0]['description']
wind = response['wind']['speed']

message = 'City: ' + city_name + '\nWeather: ' + str(weather) + '\nWind: ' + str(wind) + ' MPH' + '\nTime: ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S')
sender = emailSender('shahrozimtiaz07@gmail.com', 'Jokerface07!')
print('Sending email')
sender.sendMessage('shahrozimtiaz07@gmail.com','Weather ' + datetime.now().strftime("%m/%d/%Y"), message)
print('Sent')
sender.close()
print('Done!')
