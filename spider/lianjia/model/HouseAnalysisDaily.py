# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class HouseAnalysisDaily(Base):
    __tablename__ = 'house_analysis_daily'

    id = Column(INTEGER(11), primary_key=True, comment='自增id')

    houseId = Column(String(255), comment='房源id')

    delta = Column(Float, comment='较上一次变化量')

    status = Column(String(64), comment='状态（降价 down、涨价 up、新房 new）')

    createdAt = Column(BIGINT(20), nullable=False, comment='创建时间')
