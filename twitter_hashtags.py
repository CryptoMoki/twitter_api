import tweepy
import csv

# Keys, tokens and secrets
consumer_key = "K3R5G3vBTJe4ioUcYBOxPT5RK"
consumer_secret = "aTrxNt1J6EvGHWnZuq5bNv0AUS7JJQA30pEjDSPAO80dIopg40"
access_token = "1008057460555374592-m0VycqkTiomreUNymjiJGaRL5IgEEm"
access_token_secret = "KJ7wD2mhYeuig5gfrmUVT2S38g4bSDw6OigNTComk1agu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

hashtags = [None] * 100
count = 0

# Open/Create a file to append data
with open('hashtags.csv', 'r') as f:
    file = csv.reader(f)
    for row in file:
        if (row[0] == ''):
            continue
        hashtags[count] = row[0]  # All your targets here
        count += 1

for tag in hashtags:
    with open('{}.csv'.format(tag), 'w+') as f:
        file = csv.writer(f)
        file.writerow(['date', 'user', '# of favorites', '# of retweets', 'tweet'])
        for tweet in tweepy.Cursor(api.search, q="{}".format(tag), count=100,
                           lang="en", since="2018-08-01").items():
            if tweet.retweeted is True:
                continue
            file.writerow([tweet.created_at, tweet.user.screen_name, tweet.favorite_count, tweet.retweet_count,
                           tweet.text])
        print("finding tweets with {} is done".format(tag))
