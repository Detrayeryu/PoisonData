# update rotating_proxies_list.txt first before running
# https://free-proxy-list.net

import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import random

# Defines the URl of the web form
url = 'http://localhost/phishermansite/VaultLoginPage.php'

# import credentials from fakeCred.py

from fakeCred import fname
from fakeCred import lname
from fakeCred import usernameslist
from fakeCred import passwordlist
from fakeCred import emails
from fakeCred import hpnumberlist
from fakeCred import rng

# -----------------------------------AVAILABLE DATA LIBRARIES--------------------------------------- #
#                                                                                                    #
#                                           FIRST NAMES                                              #
#                                            LAST NAMES                                              #
#                                            USERNAMES                                               #
#                                            PASSWORDS                                               #
#                                             EMAILS                                                 #
#                                                                                                    #
# -------------------------------------------------------------------------------------------------- #

# Initialize the web driver
driver = webdriver.Chrome()  # Use the appropriate driver here

# Open a webpage
driver.get(url)

def move_mouse(num):
    for i in range(num):
        pyautogui.moveTo(300, 300)
        pyautogui.moveTo(200, 200)

for i in range(5): #change value for number of times to spam
    randomPassword = random.choice(passwordlist)
    randomUsername = random.choice(usernameslist)
    randomEmail = random.choice(emails)
    
    # Interact with form elements
    move_mouse(2)
    driver.find_element(By.NAME, 'Username').send_keys(randomUsername)
    move_mouse(2)
    driver.find_element(By.NAME, 'MasterPassword').send_keys(randomPassword)
    move_mouse(2)
    driver.find_element(By.NAME, 'Email').send_keys(randomEmail)
    move_mouse(2)
    driver.find_element(By.NAME, 'KeyWord').send_keys(rng(5))
    move_mouse(2)
    # Click a button
    driver.find_element(By.CLASS_NAME, 'g-recaptcha').click()

    # Perform other interactions as needed

# Close the browser window
driver.quit()
    