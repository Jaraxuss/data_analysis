# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class HouseInfoLog(Base):
    __tablename__ = 'house_info_log'

    id = Column(INTEGER(11), primary_key=True, comment='自增id')
    houseId = Column(String(255), comment='房源id')
    communityName = Column(String(255), comment='小区名称')
    region = Column(String(255), comment='所在区域')
    totalPrice = Column(Float, comment='总价（万元）')
    unitPrice = Column(Float, comment='单价（元/平米）')
    buildingArea = Column(Float, comment='建筑面积')
    innerArea = Column(Float, comment='套内面积')
    houseType = Column(String(255), comment='房屋户型')
    orientation = Column(String(255), comment='房屋朝向')
    floor = Column(String(255), comment='所在楼层')
    houseStructure = Column(String(255), comment='户型结构')
    renovationCondition = Column(String(255), comment='装修情况')
    ladderHouseholdProportion = Column(String(255), comment='梯户比例')
    hasElevator = Column(String(255), comment='配备电梯')
    buildingType = Column(String(255), comment='建筑类型')
    buildingStructure = Column(String(255), comment='建筑结构')
    yearOfPropertyRights = Column(String(255), comment='产权年限')
    tradingAuthority = Column(String(255), comment='交易权属')
    housingPurposes = Column(String(255), comment='房屋用途')
    yearOfHousing = Column(String(255), comment='房屋年限')
    propertyRights = Column(String(255), comment='产权所属')
    mortgageInfo = Column(String(255), comment='抵押信息')
    premisesPermitInfo = Column(String(255), comment='房本备件')
    href = Column(String(255), comment='链接')
    listingAt = Column(BIGINT(20), comment='挂牌时间')
    lastTransactionAt = Column(BIGINT(20), comment='上次交易')
    createdAt = Column(BIGINT(20), nullable=False, comment='创建时间')
