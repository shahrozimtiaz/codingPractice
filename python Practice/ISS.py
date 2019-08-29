import requests
import time
import folium
import subprocess

issJson = requests.get('http://api.open-notify.org/iss-now.json').json()
peopleJson = requests.get('http://api.open-notify.org/astros.json').json()
location = issJson['iss_position']
lstPeopleDetails = peopleJson['people']
lstPeople = ""
for person in lstPeopleDetails:
    lstPeople += ', ' + person['name']
lstPeople = lstPeople[2:]
lat = location['latitude']
long = location['longitude']
m = folium.Map(location=[lat,long],zoom_start=5)
marker = folium.Marker([lat, long], tooltip='ISS Location: lat: ' + lat + ' long: ' + long, popup="Number of humans in space right now " + str(peopleJson['number']) + ': ' + lstPeople).add_to(m)
m.save('map.html')
subprocess.call(['open','/Users/shahrozimtiaz/Documents/codingPractice/python Practice/map.html'])


# while(True):
#     print('Calculating..')
#     del marker
#     issJson = requests.get('http://api.open-notify.org/iss-now.json').json()
#     peopleJson = requests.get('http://api.open-notify.org/astros.json').json()
#     # dict_keys(['iss_position', 'message', 'timestamp'])
#     # dict_keys(['people', 'number', 'message'])
#
#     location = issJson['iss_position']
#     lstPeopleDetails = peopleJson['people']
#     lstPeople = ""
#     for person in lstPeopleDetails:
#         lstPeople += ', ' + person['name']
#     lstPeople = lstPeople[2:]
#     lat = location['latitude']
#     long = location['longitude']
#     m.location=[lat,long]
#     marker = folium.Marker([lat,long],tooltip='ISS Location: lat: ' + lat + ' long: ' + long, popup="Number of humans in space right now " + str(peopleJson['number']) + ': ' + lstPeople).add_to(m)
#     m.save('map.html')
#     time.sleep(25)