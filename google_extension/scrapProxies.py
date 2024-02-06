import requests
from bs4 import BeautifulSoup

url = 'https://free-proxy-list.net'
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Use BeautifulSoup methods to find and extract specific elements
    textareas = soup.find_all('textarea', class_='form-control')  # Find all <h2> elements with class 'headline'
    proxylist = str(textareas[0])
    lines = proxylist.split("\n")
    proxies = lines[3:-1]
else:
    print('Failed to fetch the webpage')
