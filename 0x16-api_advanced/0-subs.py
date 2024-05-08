#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        subscribers = data["data"]["subscribers"]
        print("Subscribers:", subscribers)  # Add this line for debugging
        return subscribers
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return 0
    except (KeyError, json.JSONDecodeError) as e:
        print("Error decoding JSON or extracting subscribers:", e)
        print("Response text:", response.text)  # Add this line for debugging
        return 0

