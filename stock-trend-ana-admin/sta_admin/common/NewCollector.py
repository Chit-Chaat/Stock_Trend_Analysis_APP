__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/13/2021 2:56 AM'

import requests
from bs4 import BeautifulSoup

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
            time_str = str(row.td.text).strip()
            if len(time_str) > 7:
                prefix, date_str = time_str.split(' ')
                current_date_prefix = prefix
            else:
                time_str = current_date_prefix + ' ' + time_str
            content_list.append({
                "content": content,
                "time": time_str,
            })
            if i == size:
                break

    return content_list
