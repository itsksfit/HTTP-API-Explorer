import json

from api.client import send_request


def main():
    print("=" * 40)
    print("HTTP API Explorer")
    print("=" * 40)

    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")

    choice = input("\nSelect Method: ")

    methods = {
        "1": "GET",
        "2": "POST",
        "3": "PUT",
        "4": "DELETE"
    }

    method = methods.get(choice)

    if method is None:
        print("Invalid Choice")
        return

    url = input("\nEnter API URL: ")

    print("\nSending Request...\n")

    response, response_time = send_request(method, url)

    if response is None:
        return

    print(f"Method        : {method}")
    print(f"Response Time : {response_time:.2f} seconds")
    print(f"Status Code   : {response.status_code}")

    print("\nJSON Response\n")

    try:
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print("Response is not JSON.")

    print("\nHeaders\n")

    for key, value in response.headers.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()