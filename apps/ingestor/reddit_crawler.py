import os 
import re
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any
from dotenv import load_dotenv
load_dotenv()
import praw




features = ['title', 'selftext', 'url', 'created_utc', 'num_comments', 'score', 'upvote_ratio', 'author_fullname', 'subreddit', 'banned_at_utc',
             'ups', 'downs', 'num_reports', 'num_crossposts', 'likes']

# import pdb; pdb.set_trace()

class RedditHandler():
    def __init__(self,):
        self.reddit = praw.Reddit(
                client_id=os.environ.get("REDDIT_CLIENT_ID"),
                client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
                user_agent="Bot by u/Humble_Technician802",
            )

    def fetch_subreddit_data(self, subreddit:str, order_by:str, limit:int=1000) -> List[Dict[str, Any]]:
        """
        Fetches data from the subreddit based on the specified order.
        Args:
            order_by (str): The order to fetch data by. Can be 'new', 'hot', 'top', etc.
            limit (int): The maximum number of posts to fetch. Default is 1000.
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing the subreddit data.
        """
        
        # Validate the order_by parameter
        valid_orders = ['new', 'hot', 'top', 'rising']
        if order_by not in valid_orders:
            raise ValueError(f"Invalid order_by value. Must be one of {valid_orders}.")
        
        subreddit = self.reddit.subreddit(subreddit)
        posts = []
        # Fetch posts based on the order_by parameter
        if order_by == 'new':
            submissions = subreddit.new(limit=limit)
        elif order_by == 'hot':
            submissions = subreddit.hot(limit=limit)
        elif order_by == 'top':
            submissions = subreddit.top(limit=limit)
        elif order_by == 'rising':
            submissions = subreddit.rising(limit=limit)
        
        # Extract relevant features from the submissions
        for submission in submissions:
            post = {feature: getattr(submission, feature, None) for feature in features}
            post['created_utc'] = datetime.utcfromtimestamp(post['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
            posts.append(post)
        return posts


if __name__ == "__main__":

    TEST_SUBREDDDIT = r'learnmachinelearning'
    handler = RedditHandler(TEST_SUBREDDDIT)

    # Fetch new posts
    new_posts = handler.fetch_subreddit_data(order_by='new', limit=10)

    # Print the new posts
    print("New Posts:")
    for post in new_posts:
        print(post)
        print("\n")