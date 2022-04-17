from sqlalchemy import Column, String, Integer, Date

from model.db import Base


class ShopDbModel(Base):
    __tablename__ = "t_shops"
    a_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    a_name = Column(String(length=50), nullable=False)
    a_online = Column(Integer)
