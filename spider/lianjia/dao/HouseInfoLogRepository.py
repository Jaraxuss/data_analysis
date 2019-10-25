from typing import List

from spider.lianjia.dao.mysqlClient import mysqlClient
from spider.lianjia.model.HouseInfoLog import HouseInfoLog


class HouseInfoLogRepository(object):

    @staticmethod
    def selectByPrimarykey(id: str) -> HouseInfoLog:
        """
        :param id: '17bce22f9e5d1651709da3df0e163a893568964b1f40084942258441484bbe84'
        :return:
        """

        session = mysqlClient.DBSession()
        houseInfoLog = session.query(HouseInfoLog).filter(HouseInfoLog.id == id).first()
        return houseInfoLog

    @staticmethod
    def selectByIdList(idList: list):
        """
        :param idList: ['17bce22f9e5d1651709da3df0e163a893568964b1f40084942258441484bbe84']
        :return:
        """

        session = mysqlClient.DBSession()
        houseInfoLogList = session.query(HouseInfoLog).filter(HouseInfoLog.id.in_(idList)).all()

        return houseInfoLogList

    @staticmethod
    def insert(houseInfoLog: HouseInfoLog):
        """
        :param id: '17bce22f9e5d1651709da3df0e163a893568964b1f40084942258441484bbe84'
        :return:
        """


        # print(houseInfoLog.__dict__)

        session = mysqlClient.DBSession()
        session.add(houseInfoLog)
        session.commit()

    @staticmethod
    def insertList(houseInfoLogList: List[HouseInfoLog]):
        """
        :param id: '17bce22f9e5d1651709da3df0e163a893568964b1f40084942258441484bbe84'
        :return:
        """

        session = mysqlClient.DBSession()
        session.add_all(houseInfoLogList)
        session.commit()
