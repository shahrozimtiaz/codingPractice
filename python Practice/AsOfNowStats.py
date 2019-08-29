from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

print('running..')
infoURL = 'https://www.worldometers.info'
options = Options()
options.headless = True
options.add_argument('--window-size=920,780')
driver = webdriver.Chrome(options=options)
driver.get(infoURL)
driver.maximize_window()
print('collecting..')
driver.save_screenshot('worldInfo.png')
driver.quit()
image = Image.open('worldInfo.png')
width, height = image.size   # Get dimensions
left = width/100
top = height/5
right = 2.3 * width/4
bottom = 3.55 * height/4
cropped_image = image.crop((left, top, right, bottom))
print('showing..')
cropped_image.show()
