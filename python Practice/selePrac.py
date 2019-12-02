from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

link = 'https://www.google.com/'

driver.get(link)

elem = driver.find_element_by_name('q')

# elem.send_keys('lebron james')
elem.send_keys('lebron james' + Keys.RETURN)

# elem = driver.find_element_by_name('btnK')
# elem.click()



soup = BeautifulSoup(driver.page_source, "html")
print('lebron' in soup.prettify())


# input()