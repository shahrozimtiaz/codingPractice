from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://twitter.com/login')


def login_twitter(username, password):
    # open the web page in the browser:
    driver.get("https://twitter.com/login")

    # find the boxes for username and password
    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")
    # enter your username:
    username_field.send_keys(username)
    driver.implicitly_wait(1)

    # enter your password:
    password_field.click()
    password_field.send_keys(password)
    driver.implicitly_wait(1)

    # click the "Log In" button:
    driver.find_element_by_class_name("EdgeButtom--medium").click()

def send_message(user,message):
    driver.get('https://twitter.com/messages/' + user)
    writer = driver.find_element_by_class_name('public-DraftEditor-content')
    driver.implicitly_wait(3)
    writer.click()
    writer.clear()
    writer.send_keys(message + Keys.RETURN)
    writer.clear()

# 2302171194-892637840370266112 leah
# 892637840370266112-892637840370266112 me
# 851888924-892637840370266112 sammmy

login_twitter(user,password)

for i in range(1,4):
    send_message('851888924-892637840370266112','I just slid into your dms using python ' + str(i) + ' time(s)')
