from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usernameStr = '0481862258'
passwordStr = 'theHoff34'

browser = webdriver.Chrome()
browser.get(('http://www.amaysim.com.au'))
browser.maximize_window()
acctButton = browser.find_element(By.XPATH, "//a[span='Account']")
acctButton.click()
time.sleep(20)

# fill in username and password and hit the login button
username = browser.find_element(By.XPATH, "//div/input[@name='username']")
username.send_keys(usernameStr)
password = browser.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(passwordStr)
loginButton = browser.find_element(By.XPATH, "//button[@type='submit']")
loginButton.click()

#Managed Settings
settingsButton = browser.find_element(By.XPATH, "a[span='Settings']")
settingsButton.click()

#Validate Call Forwarding
browser.close()
