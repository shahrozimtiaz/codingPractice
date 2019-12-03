import requests
import time
from datetime import datetime

url = 'https://project-102-cadslist.herokuapp.com/lobby/'
count = 1
while True:
    response = requests.get(url)
    print('{} pinged: response {} {}'.format(count,response.status_code,datetime.now().strftime("%I:%M %p")))
    count+=1
    time.sleep(10*60)
