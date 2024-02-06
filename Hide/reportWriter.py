from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import sys
from fpdf import FPDF
import socket
import requests
from urllib.parse import urlparse

url = "http://google.com"
sucessfullEntry = 4
attempt = 10

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