"""
 реализация Объектов типа Tree
"""
import os

# from tools_objects import obj_sha1
# from blobobj.blob_obj import BlobObject

from os.path import isfile, join


class TreeObject:
    """
    Tree-объект - могут хранить внутри себя как ссылки на blob и также ссылки на другие объекты-деревья.
    Запись состоит из одной строки вида:
            <права файла> <тип объекта(tree or blob)> <sha1 объекта> <имя файла>
    """

    def __init__(self, input_dir="./", output_dir='.igit/objects/'):
        self.input_dir = input_dir  # папка которую нужно обработать
        self.oput_dir = output_dir  # папка в которую сохранять результат дерева в виде файла
        self.treeobj = []  # все записи дерева

    def addfiles(self):
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
