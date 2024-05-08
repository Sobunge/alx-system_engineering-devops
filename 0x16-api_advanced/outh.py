import requests
import time

def get_oauth_token(client_id, client_secret, username, password):
    url = "https://www.reddit.com/api/v1/access_token"
    auth = (client_id, client_secret)
    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }

    max_retries = 3
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        response = requests.post(url, auth=auth, data=data)
        if response.status_code == 200:
            response_data = response.json()
            if "access_token" in response_data:
                return response_data["access_token"]
            else:
                print("Failed to obtain OAuth token:", response_data.get("error"))
                return None
        elif response.status_code == 429:
            print("Rate limit exceeded. Retrying in {} seconds...".format(retry_delay))
            time.sleep(retry_delay)
        else:
            print("Failed to obtain OAuth token. Status code:", response.status_code)
            return None

    print("Max retries exceeded. Failed to obtain OAuth token.")
    return None

# Replace these with your app's client ID, client secret, Reddit username, and password
client_id = "-NyEHY07bVzToRWmjLxCzw"
client_secret = "-C8XZI10GZBHEPx84reO75ZT3nVgTA"
reddit_username = "sobunge"
reddit_password = ""

oauth_token = get_oauth_token(client_id, client_secret, reddit_username, reddit_password)
if oauth_token:
    print("OAuth token:", oauth_token)
