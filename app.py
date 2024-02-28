from presenter import Present
from view import ConsoleView


def inp(txt):
    return input(txt)


def main():
    x = inp('Введите 1 если хотите добавить обувь\n'
            'Введите 2 если хотите посмотреть обувь\n'
            'Введите 3 если хотите изменить какую то позицию\n'
            'Введите 4 если хотите удалить позицию\n'
            'Введите 0 если хотите выйти из меню')
    presenter = Present()
    shoes = ConsoleView()
    while True:
        if x == '1':
            presenter.add(shoes.input_shoes())
        elif x == '2':
            presenter.search()
        elif x == '3':
            presenter.refactor(shoes.input_shoes(), shoes.input_shoes())
        elif x == '4':
            presenter.delete(shoes.input_shoes())
        elif x == '0':
            break
        x = inp('Введите 1 если хотите добавить обувь\n'
                'Введите 2 если хотите посмотреть обувь\n'
                'Введите 3 если хотите изменить какую то позицию\n'
                'Введите 4 если хотите удалить позицию\n'
                'Введите 0 если хотите выйти из меню')


if __name__ == '__main__':
    main()
