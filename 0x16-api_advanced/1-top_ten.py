#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles,
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts,
    If not a valid subreddit, print None
    """
    header = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    resp = requests.get(url, headers=header, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
