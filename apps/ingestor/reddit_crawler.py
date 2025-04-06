import os 
import re
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any


# TEST_SUBREDDDIT = r''


if __name__ == "__main__":
    # TEST_SUBREDDDIT = r'/r/learnpython'
    # TEST_SUBREDDDIT = r'/r/learnprogramming'
    TEST_SUBREDDDIT = r'/r/learnmachinelearning'
    # TEST_SUBREDDDIT = r'/r/machinelearning'
    # TEST_SUBREDDDIT = r'/r/artificial'
    # TEST_SUBREDDDIT = r'/r/deeplearning'
    # TEST_SUBREDDDIT = r'/r/datascience'
    
    # TEST_SUBREDDDIT = r'/r/learnpython'  # Example subreddit
    reddit_crawler(TEST_SUBREDDDIT)