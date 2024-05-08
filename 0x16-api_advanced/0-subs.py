import requests

def number_of_subscribers(subreddit):
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Template/1.0 by /u/sobunge"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        print("Error:", req.status_code)
        return 0

subscribers = number_of_subscribers("programming")
print("Number of subscribers:", subscribers)
