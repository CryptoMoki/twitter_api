import tweepy
import csv

# Keys, tokens and secrets
consumer_key = "K3R5G3vBTJe4ioUcYBOxPT5RK"
consumer_secret = "aTrxNt1J6EvGHWnZuq5bNv0AUS7JJQA30pEjDSPAO80dIopg40"
access_token = "1008057460555374592-m0VycqkTiomreUNymjiJGaRL5IgEEm"
access_token_secret = "KJ7wD2mhYeuig5gfrmUVT2S38g4bSDw6OigNTComk1agu"

# Tweepy OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

targets = [None] * 100
count = 0

with open('users.csv') as f:
     file = csv.reader(f)
     for row in file:
         if(row[0] == ''):
             continue
         targets[count] = row[0] # All your targets here
         count += 1

with open('results.csv', 'w+') as f:
    file = csv.writer(f)
    file.writerow(['handle', 'name', 'followers_count'])
    for target in targets:
        if target == None:
            continue
        user = api.get_user(target)
        screen_name = user.screen_name
        name = user.name

        file.writerow([user.screen_name, user.name, user.followers_count])
