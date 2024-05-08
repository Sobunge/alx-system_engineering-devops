#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    oauth_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzE1MjQxODcyLjU0NjQ0OCwiaWF0IjoxNzE1MTU1NDcyLjU0NjQ0OCwianRpIjoicTR0ZFl6Vm1tN29LalhjS01XZlNtd0IwRTZOaVZnIiwiY2lkIjoiLU55RUhZMDdiVnpUb1JXbWpMeEN6dyIsImxpZCI6InQyX3k3Y2E2dmp1cCIsImFpZCI6InQyX3k3Y2E2dmp1cCIsImxjYSI6MTcxMjk4ODU2MTUwNywic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.a8JEjalxjIbTI9n7Sdg17uwKngHq3oe-qCu80_1KX-C9AwNduhsNA5jJUyX5dt7UpXTjQaAdNpVLpd--CErlfszhDERHxXiQR3RoFGczloK8oX5zFxK1t2uhLv8wMAxIvpBsoWX5pf4ji_EtkFNr_CjTqAPGoqutdETCeOAdTn16FWpYa-yD_aNFAYOZsIm0Zm3TurV11V2gaeeiuk8u6PUP5CnEPJ-JBUo-8fWNmbIhfsoGMuDVBkXik286jIzg8GLL36EeMM6BuPn7d2leYrqXNgNAkb_8F8ooefrasPPiYmOTK2F081V961OBHEvXkPdg6bExZfoRldmXyGdrXw"
    headers = {
        "Authorization": f"bearer {oauth_token}",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results

print(number_of_subscribers("programming"))
