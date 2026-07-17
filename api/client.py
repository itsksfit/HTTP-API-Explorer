import time
import requests

def get_request(url):
    try:
        start = time.time()

        response = requests.get(url)

        end = time.time()
        response_time = end - start

        return response, response_time

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None