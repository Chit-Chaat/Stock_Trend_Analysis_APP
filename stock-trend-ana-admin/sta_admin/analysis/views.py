import logging

from JsonResponseResult import JsonResponseResult
from NewCollector import crawl_news
from SentimentalAnalyzer import generate_score

logger = logging.getLogger('analysis module')


def index(request):
    logger.info('this is a sample request')
    data = {
        "areas": [
            'New England', 'Mid East', 'Great Lakes',
            'Plains', 'Southeast', 'Southwest',
            'Rocky Mountains', 'Far West', 'Outlying areas'],
        "nums": {
            "odd": [1, 3, 5],
            "even": [2, 4, 6]
        },
        "tuitions": ['<= $5k', '<= $10k', '<= $15k']
    }
    return JsonResponseResult().ok(data=data)


def bad_request(request):
    logger.info('this is a sample request')
    return JsonResponseResult().error(data="this is sample error")


def get_latest_news(request, stock):
    logger.info("parameter stock is: ----> ", stock)
    raw_news = crawl_news(stock)
    if len(raw_news) > 0:
        scored_news = generate_score(raw_news, textKey="content")
        return JsonResponseResult().ok(data=scored_news)
    else:
        return JsonResponseResult().error(code=501, data="failed to get current news data")
