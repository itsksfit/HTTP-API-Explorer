import requests
def get_request(url):
    response = requests.get(url)         #Send an HTTP GET request to this URL.
    return response