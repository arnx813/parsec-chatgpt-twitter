import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADjlnQEAAAAATgCWkkLf%2Bvjk4nEerlz7h5nd4Nc%3DIlMEEaeOTjc4GM4gR7goUBnFBXtbeXDLCskUEiDkc4KY8qOMIQ')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)