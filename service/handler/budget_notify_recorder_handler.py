from service.handler.abstract_handler import AbstractHandler
from model.db_model.budget import MonthBudgetDbModel
from service.command.budget_notify_recorder_command import BudgetNotifyRecorderCommand


class BudgetNotifyRecorderHandler(AbstractHandler):
    def handle(self, month_budget_db_model: MonthBudgetDbModel):
        BudgetNotifyRecorderCommand.execute(month_budget_db_model)
        super().handle(month_budget_db_model)
