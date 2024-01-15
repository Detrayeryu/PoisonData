import requests
from bs4 import BeautifulSoup

#from spamV2 import url

url = "http://security-page-community-standards.blogspot.sg/"

response = requests.get('https://www.whois.com/whois/')

if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the desired form by ID, replace 'form_id' with the actual form ID
    form = soup.find('form', {'action': '\search.php'})  # Change 'form_id' to the actual ID
    
    if form:
        # Get the form action URL, method, and other necessary details
        action = form.get('action')
        method = form.get('method')

        response = requests.post("https://www.whois.com/whois/", data={"query": url,})

        if response.status_code == 200:
            print("success")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            info = soup.find_all('main')
            
            for pre_tag in info:
                print(pre_tag.get_text())
        else:
            print("unsuccessful", response.status_code)