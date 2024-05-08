#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests
import time

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 403:
            print("Error: Access to the subreddit is forbidden. Please check if the subreddit exists.")
            return 0
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return 0
    except (KeyError, json.JSONDecodeError) as e:
        print("Error decoding JSON or extracting subscribers:", e)
        print("Response text:", response.text)
        return 0

if __name__ == '__main__':
    subreddit = "programming"
    print(number_of_subscribers(subreddit))

