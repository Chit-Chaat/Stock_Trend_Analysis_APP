__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/13/2021 2:56 AM'

import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger('NewCollector Module')
source_url = 'https://finviz.com/quote.ashx?t='


def crawl_news(identifier, size=10):
    url = source_url + identifier
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
    response = requests.get(url=url, headers=headers)
    content_list = []
    if response.status_code == 200:
        html_content = BeautifulSoup(response.text, features="html.parser")
        content_table = html_content.find(id='news-table').findAll('tr')
        current_date_prefix = ""
        for i, row in enumerate(content_table):
            content = row.a.text
            new_s_url = row.a.attrs['href']
            time_str = str(row.td.text).strip()
            if len(time_str) > 7:
                prefix, date_str = time_str.split(' ')
                current_date_prefix = prefix
            else:
                time_str = current_date_prefix + ' ' + time_str
            content_list.append({
                "content": content,
                "timestamp": time_str,
                "url": new_s_url
            })
            if i == size:
                break
    else:
        logger.warn("Something bad happened, when crawl news data. since the Http Code is " + str(response.status_code))

    return content_list
