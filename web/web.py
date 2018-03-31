from flask import Flask,render_template
from data_tool import rank_find_all,data_sort,old_new_sort,MClient_rank,now_time
app = Flask(__name__)


@app.route('/')
def index():
    my_set = MClient_rank()
    lists = rank_find_all()
    datas = data_sort(my_set,lists)
    time = now_time()
    news = old_new_sort()
    # print(datas)
    return render_template('index.html',datas=datas,time=time,news=news)


if __name__ == '__main__':
    app.run()
