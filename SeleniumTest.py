from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary)
user_name = "Terit"
password = "nofear"
#driver = webdriver.Firefox()
driver.get("https://www.redguides.com/community/login")
element = driver.find_element_by_name("login")
element.send_keys(user_name)
element = driver.find_element_by_name("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(3)
driver.get('https://www.redguides.com/community/resources/bard-mellee-mez-puller-supported.977/')
html = driver.find_element_by_class_name("  ")
print(html.text)
#print(html)
#soup = BeautifulSoup(html.data, features='html.parser')

driver.quit()