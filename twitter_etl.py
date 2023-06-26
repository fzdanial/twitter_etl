import pandas as pd
import s3fs
import tweepy
import json
from datetime import datetime
import keys #py file for API keys (not uploaded on GH)

#authentication
auth = tweepy.OAuthHandler(keys.access_key, keys.access_secret)
auth.set_access_token(keys.consumer_key, keys.consumer_secret)

#API object creation
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#tweet extraction
# tweets = api.user_timeline(screen_name = '@fzdanial',
#                            count = 200, #how many to download
#                            include_rts = False, #wanna ignore rts
#                            tweet_mode = 'extended' #
#                            )

# print(tweets)