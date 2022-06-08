from webbrowser import get
import tweepy
import os
#live tweets from a specific user
def get_tweets(username):
    auth = tweepy.OAuthHandler(os.environ["consumer_key"], os.environ["consumer_secret"])
    auth.set_access_token(os.environ["access_token"], os.environ["access_token_secret"])
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=username, count=1, include_rts=False,exclude_replies=True)
    return tweets
#tweet urls from a specific user
def get_tweet_urls(username):
    tweets = get_tweets(username)
    urls = []
    for tweet in tweets:
        urls.append(tweet.text)
        print(tweet.text)
    return urls

get_tweet_urls('genshinimpact')