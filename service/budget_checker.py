from repository.budget_repositry import BudgetRepository
from service.handler.shop_notify_handler import ShopNotifyHandler
from service.handler.shop_offline_handler import ShopOfflineHandler
from service.handler.budget_notify_recorder_handler import BudgetNotifyRecorderHandler


class BudgetChecker:

    def __init__(self):
        self.shop_notify_handler = ShopNotifyHandler()
        self.shop_offline_handler = ShopOfflineHandler()
        self.shop_notify_handler.set_next(self.shop_offline_handler).set_next(None)

    def check(self, budget_month_list):
        for budget_month in budget_month_list:
            self.shop_notify_handler.handle(budget_month)
