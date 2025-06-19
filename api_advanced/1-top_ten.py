#!/usr/bin/python3
"""1-top_ten.py"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
            return

        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")
