import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api-ce.kroger.com/v1/"

def get_token():
    client_id = os.environ["KROGER_CLIENT_ID"]
    client_secret = os.environ["KROGER_CLIENT_SECRET"]
    response = requests.post(
        f"{BASE_URL}connect/oauth2/token",
        auth=(client_id, client_secret),
        data={
            "grant_type": "client_credentials",
            "scope": "product.compact",
        },
        timeout=15,
    )
    response.raise_for_status()
    return response.json()["access_token"]

def main():
    get_token()
    print("Successfully obtained an access token.")


if __name__ == '__main__':
    main()