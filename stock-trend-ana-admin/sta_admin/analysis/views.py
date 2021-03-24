import logging
from datetime import datetime

from ModelLoader import StockModel
from JsonResponseResult import JsonResponseResult
from NewCollector import crawl_news
from SentimentalAnalyzer import generate_score
from StockDataGenerator import StockDataGenerator
from StockMetaData import StockMetaData

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


def get_basic_info(request, ticker, start_date):
    # keep same data structure with// https://echarts.apache.org/examples/data/asset/data/stock-DJI.json
    # sample viz https://echarts.apache.org/examples/zh/editor.html?c=candlestick-brush
    # data columns: datetime, open, close, lowest, highest, volume
    logger.info("parameter stock is: ----> ", ticker)
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    metadata = StockMetaData(ticker, start_date_obj)
    generator = StockDataGenerator(metadata)
    _, data_items = generator.download_basic_info()
    if len(data_items) > 0:
        return JsonResponseResult().ok(data=data_items)
    else:
        return JsonResponseResult().error(code=405,
                                          data="failed to download data of " + ticker + ", please check trickier.")


def predict_future_price(request, ticker, start_date):
    logger.info("parameter stock is: ----> ", ticker)
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    metadata = StockMetaData(ticker, start_date_obj)
    generator = StockDataGenerator(metadata)
    model = None
    try:
        model = StockModel(metadata)
        model.load()
    except FileNotFoundError:
        return JsonResponseResult().error(code=405,
                                          data="failed to load model file of " + ticker + ", please check trickier.")
    y_test = model.predict(generator)
    if len(y_test) > 0:
        return JsonResponseResult().ok(data=y_test)
    else:
        return JsonResponseResult().error(code=405,
                                          data="failed to predict future value of " + ticker)


def get_latest_news(request, ticker):
    logger.info("parameter stock is: ----> ", ticker)
    raw_news = crawl_news(ticker)
    if len(raw_news) > 0:
        scored_news = generate_score(raw_news, textKey="content")
        return JsonResponseResult().ok(data=scored_news)
    else:
        return JsonResponseResult().error(code=405, data="failed to get current news data of " + ticker)
