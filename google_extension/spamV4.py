# update rotating_proxies_list.txt first before running
# https://free-proxy-list.net

import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import sys
from fpdf import FPDF
import socket
from urllib.parse import urlparse
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

attempt = 1

# Track number of successful spams
sucessfullEntry = 0

for i in range(attempt): #change value for number of times to spam
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
            
            sucessfullEntry += 1

            # Perform other interactions as needed
    except:
        print("proxy failed")
    

# Close the browser window
driver.quit()


#--------------------------------------------------------------# 
#                   NS Lookup + UpOrDown                       #
#--------------------------------------------------------------# 


def check_urls(url):
    try:
        response = requests.get(url)
        print(f"URL: {url}, \033[92mWebsite Up {response.status_code}\033[0m")
    except requests.RequestException as e:
        print(f"URL: {url}, \033[91mWebsite Down\033[0m")
        
def get_geolocation(ip_address):
    # Resolve the IP address using ipinfo.io API
    ip_response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_data = ip_response.json()

    return ip_data

def get_domain_geolocation(url):
    try:
        # Use getaddrinfo for DNS resolution
        ip_address = socket.gethostbyname(url)

        # Get geolocation information for the resolved IP address
        geolocation_result = get_geolocation(ip_address)

        return geolocation_result

    except socket.gaierror as e:
        print(f"Error resolving DNS for {url}: {e}")
        return "None"  # or raise an exception, depending on your needs

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "None"

if __name__ == "__main__":   
    status = check_urls(url)
    url = urlparse(url).netloc
    geolocation_result = get_domain_geolocation(url)
    
    if geolocation_result != "None":
        ipaddress = geolocation_result['ip']
        organisation = geolocation_result['org']
        location = geolocation_result['city'], geolocation_result['region'], geolocation_result['country']
        LongAndLat = geolocation_result['loc']
        extra = " "
    else:
        extra = "No information found on this domain"

#-------------------------------------------------------------# 
#                      Report writing                         #
#-------------------------------------------------------------# 

# Formatting PDF
pdf = FPDF()
pdf.compress = False
pdf.add_page()
pdf.set_font('Arial', 'BU', 16)
pdf.ln(10)

# PDF Content
pdf.write(5, 'Report')
pdf.ln(10)
pdf.set_font('Arial', 'I', 8)
pdf.write(2, f'Target url: {url}')
pdf.ln(10)
pdf.write(2, f'Target ip address: {ipaddress}')
pdf.ln(10)
pdf.write(2, f'Target Organisation: {organisation}')
pdf.ln(10)
pdf.write(2, f'Target Location: {location}')
pdf.ln(10)
pdf.write(2, f'Target Geo Location: {LongAndLat}')
pdf.ln(10)
pdf.write(2, extra)
pdf.ln(10)
pdf.write(2, f"Website successfully spammed {sucessfullEntry} number of times")
pdf.ln(4)
pdf.write(2, f"{attempt - sucessfullEntry} failed attempts")


# Output PDF
pdf.output(f'Report.pdf', 'F')