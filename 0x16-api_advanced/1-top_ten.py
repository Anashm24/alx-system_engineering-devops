#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Bio/34'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        posts = response.json()['data']['children']
        for i in range(10):
            print(posts[i]['data']['article'])
