from view import IView, ConsoleView
from model import IModel, Model
from presenter import IPresenter, Presenter



def main():

    model: IModel = Model()
    view: IView = ConsoleView()
    presenter: IPresenter = Presenter(view=view, model=model)
    print(presenter)

if __name__ == '__main__':
    main()
