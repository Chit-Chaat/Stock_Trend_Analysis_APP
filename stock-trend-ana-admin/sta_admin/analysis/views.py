import logging

from JsonResponseResult import JsonResponseResult

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
