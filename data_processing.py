import re
import tool
import pymongo
from pymongo import MongoClient


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

def rank_update(data):
    my_set = MClient_rank()
    my_set.drop()
    for i in data:
        new_insert(my_set,i)


def new_insert(Client,data):
    Client.insert(data)


def new_find(url):
    my_set = MClient()
    return bool(my_set.find_one({'url':url}))


def new_update(url,hot):
    my_set = MClient()
    my_set.update({'url':url},{'$set':{'hot':hot}})

def data_sort(data):
    a = 6
    datas = []
    for i in range(7):
        url_pattern = re.compile(r'href="(.*)" ')   #href正则
        url = re.findall(url_pattern,str(data[a]))[0]

        tag_pattern = re.compile(r'target="_blank">(.*?)</a>')  #标题正则
        tag = re.findall(tag_pattern, str(data[a]))[0]

        hot_pattern = re.compile(r'<td nowrap="">(.*)</td>') #热度正则
        hot = re.findall(hot_pattern, str(data[a+1]))[0]

        time_pattern = re.compile(r'<td nowrap="">(.*)-(.*)-(..)')
        times = re.findall(time_pattern, str(data[a+2]))
        for i in re.findall(time_pattern, str(data[a+2])):
            mon = i[1]
            day = i[2]
        date = mon + '.' + day
        new_data ={
            'url':url,
            'tag':tag,
            'hot':hot,
            'date':date
        }
        datas.append(new_data)
        a += 5
    return datas

def new_rank_sort(data):
    urls = []
    tags = []
    pattern = re.compile(r'<a(.*?)</a>')
    a = re.findall(pattern, str(data))
    for i in a:
        url_pattern = re.compile(r'href="(.*?)">')
        urls.append(re.findall(url_pattern, i))

        tag_pattern = re.compile(r'">(.*)')
        tags.append(re.findall(tag_pattern, i))

    hot_pattern = re.compile(r'<td class="cBlue">(.*?)</td></tr>')
    hots = re.findall(hot_pattern, str(data))
    new_list=[]
    date = tool.now_time()
    for a,b,c in zip(urls,tags,hots):
        new={
            'url':a[0],
            'tag':b[0],
            'hot':str(c),
            'date':date
        }
        new_list.append(new)

    return new_list

