import tweepy

consumer_key = "DzxByQz6RSXs5ye8hd0lo74WB"
consumer_secret = "fwtBhjC7hCpj5WtOlT5kpJhTNJCSjgRclfDXGaGOkIpTLuBkUU"
access_token = "1657500964319002624-hzziYst9gV7AbFYsBZvHhYIyuIlZf1"
access_token_secret = "yNO7At262a4KorFgdscXvWrdkhFzUaASi0Xp2HORS1vyn"
bearer = 'AAAAAAAAAAAAAAAAAAAAADjlnQEAAAAATgCWkkLf%2Bvjk4nEerlz7h5nd4Nc%3DIlMEEaeOTjc4GM4gR7goUBnFBXtbeXDLCskUEiDkc4KY8qOMIQ'

client = tweepy.Client(bearer_token=bearer, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

client.create_tweet(text="Yeah boy! I did it")