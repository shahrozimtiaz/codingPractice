import requests
import time

url = 'https://project-102-cadslist.herokuapp.com/lobby/'
count = 1
while True:
    response = requests.get(url)
    print('{} pinged: response {}'.format(count,response.status_code))
    count+=1
    time.sleep(10*60)
