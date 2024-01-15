import requests
import random

# add libraries as RAW urls here
commonpasswordsrawurl = 'https://raw.githubusercontent.com/danielmiessler/SecLists/aad07fff50ca37af2926de4d07ff670bf3416fbc/Passwords/10_million_password_list_top_1000.txt'
firstnamerawurl = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"
lastnamerawurl = "https://raw.githubusercontent.com/zeraye/names-surnames-list/master/surnames-list.txt"
domain = ['gmail', 'googlemail', 'yahoo', 'hotmail', 'outlook']
usernamesrawurl = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/xato-net-10-million-usernames.txt"



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

# fake email generator
fname =  ExtractData(firstnamerawurl)
fname = [word[:-2] for word in fname]
lname =  ExtractData(lastnamerawurl)
lname = [word.lower() for word in lname]


emails = []
for first in fname:
    for last in lname:
        for dom in domain:
            newemail = f"{first}.{last}@{dom}.com"
            emails.append(newemail)


# Phone number generator
hpnumberlist = []

for i in range(100):
    number = str(random.choice([8,9]))
    for i in range(7):
        number = number + str(random.randint(0,9))
    hpnumberlist.append(number)
    
# simple random number generator. length = length of number to generate
def rng(length):
    rng = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return rng


# Create varibles and run RAW urls through ExtractData()
passwordlist =  ExtractData(commonpasswordsrawurl)
usernameslist = ExtractData(usernamesrawurl)