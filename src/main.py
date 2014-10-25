'''
Created on 23-Oct-2014

@author: Rahul

@summary: Main file to drive data collection, sentiment calculation, and
         serialization.
'''
from integrations.twitter import Collector
from integrations.settings import TWITTER_CREDS, TWITTER_SEARCH_PARAMS,\
    OUTPUT_FILE, FIELDS_TO_SAVE
from core.sentiment import get_sentiment_for_text
from serializers.csv import write


TWITTER_HANDLES = {
    "microsoft": ["@microsoft", "@bing"]
}



def prepare_to_serialize(source, company, identifiers, text_sentiment):
    '''
        Prepares the data in the format that is convenient for serialization
    '''
    return {"source": source,
            "company": company,
            "identifiers": str(identifiers),
            "created_at": text_sentiment[0],
            "text": text_sentiment[1],
            "sentiment": text_sentiment[2][0],
            "p_pos": text_sentiment[2][1],
            "p_neg": text_sentiment[2][2]
            }


def sentiment_on_twitter(twitter_handles):
    '''
        Integrates twitter data and performs sentiment analysis.
    '''
    source = "twitter"

    for company, handles in twitter_handles.items():
        print "\n\n Processing: %s" % (handles)

        print "Getting data from twitter.. "
        tweets = Collector(TWITTER_CREDS).get_updates(handles, **TWITTER_SEARCH_PARAMS)  # @IgnorePep8

        print "Preparing data to serialize.. "
        tweets = [(tweet.created_at, tweet.text.encode('utf-8'), get_sentiment_for_text(tweet.text.encode('utf-8'))) for tweet in tweets]  # @IgnorePep8

        print "Serializing data in CSV format.. "
        ofile = OUTPUT_FILE
        fields = FIELDS_TO_SAVE
        tweets = [prepare_to_serialize(source, company, handles, tweet) for tweet in tweets]  # @IgnorePep8
        write(ofile, fields, tweets)

if __name__ == '__main__':
    sentiment_on_twitter(TWITTER_HANDLES)
