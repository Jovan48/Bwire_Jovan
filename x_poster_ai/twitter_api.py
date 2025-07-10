import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_x(message: str):
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET")

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
    api = tweepy.API(auth)

    try:
        api.update_status(status=message)
        print("✅ Post published to X.")
    except Exception as e:
        print("❌ Failed to post:", e)
