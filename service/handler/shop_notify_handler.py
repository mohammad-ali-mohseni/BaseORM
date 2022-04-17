from service.handler.abstract_handler import AbstractHandler
from model.db_model.budget import MonthBudgetDbModel
from service.notifier.stdout_budget_notifier import StdoutBudgetNotifier
from service.command.budget_notify_recorder_command import BudgetNotifyRecorderCommand


class ShopNotifyHandler(AbstractHandler):
    def handle(self, month_budget_db_model: MonthBudgetDbModel):
        budget_percentage_usage = 100 * month_budget_db_model.a_amount_spent / month_budget_db_model.a_budget_amount

        if budget_percentage_usage >= 50 and month_budget_db_model.a_budget_percentage_notification == 0 or \
                budget_percentage_usage >= 100 and month_budget_db_model.a_budget_percentage_notification < 100:
            StdoutBudgetNotifier().notify(month_budget_db_model)
            BudgetNotifyRecorderCommand.execute(month_budget_db_model)
            super().handle(month_budget_db_model)
