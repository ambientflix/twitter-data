import sys, tweepy
import re
import string

# Authorizes access to the Twitter API
def twitter_auth():
    try:
        consumer_key = "DSt3NyAqOGFEGyUWzLRYZcx1g"
        consumer_secret = "581Fs2Q0hDctuMISQ83EkNp8xwc5JSu2wWB18hbYfjpR55dvO5"
        access_token = "1143319962653560832-ggi4PS3OGStUcC5RLSPaV5YhwjJkE5"
        access_secret = "ZU48qIyslkpy6qVDRocKcXBDA7uS3ox7anwbtC5WJZHb7"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variable not set\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

# Creates connection to the twitter API
def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return client

if __name__ == "__main__":
    s = ""
    user = "Allen_Lin_"
    client = get_twitter_client()
    # Get's the last 30 tweets in your feed... this would be from people you follow and what
    # they tweet or retweet
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(30):
        s += status.text

    # Parse it a little bit
    table = str.maketrans('', '', string.punctuation)
    s = re.split(r'\W+', s)
    stripped = [w.translate(table) for w in s]
    words = [word.lower() for word in stripped]
    feedData = open("feedData.txt", "w")
    for word in words:
        feedData.writelines(word+"\n")
