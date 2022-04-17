from model.db_model.shop import ShopDbModel
from repository.shop_repository import ShopRepository
from sqlalchemy.sql.expression import and_


class ShopOfflineCommand:

    @staticmethod
    def execute(shop_id):
        ShopRepository().update(and_(ShopDbModel.a_id == shop_id), {"a_online": 0})
