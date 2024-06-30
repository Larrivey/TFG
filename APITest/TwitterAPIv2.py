import tweepy
import auth
access_token = "1273356146187919364-aIA2tCmt3I1X3gYrgQhM8Qjx2dWpRR"
access_token_secret = "LdhKFNOrQxoJv5g0uhlGmJlKEOdQdmfKv9Umik7MEpJmr"
api_key = "73TAdmz4Ml0ERGqupqNsB6ZPv"
api_key_secret = "KYS57fppGvRxsuhtspiPkiiu35GAURsPw6MRhPuHCS0kAPq464"


auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Succesful Authentication')
except:
    print('Failed authentication')

#blocks = api.get_blocks()
api.get_followers()
print(blocks)