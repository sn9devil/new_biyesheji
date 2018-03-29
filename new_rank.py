import requests
import time
import re
from data_processing import rank_update,new_rank_sort
from bs4 import BeautifulSoup

if __name__ == '__main__':
    while(1):
        html = 'http://news.163.com/rank/'
        response = requests.get(html)
        # response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        news = soup.select('.tabContents')
        new_list = new_rank_sort(news[7])
        rank_update(new_list)
        print('已更新')
        time.sleep(60)
