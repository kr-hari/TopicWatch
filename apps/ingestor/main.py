from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List
from apps.ingestor.reddit_handler import RedditHandler


app = FastAPI()
reddit_handler = RedditHandler()


# Get Endpoint: Fetch from a single subreddit data
@app.get("/fetch_subreddit/single")
def fetch_subreddit_data(
    subreddit: str = Query(..., description="Subreddit name"),
    order_by: str = Query("new", description="Order to fetch data by. Can be 'new', 'hot', 'top', etc."),
    limit: int = Query(1000, description="Maximum number of posts to fetch")
):
    """
    Fetches data from a single subreddit based on the specified order.
    """
    try:
        posts = reddit_handler.fetch_subreddit_data(
            subreddit=subreddit, order_by=order_by, limit=limit
        )
        return {"data": posts}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

# Post Endpoint: Fetch from multiple subreddits data
@app.post("/fetch_subreddit/multiple")
def fetch_multiple_subreddits_data(
    subreddits: List[str] = Query(..., description="List of subreddit names"),
    order_by: str = Query("new", description="Order to fetch data by. Can be 'new', 'hot', 'top', etc."),
    limit: int = Query(1000, description="Maximum number of posts to fetch per subreddit")
):
    """
    Fetches data from multiple subreddits based on the specified order.
    """
    try:
        posts = reddit_handler.fetch_all_subreddits(
            list_of_subreddits=subreddits, order_by=order_by, limit=limit
        )
        return {"data": posts}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))