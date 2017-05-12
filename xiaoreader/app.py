from flask import Flask, jsonify, make_response, request, abort

from xiaoreader.db.mymongo import MyMongo
import time

# 静态文件的放置路径，可根据实际情况设置，这里设置为默认路径：'./static/'
app = Flask(__name__, static_url_path='')

# 模拟json数据
mongo = MyMongo()


def get_results(key):
    res = mongo.get_many('xiao', 'wxread', 'title', key)
    return res if res else []


def get_soft_results(key):
    res = mongo.get_many_regex('xiao', 'wxread', 'title', key)
    return res if res else []


# 设置根路由
@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/item/<bookid>', methods=['GET'])
def item(bookid):
    return app.send_static_file('item.html')


# @app.route('/item/<bookid>', methods=['GET'])
# def book(bookid):
#     result = mongo.get_one('xiao', 'wxread', 'id', bookid)
#     return app.make_response((json.dumps(result), 200))



@app.route('/api/item', methods=['POST'])
def get_item():
    __order__ = ['id', 'url', 'title', 'cate', 'intro', 'vote_cnt', 'star']

    if request.json['bid'] == "":
        abort(400)

    bid = request.json['bid']

    result = mongo.get_one('xiao', 'wxread', 'id', bid)

    order_result = []
    for name in __order__:
        order_result.append({'key': name, 'value': result.get(name)})

    return jsonify({'result': order_result}), 200


# POST方法API，添加数据项
@app.route('/api/search', methods=['POST'])
def search():
    if request.json['query'] == "":
        abort(400)

    key = request.json['query']
    result_list = get_soft_results(key)

    results = []

    # 排序
    if result_list:
        result_list.sort(key=lambda x: x['vote_cnt'], reverse=True)

    for idx, item in enumerate(result_list):
        dic = {'seqid': idx + 1, 'date': get_current(), 'url': '/item/{}'.format(item['id']),
               'short': '{}...'.format(item['intro'][:110]) if len(item['intro']) >= 110 else item['intro']}
        item.update(dic)
        results.append(item)
    return jsonify({'results': results}), 200


def get_current():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


# 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
