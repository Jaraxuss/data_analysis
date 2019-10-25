from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from spider.lianjia.settings import mysqlConfig


class MySQLClient:

    def __init__(self):
        print('* Initialize MySQL connection ...')

        self.engine = create_engine('mysql+pymysql://' + mysqlConfig["user"] + ':' + mysqlConfig["password"] + '@' + mysqlConfig["host"] + ':' + mysqlConfig["port"] + '/' + mysqlConfig["database"],
                                    pool_size=10,
                                    pool_recycle=3600,
                                    # echo=True,
                                    encoding='utf-8')

        self.DBSession = sessionmaker(bind=self.engine)


mysqlClient = MySQLClient()
