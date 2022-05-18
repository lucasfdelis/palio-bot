import tweepy
from acesso import token
auth = tweepy.OAuthHandler(token[0], token[1])
auth.set_access_token(token[3], token[4])
api = tweepy.API(auth)

for tweet in api.search_tweets(q="Palio",
                               lang="pt-BR",
                               result_type="recent",
                               count=100):
    if tweet.user.id_str == "1526710339676545029":
        pass
    else:
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                print(e)
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                print(e)
