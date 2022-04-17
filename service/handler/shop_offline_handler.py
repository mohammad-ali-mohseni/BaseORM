from service.handler.abstract_handler import AbstractHandler
from model.db_model.budget import MonthBudgetDbModel
from service.command.shop_offline_command import ShopOfflineCommand


class ShopOfflineHandler(AbstractHandler):
    def handle(self, month_budget_db_model: MonthBudgetDbModel):
        ShopOfflineCommand.execute(month_budget_db_model.a_shop_id)
        super().handle(month_budget_db_model)
