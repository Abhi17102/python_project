import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read credentials from environment
api_key = os.getenv("API_KEY")
api_key_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate using OAuth1.0a
auth = tweepy.OAuth1UserHandler(
    api_key,
    api_key_secret,
    access_token,
    access_token_secret
)

# Create API client
api = tweepy.API(auth)

# Your tweet message
tweet = "🚀 Tweeting from Python using Tweepy + .env for security! #Python #Tweepy #Automation"

# Post the tweet
try:
    api.update_status(tweet)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print(f"❌ Failed to post tweet: {e}")
