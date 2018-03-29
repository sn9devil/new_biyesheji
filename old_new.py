import requests
import time
from bs4 import BeautifulSoup
from data_processing import MClient,data_sort,new_insert,new_find,new_update

if __name__ == '__main__':
    while(1):
        html = 'http://news.ifeng.com/hotnews/'
        response = requests.get(html)
        response.encoding='utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        news = soup.select('tbody > tr')
        news_data = soup.select('tbody > tr > td')
        datas = data_sort(news_data)
        my_set = MClient()
        for i in datas:
            print(i)
            if(new_find(i['url'])):
                new_update(i['url'],i['hot'])
            else:
                new_insert(my_set,i)
        print('更新完毕')
        time.sleep(60)

