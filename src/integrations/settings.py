'''
Created on 23-Oct-2014

@author: Rahul

@summary: Holds settings like access tokens and API secrets.
'''
import datetime

TWITTER_CREDS = {
    "API_KEY": "X2hc4sGgCTt6CRFESCL3wWz1V",
    "API_SECRET": "Fqf8qFMkazjRsWN2WCPY2KCKELTQKdUrNckRkLRzAKGEzoZmqT",
    "ACCESS_TOKEN": "161699092-OceTQyDBtgQV7ZcY3vN2yx1P1haCbEhIHwgxn3xf",
    "ACCESS_TOKEN_SECRET": "7RClKpGWRQycLNTCLci6kAnrjtSEQ7Cjh4TnKkMl92jOb"
}

TWITTER_SEARCH_PARAMS = {
    "count": 100,
    "since_id": "5259984495239823"
}

# The output file to save the sentiment results in csv format.
OUTPUT_FILE = "sentiment-results.csv"

FIELDS_TO_SAVE = ["source", "company", "identifiers", "created_at", "text",
                  "sentiment", "p_pos", "p_neg"]
