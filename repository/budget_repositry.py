from repository.base_repository import BaseRepository
from repository.abstract.abstract_get_model import AbstractGetModel
from model.db_model.budget import MonthBudgetDbModel
from model.db import Session


class BudgetRepository(BaseRepository, AbstractGetModel):
    def __init__(self, session=None):
        if session is None:
            self.session = Session()
        else:
            self.session = session
        BaseRepository.__init__(self.session)

    def get(self, model_filter=()):
        return self.session.query(MonthBudgetDbModel).filter(model_filter).all()

    def update(self, model_filter=(), new_values={}):
        self.session.query(MonthBudgetDbModel).filter(model_filter).update(new_values)
        self.session.commit()
