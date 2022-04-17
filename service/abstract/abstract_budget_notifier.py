from abc import ABC, abstractmethod
from model.db_model.budget import MonthBudgetDbModel


class AbstractBudgetNotifier(ABC):
    @abstractmethod
    def notify(self, month_budget_db_model: MonthBudgetDbModel):
        raise NotImplementedError
