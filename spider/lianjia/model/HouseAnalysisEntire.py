# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class HouseAnalysisEntire(Base):
    __tablename__ = 'house_analysis_entire'

    id = Column(INTEGER(11), primary_key=True, comment='自增id')

    houseId = Column(String(255), comment='房源id')

    delta = Column(Float, comment='总变化量 第一次与最近一次价格差值')

    status = Column(String(64), comment='状态（降价 down、涨价 up、新房 new）')

    downCount = Column(INTEGER(11), comment='降价次数')

    upCount = Column(INTEGER(11), comment='涨价次数')

    createdAt = Column(BIGINT(20), nullable=False, comment='创建时间')
