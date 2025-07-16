import praw
import re
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def init_reddit():
    return praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent="HuggingFacePersonaApp"
    )

def extract_username_from_url(url):
    return re.findall(r"reddit\.com/user/([^/]+)", url)[0]

def fetch_user_content(username, reddit_instance, limit=100):
    user = reddit_instance.redditor(username)
    
    posts = []
    for submission in user.submissions.new(limit=limit):
        posts.append({
            'title': submission.title,
            'selftext': submission.selftext,
            'subreddit': str(submission.subreddit),
            'url': submission.url
        })
    
    comments = []
    for comment in user.comments.new(limit=limit):
        comments.append({
            'body': comment.body,
            'subreddit': str(comment.subreddit),
            'link': f"https://www.reddit.com{comment.permalink}"
        })
    
    return posts, comments
