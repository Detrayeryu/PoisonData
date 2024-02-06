import socket
import requests
from urllib.parse import urlparse

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data_list = [line.strip() for line in file]
    return data_list

def is_ip_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
        return True
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, address)
            return True
        except socket.error:
            return False

def check_urls(url):
    try:
        response = requests.get(url)
        print(f"URL: {url}, \033[92mWebsite Up {response.status_code}\033[0m")
    except requests.RequestException as e:
        print(f"URL: {url}, \033[91mWebsite Down\033[0m")

def check_ip(ip_address):
    try:
        # Perform a reverse DNS lookup to get the domain name associated with the IP
        domain_name, _, _ = socket.gethostbyaddr(ip_address)
        
        # Check the status of the IP address
        response = requests.get(f"http://{ip_address}")
        
        if response.status_code == 200:
            print(f"IP: {ip_address}, Domain: {domain_name}, \033[92mWebsite Up\033[0m")
        else:
            print(f"IP: {ip_address}, \033[91mWebsite Down\033[0m")
    
    except (socket.herror, requests.RequestException) as e:
        print(f"IP: {ip_address}, \033[93mInvalid IP or Website Down\033[0m")
        print(f"\033[94mPlease check https://www.whatismyip.com/ip-address-lookup/ to verify\033[0m")
        
        
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
    
    file_path = "data.txt"
    url_list = read_data_from_file("./domain_list.txt")

    for url in url_list:
        if is_ip_address(url):
            status = check_ip(url)
            geolocation_result = get_geolocation(url)
            if geolocation_result != "None":
                print(f"Geolocation information for {url}:")
                print(f"IP Address: {geolocation_result['ip']}")
                print(f"Organisation: {geolocation_result['org']}")
                print(f"Location: {geolocation_result['city']}, {geolocation_result['region']}, {geolocation_result['country']}")
                print(f"Latitude/Longitude: {geolocation_result['loc']}\n")
            else:
                print(f"No information found on this ip address")
        else:
            status = check_urls(url)
            url = urlparse(url).netloc
            geolocation_result = get_domain_geolocation(url)
            
            if geolocation_result != "None":
                print(f"Geolocation information for {url}:")
                print(f"IP Address: {geolocation_result['ip']}")
                print(f"Organisation: {geolocation_result['org']}")
                print(f"Location: {geolocation_result['city']}, {geolocation_result['region']}, {geolocation_result['country']}")
                print(f"Latitude/Longitude: {geolocation_result['loc']}\n")
            else:
                print(f"No information found on this domain")
        



