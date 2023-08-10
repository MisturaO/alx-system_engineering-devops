#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    A recursive functions that returns a list containing
    the titles of all hot articles for a given subreddit
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of all hot articles.
        after (str): Token for pagination (optional).
        """
    apiUrl = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    param = {"count": count, "after": after, "limit": 100}
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    if hot_list is None:
        hot_list = []

    response = requests.get(apiUrl, params=param,
                            allow_redirects=False, headers=header)
    # print(response.json())

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
    else:
        return None

    return hot_list
