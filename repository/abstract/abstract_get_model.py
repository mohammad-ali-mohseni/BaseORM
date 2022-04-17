from abc import ABC, abstractmethod


class AbstractGetModel(ABC):
    @abstractmethod
    def get(self, params={}):
        raise NotImplementedError
