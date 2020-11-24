"""
 реализация Объектов типа Tree
"""
import os

# from tools_objects import obj_sha1


class TreeObject:
    """
    Tree-объект - могут хранить внутри себя как ссылки на blob и также ссылки на другие объекты-деревья.
    Запись состоит из одной строки вида:
            <права файла> <тип объекта(tree or blob)> <sha1 объекта> <имя файла>
    """

    def __init__(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()