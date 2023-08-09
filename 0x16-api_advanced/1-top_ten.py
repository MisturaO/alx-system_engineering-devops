#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and gets titles
    of the first 10 hot posts
    Args:
        subreddit
    """
    apiUrl = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    param = {
        "limit": 10
        }
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(apiUrl, params=param,
                            headers=header, allow_redirects=False)

    data = response.json().get('data')

    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get('data').get('title')) for child in
         data.get('children')]
