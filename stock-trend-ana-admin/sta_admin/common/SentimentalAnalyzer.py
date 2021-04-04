__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/13/2021 5:08 AM'

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
            kv['type']="info"
            kv['icon'] = "el-icon-info"
    return rawData
