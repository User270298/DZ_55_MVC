from abc import ABC, abstractmethod
from typing import List
from core import Shoes

class IModel(ABC):
    @abstractmethod
    def add_shoes(self, shoes: Shoes):
        pass

    @abstractmethod
    def search_shoes(self, name):
        pass

    @abstractmethod
    def refactor_shoes(self, name, shoes_ref: Shoes) -> Shoes:
        pass

    @abstractmethod
    def delete_shoes(self, name):
        pass



class Model(IModel):
    def __init__(self):
        self.db=[]
    def add_shoes(self, shoes: Shoes):
        return self.db.append(shoes)

    def search_shoes(self, name):
        if not self.db:
            return f'There are no such shoes'
        for i in self.db:
            shoes = i
            for j in shoes:
                if name == j:
                    return shoes
        return f'There are no such shoes'
    def refactor_shoes(self, name, shoes_ref: Shoes) :
        for i in self.db:
            shoes=i
            print(shoes)
            for j in shoes:
                print(j)
                if name==j:
                    self.db.append(shoes_ref)
                    self.db.remove(i)
                    return
        return f'There are no such shoes'

    def delete_shoes(self, name):
        for i in self.db:
            shoes = i
            print(shoes)
            for j in shoes:
                if name == j:
                    self.db.remove(i)
                    return
        return f'There are no such shoes'





