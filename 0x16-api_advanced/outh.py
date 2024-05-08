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
client_id = "sobunge"
client_secret = "-C8XZI10GZBHEPx84reO75ZT3nVgTA"
reddit_username = "sobunge"
reddit_password = "merium@kema"

oauth_token = get_oauth_token(client_id, client_secret, reddit_username, reddit_password)
if oauth_token:
    print("OAuth token:", oauth_token)
