# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:00:15 2018

@author: zhangying
"""

import csv
from datetime import datetime

from spider.lianjia.dao.HouseInfoLogRepository import HouseInfoLogRepository
from spider.lianjia.log import MyLog
from spider.lianjia.model.HouseInfoLog import HouseInfoLog
from util.Util import str2timstamp
from sqlalchemy import exc


class HtmlOutputer():
    """数据输出收集模块"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.log = MyLog("html_outputer", "logs")

        datetimeObj = datetime.now(tz=None)
        timestr = str(datetimeObj.year) + "-" + str(datetimeObj.month) + "-" + str(datetimeObj.day)
        self.currtimestamp = str2timstamp(timestr)
        # self.currtimestamp = str(int(time.time()))
        print("================ currtime: " + str(self.currtimestamp) + "================")
        filename = "output//ershoufang.csv"
        with open(filename, "w", newline="") as f:
            data = [
                "id", "小区名称", "所在区域", "总价", "单价",
                "房屋户型", "所在楼层", "建筑面积", "户型结构",
                "套内面积", "建筑类型", "房屋朝向", "建筑结构",
                "装修情况", "梯户比例", "配备电梯", "产权年限",
                "挂牌时间", "交易权属", "上次交易", "房屋用途",
                "房屋年限", "产权所属", "抵押信息", "房本备件",
                "链接", "日志创建时间"
            ]
            writer = csv.writer(f, dialect='excel')
            writer.writerow(data)

    def collect_data(self, data):
        if data is None:
            self.log.logger.error("页面数据收集：传入数据为空！")
            print("页面数据收集：传入数据为空！")
            return

        filename = "output//ershoufang.csv"
        with open(filename, "a", newline="") as f:
            data.append(self.currtimestamp)
            houseInfoLog = HouseInfoLog(houseId=data[0],
                                        communityName=data[1],  # 小区名称
                                        region=data[2],  # 所在区域
                                        totalPrice=data[3],  # 总价（万元）
                                        unitPrice=data[4],  # 单价（元/平米）
                                        buildingArea=data[7],  # 建筑面积
                                        innerArea=None if data[9] == '暂无数据' else data[9],  # 套内面积
                                        houseType=data[5],  # 房屋户型
                                        orientation=data[11],  # 房屋朝向
                                        floor=data[6],  # 所在楼层
                                        houseStructure=data[8],  # 户型结构
                                        renovationCondition=data[13],  # 装修情况
                                        ladderHouseholdProportion=data[14],  # 梯户比例
                                        hasElevator=data[15],  # 配备电梯
                                        buildingType=data[10],  # 建筑类型
                                        buildingStructure=data[12],  # 建筑结构
                                        yearOfPropertyRights=data[16],  # 产权年限
                                        tradingAuthority=data[18],  # 交易权属
                                        housingPurposes=data[20],  # 房屋用途
                                        yearOfHousing=data[21],  # 房屋年限
                                        propertyRights=data[22],  # 产权所属
                                        mortgageInfo=data[23],  # 抵押信息
                                        premisesPermitInfo=data[24],  # 房本备件
                                        href=data[25],  # 链接
                                        listingAt=None if data[17] == '暂无数据' else str2timstamp(data[17]),  # 挂牌时间
                                        lastTransactionAt=None if data[19] == '暂无数据' else str2timstamp(data[19]),  # 上次交易
                                        createdAt=data[26])  # 创建时间

            try:
                HouseInfoLogRepository.insert(houseInfoLog)
            except exc.IntegrityError as e:
                self.log.logger.error("入库异常：" + repr(e))
                print("入库异常：" + repr(e))
            else:
                writer = csv.writer(f, dialect='excel')
                writer.writerow(data)

        self.log.logger.info("2.4页面数据收集：成功!")
        print("2.4页面数据收集：成功!")
