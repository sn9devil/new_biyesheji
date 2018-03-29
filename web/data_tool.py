
from pymongo import MongoClient
import time


def now_time():
    localtime = time.localtime(time.time())
    mon = str(localtime.tm_mon)
    day = str(localtime.tm_mday)
    date = mon + '.' + day
    return date


def MClient():
    client = MongoClient('localhost', 27017)
    db = client['mydb3']
    my_set = db['news']
    return my_set


def MClient_rank():
    client = MongoClient('localhost', 27017)
    db = client['mydb3']
    my_set = db['rank']
    return my_set


def rank_find_all():
    my_set = MClient_rank()
    return my_set.find({"date":now_time()})


def news_find_all(s):
    my_set = MClient()
    return my_set.find({"date":s})


def data_sort(client,datas):
    my_set = client
    hot = []
    sort_list = []
    for i in datas:
        hot.append(int(i['hot']))
    hot.sort(reverse = True)
    for i in hot:
        sort_list.append(my_set.find_one({'hot':str(i)}))
    return sort_list


def time_minus_one(s):
    return str(float(s) - 0.01)


def time_set():
    s = now_time()
    lists = []
    for i in range(4):
        s = time_minus_one(s)
        item = s
        if(len(item)!=5):
            item = '0'+ item
        lists.append(item[0:5])
    return lists


def date_find_one(date):
    my_set = MClient()
    data = my_set.find({'date':date})
    return data


def old_new():
    news= []
    lists = time_set()
    for i in lists:
        news.append(date_find_one(i))
    return news

def old_new_sort():
    lists = old_new()
    item = 0
    for i in lists:
        s = []
        for b in i:
            s.append(b)
        lists[item] = data_sort(MClient(),s)
        item = item + 1
    return lists

