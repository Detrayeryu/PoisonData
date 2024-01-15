# update rotating_proxies_list.txt first before running
# https://free-proxy-list.net

import requests
import random
import queue

q = queue.Queue()


with open("./rotating_proxies_list.txt", "r") as f:
    next(f)
    next(f)
    next(f)
    proxies = f.read().split("\n")

# Defines the URl of the web form
url = 'http://localhost/phishermansite/BankDB.php'

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




for i in range(100): #change value for number of times to spam
    randomPassword = random.choice(passwordlist)
    randomBankUID = rng(14) # rng() is a function that generates a random number with x number of digits.
    
    try:
        res = requests.get(url, proxies={"http": proxies[i],
                                            "https": proxies[i]})
        print(f'ip address {proxies[i]}, code = {res.status_code}')
    except:
        print("proxy failed")
    
    # Main function that sends the POST request. Edit data={} after using Burp Suite
    response = requests.post(url, data={"BankUID": randomBankUID, "Password": randomPassword, "ipaddr": proxies[i]})



if response.status_code == 200:
    print('Success!')
else:
    print(f'HTTP Error: {response.status_code}')
