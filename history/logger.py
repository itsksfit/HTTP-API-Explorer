from datetime import datetime
def save_request(method, url, status_code, response_time):
    with open("history/requests.log", "a") as file:
        file.write(f"Time   : {datetime.now()}\n")
        file.write(f"Method : {method}\n")
        file.write(f"URL    : {url}\n")
        file.write(f"Status : {status_code}\n")
        file.write(f"Response Time : {response_time:.2f} sec\n")
        file.write("-" * 40 + "\n")