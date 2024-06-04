#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses
the title of all hot articles, and prints a sorted count of given keywords
"""


import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """ parses the title of all hot articles, and prints a sorted count
    args:
        subreddit (str): is the subreddit to search with
        word_list (list): is the list of words to search for in post titles
        after (str): the parameter for the next page of the API results
        word_count (obj): is key/value pairs of words/counts
    """

    if not word_count:
        for word in word_count:
            if word.lower() not in word_count:
                word_count[word.lower()] = 0

    if after is None:
        word_dict = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word in word_dict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    resp = requests.get(url, headers=header, params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        return None

    try:
        hot = resp.json()['data']['children']
        aft_h = resp.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_count.keys():
                word_count[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft_h, word_count)
