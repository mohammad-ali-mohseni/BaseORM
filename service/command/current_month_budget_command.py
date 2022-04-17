from sqlalchemy.sql.expression import and_
from repository.budget_repositry import BudgetRepository
from model.db_model.budget import MonthBudgetDbModel
from datetime import date


class CurrentMonthBudgetCommand:

    @staticmethod
    def execute():
        return BudgetRepository().get(and_(MonthBudgetDbModel.a_month >= date.today().replace(day=1)))
