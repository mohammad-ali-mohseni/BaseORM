from service.abstract.abstract_budget_notifier import AbstractBudgetNotifier
from model.db_model.budget import MonthBudgetDbModel
from datetime import date


class StdoutBudgetNotifier(AbstractBudgetNotifier):
    def notify(self, month_budget_db_model: MonthBudgetDbModel):
        print("current date: {} , shop ID: {} , current month budget:{}, expenditure:{}, budget percentage:{}".format(
            date.today(), month_budget_db_model.a_shop_id, month_budget_db_model.a_month,
            month_budget_db_model.a_amount_spent,
            round((100 * month_budget_db_model.a_amount_spent / month_budget_db_model.a_budget_amount), 2)))
