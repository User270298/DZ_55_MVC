from abc import ABC, abstractmethod
from core import Shoes


class IView(ABC):
    @abstractmethod
    def input_shoes(self) -> Shoes:
        pass


class ConsoleView(IView):
    def input_shoes(self) -> Shoes:
        return Shoes(gender=input("Input gender\n"), view=input("Input view\n"),
                     color=input("Input color\n"), price=input("Input price\n"),
                     munufactur=input("Input munufactur\n"), size=input("Input size\n"))
        # return Shoes(gender=("one"), view=("two"),
        #              color=("three"), price=("four"),
        #              munufactur=("five"), size=("six"))
