#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers from a given subreddit
    Args:
        subreddit"""

    apiUrl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(apiUrl, headers=header, allow_redirects=False)

    if response.status_code >= 300:
        return 0
    """.get('data').get('subscribers') handles cases where the data or subscribers keys might be missing."""
    return response.json().get('data').get('subscribers')
