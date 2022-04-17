from abc import ABC, abstractmethod


class AbstractUpdateModel(ABC):
    @abstractmethod
    def update(self, model):
        raise NotImplementedError
