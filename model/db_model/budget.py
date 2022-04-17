from sqlalchemy import Column, Integer, Date, DECIMAL

from model.db import Base


class MonthBudgetDbModel(Base):
    __tablename__ = 't_budgets'
    a_shop_id = Column(Integer, primary_key=True)
    a_budget_amount = Column(DECIMAL)
    a_amount_spent = Column(DECIMAL)
    a_month = Column(Date, primary_key=True)
    a_budget_percentage_notification = Column(DECIMAL)
