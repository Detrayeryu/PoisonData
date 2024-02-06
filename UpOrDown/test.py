# update rotating_proxies_list.txt first before running
# https://free-proxy-list.net

import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import sys
import socket
from urllib.parse import urlparse

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data_list = [line.strip() for line in file]
    return data_list

url_list = read_data_from_file("./domain_list.txt")

# Initialize the web driver
driver = webdriver.Chrome()  # Use the appropriate driver here

# Open a webpage
driver.get("https://centralops.net/co/")

def move_mouse(num):
    for i in range(num):
        pyautogui.moveTo(300, 300)
        pyautogui.moveTo(200, 200)


for url in url_list:
    move_mouse(2)
    driver.find_element(By.NAME, "addr").send_keys(url)
    move_mouse(2)
        
        
    # Click a button
    driver.find_element(By.NAME, 'go').click()
    

# Close the browser window
#driver.quit()
