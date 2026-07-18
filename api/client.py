import time

import requests


def send_request(method, url):
    try:
        start = time.perf_counter()

        response = requests.request(method, url)

        end = time.perf_counter()

        response_time = end - start

        return response, response_time

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None