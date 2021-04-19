__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/13/2021 5:08 AM'

import datetime

import nltk

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def generate_score(rawData, textKey, scoreKey="score"):
    analyzer = SentimentIntensityAnalyzer()
    for kv in rawData:
        value = kv[textKey]
        scores = analyzer.polarity_scores(value)
        kv[scoreKey] = scores
        if scores['compound'] > 0:
            kv['type'] = "success"
            kv['icon'] = "el-icon-circle-check"
        elif scores['compound'] < 0:
            kv['type'] = "error"
            kv['icon'] = "el-icon-error"
            kv['color'] = '#F56C6C'
        else:
            kv['type'] = "info"
            kv['icon'] = "el-icon-info"
    return rawData


def calculate_proportion(rawData, textKey, scoreKey="score"):
    positive_val, negative_val, neutral_val = 0.0, 0.0, 0.0
    analyzer = SentimentIntensityAnalyzer()
    for kv in rawData:
        date_str = kv['timestamp'].split(' ')[0]
        date_obj = datetime.datetime.strptime(date_str, '%b-%d-%y')
        today_obj = datetime.datetime.today() - datetime.timedelta(days=2)
        if today_obj <= date_obj:
            # if it is today's news
            value = kv[textKey]
            scores = analyzer.polarity_scores(value)
            positive_val += scores['pos']
            negative_val += scores['neg']
            neutral_val += scores['neu']

    emotion_sum = max(positive_val + negative_val + neutral_val, 1)
    result = [
        {'icon': 'icon-rate-face-3', 'color': '#FF9900', 'name': 'positive', 'value': round(positive_val, 2),
         'proportion': str(round(positive_val * 100 / emotion_sum, 1)) + '%'},
        {'icon': 'icon-rate-face-1', 'color': '#F7BA2A', 'name': 'negative', 'value': round(negative_val, 2),
         'proportion': str(round(negative_val * 100 / emotion_sum, 1)) + '%'},
        {'icon': 'icon-rate-face-2', 'color': '#99A9BF', 'name': 'neutral', 'value': round(neutral_val, 2),
         'proportion': str(round(neutral_val * 100 / emotion_sum, 1)) + '%'},
    ]
    return result
