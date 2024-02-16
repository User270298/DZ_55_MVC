from abc import ABC, abstractmethod
from typing import List
from core import Shoes
from pprint import pprint
from presenter import Presenter


class DataBase:
    def __init__(self):
        self.db: List[Shoes] = []

    def search_database(self):
        return self.db


class IModel(ABC):
    @abstractmethod
    def add_shoes(self, shoes: Shoes):
        pass

    @abstractmethod
    def search_shoes(self):
        pass

    @abstractmethod
    def refactor_shoes(self, shoes: Shoes) -> Shoes:
        pass

    @abstractmethod
    def delete_shoes(self, shoes: Shoes):
        pass


class Model(IModel):
    def __init__(self):
        self.database = DataBase()

    def add_shoes(self, shoes: Shoes):
        self.database.db.append(shoes)

    def search_shoes(self):
        # if shoes in self.database.db:
        #     return shoes
        # return None
        return self.database.db
    def refactor_shoes(self, shoes: Shoes) :
        pass
#
#
    def delete_shoes(self, shoes: Shoes):
        for i in range(len(self.database.db)-1):
            if self.database.db[i] == shoes:
                del self.database.db[i]




# model=Model()
# shoes_1=Shoes('man', 'cross', 'blue', '15$', 'USA', '45')
# shoes_2=Shoes('woman', 'sandals', 'red', '0,5$', 'USSR', '46')
# model.add_shoes(shoes_1)
# model.add_shoes(shoes_2)
# # pprint(model.database.db)
# # pprint(model.search_shoes(shoes_1))
# print(model.delete_shoes(shoes_1))
# print(model.database.db)

