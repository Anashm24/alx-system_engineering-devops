#!/usr/bin/python
"""retrieve data from an API endpoint"""
import requests


def get_subreddit_names():
    url = "https://www.reddit.com/subreddits.json"
    headers = {"User-Agent": "MyRedditApp/1.0 by MyUsername"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subreddit_names = [sub["data"]["display_name"]
                           for sub in data["data"]["children"]]
        return sorted(subreddit_names)
    else:
        return []


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/1.0 by MyUsername"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
