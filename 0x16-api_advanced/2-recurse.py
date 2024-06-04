#!/usr/bin/python3
"""
a recursive function that queries the Reddit API,
returns a list containing the titles of all hot articles for a given subreddit
"""
import requests
import sys


def title_add(hot_list, hot_posts):
    """ adds an item into the list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    title_add(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """return titles of all of the hot articles, if no results return none"""
    usr_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': usr_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url,
                        headers=headers,
                        params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        return None

    dic = resp.json()
    hot_posts = dic['data']['children']
    title_add(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
