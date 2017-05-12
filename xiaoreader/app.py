from flask import Flask, jsonify, make_response, request, abort

from xiaoreader.db.mymongo import MyMongo

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


# POST方法API，添加数据项
@app.route('/search', methods=['POST'])
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
        item.update({'id': idx + 1})
        results.append(item)
    return jsonify({'results': results}), 201


# 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
