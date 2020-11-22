"""
основной модуль с которого всё начинается.
моя реализация супер-пупер git
"""
import os
from sys import argv


def create_empty_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        pass


def cmd_init(arg):
    """
    функция инициализации репозитория
    :param arg: аргументы команды init
    :return: True - если операция завершилась без ошибок
    """
    igit_dir = '.igit/'
    repo_files = ['config', 'description', 'HEAD']
    repo_dirs = ['branches', 'hooks', 'info', 'objects/info', 'objects/pack', 'refs/heads', 'refs/tags']
    for name in repo_dirs:
        os.makedirs(igit_dir + name)
    for name in repo_files:
        create_empty_file(igit_dir + name)
    print('Инициализация репозитория завершена.')
    return True


def cmd_add(arg):
    """
    функция добавления файлов в индекс
    :param arg: аргументы команды init
    :return:
    """
    pass


def cmd_commit(arg):
    """
    функция добавления объектов в репозиторий
    :param arg: аргументы команды init
    :return:
    """
    pass


def cmd_help(cmd):
    """
    вывод помощи по командам
    :param filename:
    :return:
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория скрипта
    filename_help = current_dir + '/help-igit.txt'
    with open(filename_help, 'r') as f:
        str_help = f.read()
    print(str_help)


def main():
    """
    основная программа
    :return: если программа закончит работу без ошибок вернет 0, иначе ошибку.
    """
    print(argv)

    if len(argv) == 1:
        print('Команда не указана')
        exit(0)

    cmd = argv[1]

    if cmd == 'init':
        print('Инициализация репозитория')
        cmd_init(argv[2:])
        exit(0)

    if cmd == 'add':
        print('добавление файлов в индекс')
        cmd_add(argv[2:])
        exit(0)

    if cmd == 'commit':
        print('добавление файлов из индекса в репозиторий')
        cmd_commit(argv[2:])
        exit(0)

    if cmd == 'help':
        cmd_help("")
        exit(0)

    print('Нет такой команды')


if __name__ == '__main__':
    main()
