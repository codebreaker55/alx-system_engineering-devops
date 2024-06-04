#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers, If not a valid subreddit, return 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # getting user agent
    # using Mozilla/5.0 to identify the browser or client making the request
    header = {"User-Agent": "Mozilla/5.0"}
    # get request to the API endpoint using requests.get()
    resp = requests.get(url, headers=header, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
