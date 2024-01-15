import requests
import random

# Defines the URl of the web form
url = 'http://localhost/phishermansite/BankDB.php'

commonpasswordsrawurl = 'https://raw.githubusercontent.com/danielmiessler/SecLists/aad07fff50ca37af2926de4d07ff670bf3416fbc/Passwords/10_million_password_list_top_1000.txt'


# following code is to extract data from the raw library of contents

def ExtractData(RawURL):
    try:
        response = requests.get(RawURL)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Content of the file is in response.text
            file_content = response.text
            DataList = file_content.split("\n")
            return DataList

            # Now you can work with the file_content variable
        else:
            print(f'Failed to fetch data. HTTP Error: {response.status_code}')
    except Exception as e:
        print(f'An error occurred: {e}')

passwordlist =  ExtractData(commonpasswordsrawurl)


for i in range(100): #change value for number of times to spam
    randomPassword = random.choice(passwordlist)
    first_digit = random.randint(1, 9)
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    randomBankUID = str(first_digit) + remaining_digits
    
    # Main function that sends the POST request. Edit data={} after using Burp Suite
    response = requests.post(url, data={"BankUID": randomBankUID, "Password": randomPassword})



if response.status_code == 200:
    print('Success!')
else:
    print(f'HTTP Error: {response.status_code}')
