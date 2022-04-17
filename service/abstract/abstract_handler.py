from handler import Handler
from abc import abstractmethod


class AbstractHandler(Handler):
    next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, budget_month_model):
        if self.next_handler:
            return self.next_handler.handle(budget_month_model)

        return None
