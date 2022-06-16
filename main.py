import time
import tweepy
from acesso import token
auth = tweepy.OAuthHandler(token[0], token[1])
auth.set_access_token(token[3], token[4])
api = tweepy.API(auth)

while True:
    for tweet in api.search_tweets(q="Palio",
                                   lang="pt",
                                   result_type="recent",
                                   count=100):
        if tweet.user.id_str == "1526710339676545029":
            pass
        else:
            print('Postagem: ', tweet.text)
            try:
                tweet.favorite()
            except Exception as e:
                print(e)
                print('O Bot já favoritou essa postagem.')
            try:
                tweet.retweet()
            except Exception as e:
                print(e)
                print('O bot já retweetou essa postagem.')
            print(' ')
    print('Pausando pesquisa por 5 minutos...')
    time.sleep(300)
