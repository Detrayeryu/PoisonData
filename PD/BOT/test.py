import requests
from bs4 import BeautifulSoup

url = 'http://localhost/phishermansite/VaultLoginPage.php'
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Use BeautifulSoup methods to find and extract specific elements
    textareas = soup.find_all('input')  # Find all <h2> elements with class 'headline'
    proxylist = str(textareas[0])
    
    print(proxylist)
else:
    print('Failed to fetch the webpage')