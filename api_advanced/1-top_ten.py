#!/usr/bin/python3
"""1-top_ten.py"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditClient/1.0'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
            else:
                print("None")
    except Exception:
        print("None")

