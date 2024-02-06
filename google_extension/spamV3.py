# update rotating_proxies_list.txt first before running
# https://free-proxy-list.net

import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import sys
# Other imports...

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        print(sys.argv)
        selected_options = sys.argv[2:]
        


# import credentials from fakeCred.py
from fakeCred import fname
from fakeCred import lname
from fakeCred import usernameslist
from fakeCred import passwordlist
from fakeCred import emails
from fakeCred import hpnumberlist
from fakeCred import rng

# proxy list
from scrapProxies import proxies

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

for i in range(50): #change value for number of times to spam
    try:
        res = requests.get(url, proxies={"http": proxies[i],
                                            "https": proxies[i]})
        print(f'ip address {proxies[i]}, code = {res.status_code}')   
        for i in range(3):
            randomFirstName = random.choice(fname)
            randomLastName = random.choice(lname)
            randomUsername = random.choice(usernameslist)
            randomPassword = random.choice(passwordlist)
            randomEmail = random.choice(emails)
            randomPN = random.choice(hpnumberlist)
            for field in selected_options:
                move_mouse(2)
                if(field == "fname"):
                    move_mouse(2)
                    element_names = ['FirstName', 'FName', 'fName']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(randomPassword)
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                if(field == "lname"):
                    move_mouse(2)
                    element_names = ['LastName', 'LName', 'lName']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(randomLastName)
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                if(field == "username"):
                    move_mouse(2)
                    element_names = ['Username', 'username']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(randomUsername)
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                if(field == "password"):
                    move_mouse(2)
                    element_names = ['MasterPassword', 'masterPassword', 'Password', 'password']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(randomPassword)
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                if(field == "email"):
                    move_mouse(2)
                    element_names = ['email', 'Email']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(randomEmail)
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                if(field == "secretKey"):
                    move_mouse(2)
                    element_names = ['KeyWord', 'SecretWord', 'SecretKey', 'Secret', 'PersonalKey']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(rng(5))
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                if(field == "hpnumber"):
                    move_mouse(2)
                    element_names = ['HPNumber', 'HpNumber', 'PNumber']
                    for name in element_names:
                        try:
                            driver.find_element(By.NAME, name).send_keys(hpnumberlist)
                            break  # Exit the loop if an element is found and data sent
                        except NoSuchElementException:
                            pass
                move_mouse(2)
                
                
            # Click a button
            driver.find_element(By.CLASS_NAME, 'g-recaptcha').click()
            driver.find_element(By.CLASS_NAME, 'submit').click()
            driver.find_element(By.CLASS_NAME, 'login').click()

            # Perform other interactions as needed
    except:
        print("proxy failed")
    

# Close the browser window
driver.quit()
