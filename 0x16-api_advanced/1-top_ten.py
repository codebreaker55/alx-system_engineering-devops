#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles,
of the first 10 hot posts listed for a given subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts,
    If not a valid subreddit, print None
    """
    user = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'

    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data.get('data', {}).get('children', []):
                print(post.get('data', {}).get('title', ''))
    except Exception as e:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Please provide a subreddit as a command-line argument.")
