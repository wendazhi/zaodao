import pymysql
from setting import *
class mysqlDB(object):
    def __init__(self,host='localhost',port='3306',user='root',password='$4jj',database='lanxian',charset='utf8',table='baseinfo'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.table = table

        self._db = self.db_connect()
        self.db_set_charset()

    def db_connect(self):
        return pymysql.connect(host=self.host, port=self.port, username=self.user, password=self.password, db=self.database,charset=self.charset)

    def getInstance(self):

        pass


    def db_set_charset(self):
        self._db.set_charset(self.charset)


    def insert(self,data):



        sql = '''
            "INSERT INTO self.table() VALUES(
            data['companyName'],
            data['companyDomain'],
            data['baseInfoCorporate'],
            data['baseInfoCapital'],
            data['baseInfoEstablish'],
            data['baseInfoTel'],
            data['baseInfoEmail'],
            data['baseInfoAddr']"
            '''

        print(sql)

if __name__ == '__main__':
    data = {'companyName': '太钢集团\n岚县\n矿业有限公司', 'companyDomain': '/company/ba1e72f0-14c3-4755-a0ad-b078f7314edb', 'baseInfoCorporate': '法人代表：马法成', 'baseInfoCapital': '注册资本：75亿', 'baseInfoEstablish': '成立时间：2009-10-13', 'baseInfoTel': '电话：03586796152', 'baseInfoEmail': '邮箱：tgjtlxkyyxgs@163.com', 'baseInfoAddr': '地址：山西省吕梁市\n岚\n县\n梁家庄乡索家坡村'}
    db = mysqlDB()
    db.insert(data)

    # 当一个字符串转换为内部编码后，它就不是str类型了！它是unicode类型