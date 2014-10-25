'''
Created on 23-Oct-2014

@author: Rahul

@summary: Holds all the code required to get data from twitter.
'''
import tweepy


class Collector(object):
    '''
        Collects the data from twitter.
    '''
    def __init__(self, creds):
        '''
            Initialize.
        '''

        # Setup the auth and get the api client.
        consumer_key = creds.get("API_KEY")
        consumer_secret = creds.get("API_SECRET")
        access_token = creds.get("ACCESS_TOKEN")
        access_token_secret = creds.get("ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Initialize the API client.
        self.api_client = tweepy.API(auth)

    def get_updates(self, twitter_handles, **options):
        '''
            For all the given companies, tries to get the data between start
            date and end data.
        '''
        search_param = ' OR '.join(twitter_handles)
        tweets = [tweet for tweet in self.api_client.search(search_param, **options)]  # @IgnorePep8
        return tweets
