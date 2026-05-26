from praw import Reddit
from typing import Optional


def connect_reddit(client_id, client_secret, user_agent) -> Optional[Reddit]:
    try:
        reddit = Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        print("Connected to Reddit API successfully.")
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit API: {e}")


def extract_posts(instance : Reddit, subreddit: str, time_filter: str, limit:None):
    subreddit = instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_list = []

    print(posts)