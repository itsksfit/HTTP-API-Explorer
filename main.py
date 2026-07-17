from api.client import get_request


def main():
    print("=" * 40)
    print("HTTP API Explorer")
    print("=" * 40)

    url = input("Enter API URL: ")

    print("\nSending Request...\n")

    response, response_time = get_request(url)

    if response is None:
        return

    print(f"Response Time : {response_time:.2f} seconds")
    print(f"Status Code : {response.status_code}")

    print("\nResponse:\n")

    data = response.json()

    print(f"Current User URL : {data.get('current_user_url', 'N/A')}")
    print(f"Repository Search : {data.get('repository_search_url', 'N/A')}")
    print(f"Repository URL : {data.get('repository_url', 'N/A')}")

    print("\nHeaders:\n")

    for key, value in response.headers.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()