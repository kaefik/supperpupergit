"""
 реализация Объектов типа Tree
"""
import os

# from tools_objects import obj_sha1
# from blobobj.blob_obj import BlobObject

from os.path import isfile, join

# тип объекта
NOOBJ = 0  # нет объекта
BLOB = 1   # объект Blob
TREE = 2   # объект Tree


class ItemTreeObject:
    """
        элемент объекта Tree (одна запись), в TreeObject таких записей может быть несколько.
        содержит следующие данные:
            * <права файла>
            * <тип объекта(tree or blob)>
            * <sha1 объекта>
            * <имя файла>
    """

    def __init__(self, right_access='', typeobj=NOOBJ, sha1='', filename=''):
        self.right_access = right_access  # <права файла>
        self.typeobj = typeobj            # <тип объекта(tree or blob)>
        self.sha1 = sha1                  # <sha1 объекта>
        self.filename = filename          # <имя файла>


class TreeObject:
    """
    Tree-объект - могут хранить внутри себя как ссылки на blob и также ссылки на другие объекты-деревья.
    Запись состоит из одной строки вида:
            <права файла> <тип объекта(tree or blob)> <sha1 объекта> <имя файла>
    """

    parent_tree = None  # Tree родитель

    def __init__(self, input_dir="./", output_dir='.igit/objects/'):
        self.input_dir = input_dir  # папка которую нужно обработать
        self.oput_dir = output_dir  # папка в которую сохранять результат дерева в виде файла
        self.treeobj = []  # все записи дерева

    def findallfiles(self):
        """
        добавление всех файлов в дерево
        :return:
        """
        # найти все файлы в папке
        files = [f for f in os.listdir(self.input_dir) if isfile(join(self.input_dir, f))]
        for ff in files:
            print(ff)


def main():
    tobj = TreeObject()
    tobj.addfiles()


if __name__ == '__main__':
    main()
