'''
Created on 23-Oct-2014

@author: Rahul
'''
from textblob.blob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer


def get_sentiment_for_text(text):
    '''
        Returns the sentiment score for the given text.
    '''
    text_analyzer = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    sentiment = text_analyzer.sentiment
    return (sentiment.classification, sentiment.p_pos, sentiment.p_neg)
