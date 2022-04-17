from model.db_model.budget import MonthBudgetDbModel
from repository.budget_repositry import BudgetRepository
from sqlalchemy.sql.expression import and_


class BudgetNotifyRecorderCommand:

    @staticmethod
    def execute(budget_month_model: MonthBudgetDbModel):
        budget_percentage_usage = 100 * budget_month_model.a_amount_spent / budget_month_model.a_budget_amount

        if budget_percentage_usage >= 50 and budget_month_model.a_budget_percentage_notification == 0:
            BudgetRepository().update(and_(MonthBudgetDbModel.a_shop_id == budget_month_model.a_shop_id,
                                           MonthBudgetDbModel.a_month == budget_month_model.a_month),
                                      {"a_budget_percentage_notification": budget_percentage_usage})

        if budget_percentage_usage >= 100 and budget_month_model.a_budget_percentage_notification < 100:
            BudgetRepository().update(and_(MonthBudgetDbModel.a_shop_id == budget_month_model.a_shop_id,
                                           MonthBudgetDbModel.a_month == budget_month_model.a_month),
                                      {"a_budget_percentage_notification": budget_percentage_usage})
