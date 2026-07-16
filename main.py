from api.client import get_request
def main():
    print("=" * 40)
    print("HTTP API Explorer")
    print("=" * 40)

    url = input("Enter API URL: ")

    print("\nSending Request...\n")

    response = get_request(url)

    print(f"Status Code : {response.status_code}")


if __name__ == "__main__":
    main()