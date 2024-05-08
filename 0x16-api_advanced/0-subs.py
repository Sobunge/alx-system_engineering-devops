import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/sobunge)"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        
        # Access rate limit headers
        ratelimit_used = int(response.headers.get('X-Ratelimit-Used', 0))
        ratelimit_remaining = int(response.headers.get('X-Ratelimit-Remaining', 0))
        ratelimit_reset = int(response.headers.get('X-Ratelimit-Reset', 0))
        
        print(f"Rate limit used: {ratelimit_used}")
        print(f"Rate limit remaining: {ratelimit_remaining}")
        print(f"Rate limit reset (seconds): {ratelimit_reset}")
        
        data = response.json().get("data")
        return data.get("subscribers")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return 0

print(number_of_subscribers("programming"))
