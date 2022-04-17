from repository.abstract.abstract_update_model import AbstractUpdateModel
from repository.abstract.abstract_get_model import AbstractGetModel
from repository.base_repository import BaseRepository
from model.db_model.shop import ShopDbModel
from model.db import Session


class ShopRepository(BaseRepository, AbstractUpdateModel, AbstractGetModel):
    def __init__(self, session=None):
        if session is None:
            self.session = Session()
        else:
            self.session = session
        BaseRepository.__init__(self.session)

    def update(self, model_filter=(), new_values={}):
        self.session.query(ShopDbModel).filter(model_filter).update(new_values)
        self.session.commit()

    def get(self, model_filter=()):
        return self.session.query(ShopDbModel).filter_by(model_filter)
