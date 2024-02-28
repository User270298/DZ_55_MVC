
from view import  ConsoleView
from model import Model

def inp(txt):
    return input(txt)


def main():
    x = inp('Введите 1 если хотите добавить обувь\n'
            'Введите 2 если хотите посмотреть обувь\n'
            'Введите 3 если хотите изменить какую то позицию\n'
            'Введите 4 если хотите удалить позицию\n'
            'Введите 0 если хотите выйти из меню\n')
    model = Model()
    view = ConsoleView()

    while True:
        if x == '0':
            break
        elif x == '1':
            model.add_shoes(view.input_shoes())
        elif x == '2':
            print(model.search_shoes(input('Input name search shoes: ')))
        elif x == '3':
            model.refactor_shoes(input('Input name refactor shoes: '), view.input_shoes())
        elif x == '4':
            model.delete_shoes(input('Input delete shoes: '))

        x = inp('Введите 1 если хотите добавить обувь\n'
                'Введите 2 если хотите посмотреть обувь\n'
                'Введите 3 если хотите изменить какую то позицию\n'
                'Введите 4 если хотите удалить позицию\n'
                'Введите 0 если хотите выйти из меню')


if __name__ == '__main__':
    main()


