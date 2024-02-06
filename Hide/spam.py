import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

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
driver.get('http://localhost/phishermansite/BankLoginPage.php')


def move_mouse(num):
    for i in range(num):
        pyautogui.moveTo(300, 300)
        pyautogui.moveTo(200, 200)


for i in range(10): #change value for number of times to spam
    randomPassword = random.choice(passwordlist)
    randomBankUID = rng(14) # rng() is a function that generates a random number with x number of digits.
    # Interact with form elements
    move_mouse(2)
    driver.find_element(By.NAME, 'BankUID').send_keys(randomBankUID)
    move_mouse(2)
    driver.find_element(By.NAME, 'Password').send_keys(randomPassword)
    move_mouse(2)
    # Click a button
    driver.find_element(By.NAME, 'submit').click()

    # Perform other interactions as needed

# Close the browser window
driver.quit()