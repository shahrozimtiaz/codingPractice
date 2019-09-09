#sudo apt-get install python-pip iceweasel xvfb
#sudo pip install pyvirtualdisplay selenium

from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Firefox()