from abc import ABC, abstractmethod
from core import Shoes
from view import IView, ConsoleView
from model import IModel


class IPresenter(ABC):
    @abstractmethod
    def check_user(self):
        pass


class Presenter(IPresenter):
    def __init__(self, view: ConsoleView, model: IModel):
        self.__view: IView = view
        self.__model = model

    def check_user(self):
        shoes: Shoes = self.__view.input_shoes()
        self.__model=shoes
