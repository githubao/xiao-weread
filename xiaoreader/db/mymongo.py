#!/usr/bin/env python
# encoding: utf-8

"""
@description:python 的mongo操作接口

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: mymongo.py
@time: 2017/2/8 14:15
"""

from pymongo import MongoClient


class MyMongo():
    url = 'mongodb://127.0.0.1:27017'

    def __init__(self):
        self.client = MongoClient(self.url)

    def _get_db(self, db):
        return self.client[db]

    def get_one(self, db, coll, key, value):
        datebase = self._get_db(db)
        collect = datebase[coll]
        return collect.find_one({key: value}, {'_id': 0})

    def get_many(self, db, coll, key, value):
        datebase = self._get_db(db)
        collect = datebase[coll]
        items = collect.find({key: value}, {'_id': 0})
        if items:
            return [item for item in items]
        return None

    def get_all(self, db, coll):
        datebase = self._get_db(db)
        collect = datebase[coll]
        rs = collect.find()
        return [item for item in rs]

    def count(self, db, coll):
        datebase = self._get_db(db)
        collect = datebase[coll]
        return collect.count()

    def set_one(self, db, coll, item):
        datebase = self._get_db(db)
        collect = datebase[coll]
        return collect.insert_one(item)

    def close(self):
        self.client.close()


def test_mongo():
    db = 'xiao'
    mongo = MyMongo()

    coll='wxread'
    key='title'
    value='红楼梦'

    res = mongo.get_many(db, coll, key, value)

    print(res)


def main():
    test_mongo()


if __name__ == '__main__':
    main()
