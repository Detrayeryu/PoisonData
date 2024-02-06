import requests
import random

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

firstnamerawurl = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"
lastnamerawurl = "https://raw.githubusercontent.com/zeraye/names-surnames-list/master/surnames-list.txt"
domain = ['gmail', 'googlemail', 'yahoo', 'hotmail', 'outlook']

fname =  ExtractData(firstnamerawurl)
fname = [word[:-2] for word in fname]
lname =  ExtractData(lastnamerawurl)
lname = [word.lower() for word in lname]


emails = []
for first in fname:
    for last in lname:
        for dom in domain:
            newemail = f"{first}.{last}@{dom}.com"
            with open('./emails.txt', 'a') as file:
                file.write(newemail + '\n')
