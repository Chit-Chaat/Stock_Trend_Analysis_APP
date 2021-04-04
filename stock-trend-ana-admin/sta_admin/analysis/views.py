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


def test(request):
    logger.info('this is a sample request')
    data = [1, 2, 3, 4, 5, 6, 7]
    return JsonResponseResult().ok(data=data)


def bad_request(request):
    logger.info('this is a sample request')
    return JsonResponseResult().error(data="this is sample error")


def get_basic_info(request, ticker, start_date):
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


def get_candle_render_data(request, ticker, start_date):
    # sample viz https://echarts.apache.org/examples/zh/editor.html?c=candlestick-brush
    # returning data structure should be look like this:
    # stock_data: {
    #     categoryData: ["2020-12-18", "2020-12-19", "2020-12-20", "2020-12-21", "2020-12-22"],
    #     values: [[3243.989990234375, 3201.64990234375, 3171.60009765625, 3249.419921875],
    #              [3200.010009765625, 3206.179931640625, 3166.0, 3226.969970703125],
    #              [3202.840087890625, 3206.52001953125, 3180.080078125, 3222.0],
    #              [3205.0, 3185.27001953125, 3184.169921875, 3210.1298828125],
    #              [3193.89990234375, 3172.68994140625, 3169.0, 3202.0]],
    #     volumes: [[0, 5995700, 1], [1, 3836800, 1], [2, 2369400, -1], [3, 2093800, 1], [4, 1451900, -1]],
    #     MA5: [3243, 3200, 3202, 3205, 3193],
    #     MA10: [3243, 3201, 3212, 3235, 3199],
    #     MA20: [3233, 3220, 3222, 3225, 3198],
    #     MA30: [3223, 3210, 3232, 3215, 3197],
    # },
    logger.info("parameter stock is: ----> ", ticker)
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    metadata = StockMetaData(ticker, start_date_obj)
    generator = StockDataGenerator(metadata)
    data_obj = generator.download_and_wrap_basic_info()
    if data_obj is not None:
        return JsonResponseResult().ok(data=data_obj)
    else:
        return JsonResponseResult().error(code=405,
                                          data="failed to download data of " + ticker + ", please check trickier.")


def predict_future_price(request, ticker, start_date="2015-01-01"):
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
