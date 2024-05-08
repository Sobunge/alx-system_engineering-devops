#!/usr/bin/python3

import requests

def get_oauth_token(client_id, client_secret, username, password):
    url = "https://www.reddit.com/api/v1/access_token"
    auth = (client_id, client_secret)
    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }
    response = requests.post(url, auth=auth, data=data)
    response_data = response.json()
    if "access_token" in response_data:
        return response_data["access_token"]
    else:
        print("Failed to obtain OAuth token:", response_data.get("error"))
        return None

# Replace these with your app's client ID, client secret, Reddit username, and password
client_id = "<your_client_id>"
client_secret = "<your_client_secret>"
reddit_username = "<your_reddit_username>"
reddit_password = "<your_reddit_password>"

oauth_token = get_oauth_token(client_id, client_secret, reddit_username, reddit_password)
if oauth_token:
    print("OAuth token:", oauth_token)
