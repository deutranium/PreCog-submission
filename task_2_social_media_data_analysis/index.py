import secrets as s
import tweepy
import csv
from time import sleep

####input your credentials here
consumer_key = s.consumer_key
consumer_secret = s.consumer_secret
access_token = s.access_token
access_token_secret = s.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Use Delhi's WOEID
tags = api.trends_place(20070458)
top_tags = tags[0]['trends']
top_tag = ""

for tag in top_tags:
    if tag['name'].startswith("#"):
        top_tag = tag['name']
        break

# Open/Create a file to append data
csvFile = open('data6.csv', 'a')
# #Use csv Writer
csvWriter = csv.writer(csvFile)

# print(top_tag)
csvWriter.writerow(["tweet_id", "tweet_full_text", "tweet_created_at", "tweet_lang", "hashtags", "tweet_retweet_count", "tweet_favorite_count", "tweet_place", "user_id", "user_screen_name", "user_followers_count", "user_friends_count", "user_created_at", "user_favourites_count", "user_statuses_count", "user_lang", "user_verified", "user_location"])
i = 1

tweets = tweepy.Cursor(api.search, tweet_mode="extended", q="#FarmersDyingModiEnjoying exclude:retweets").items(11000)

while(True):
    try:
        for tweet in tweets:
                hashtags = "#" + " #".join([hashtag['text'] for hashtag in tweet.entities.get('hashtags')])
                print(i)

                if tweet.place:
                    tweet_place = tweet.place.full_name + ', ' + tweet.place.country_code
                else:
                    tweet_place = "Not Geo-tagged"
                i += 1
                
                csvWriter.writerow([tweet.id, tweet.full_text.encode('utf-8'), tweet.created_at, tweet.lang, hashtags, tweet.retweet_count, tweet.favorite_count, tweet_place, tweet.user.id, tweet.user.screen_name, tweet.user.followers_count, tweet.user.friends_count, tweet.user.created_at, tweet.user.favourites_count, tweet.user.statuses_count, tweet.user.lang, tweet.user.verified, tweet.user.location])
        # break
    except tweepy.TweepError:
        print("tweeeeeeeeeeep")
        sleep(14)
        continue

    except IOError:
        print("iiiiiiiiioooooo")
        sleep(14)
        continue
