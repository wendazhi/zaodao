import pymongo
import redis
from zaodao.config import *


class Save(object):
    def __init__(self):
        self.Redis_init()
        self.MongoDB_init()

    def Redis_init(self):
        self.r_db = redis.Redis(host=HOST, port=PORT, password=PASSWORD)

    def MongoDB_init(self):
        client = pymongo.MongoClient(MONGO_URL)
        self.m_db = client[MONGO_TABLE]

    def save_to_mongoDB(self, content):
        try:
            if not self.m_db[MONGO_TABLE].find({"companyName": content['companyName']}).count():

                if self.m_db[MONGO_TABLE].insert(content):
                    print(content['companyName'], '数据存储到mongoDB成功!')
            else:
                print(self.m_db[MONGO_TABLE].find({"companyName": content['companyName']}))
                print(content['companyName'], "已存在mongoDB数据库中")
        except Exception:
            print(content['companyName'], '数据存储到mongoDB失败!')

    def save_to_redis(self, content):
        try:
            self.r_db.lpush(REDIS_TABLE, content)
            print('保存到redis成功!')
        except:
            print('保存到redis失败')

    def save_to_file(self, content):
        data = ''
        for (field, value) in content.items():
            data += '%s\t' % (value)
        data = data + '\n'
        with open(FILE_NAME, 'a', encoding='utf-8') as f:
            f.write(data)
