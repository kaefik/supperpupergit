"""
 реализация Объектов типа Tree
"""
import os

from tools_objects import obj_sha1, get_file_dirs
# from blobobj.blob_obj import BlobObject


from os.path import isfile, join

# тип объекта
NOOBJ = 0  # нет объекта
BLOB = 1  # объект Blob
TREE = 2  # объект Tree


class ItemTreeObject:
    """
        элемент объекта Tree (одна запись), в TreeObject таких записей может быть несколько.
        содержит следующие данные:
            * <права файла>
            * <тип объекта(tree or blob)>
            * <sha1 объекта>
            * <имя файла>
    """

    def __init__(self):
        # (self, right_access='', typeobj=NOOBJ, sha1='', nameobj=''):
        self.right_access = '000000'  # <права файла>
        self.typeobj = NOOBJ  # <тип объекта(tree or blob)>
        self.sha1 = '0000000000000000000000000000000000000000'  # <sha1 объекта>
        self.name = ''  # <имя файла или папки>

    def generate_blobs(self):
        """
        получение данных
        """
        if isfile(join(self.name, f)):
            pass



class TreeObject:
    """
    Tree-объект - могут хранить внутри себя как ссылки на blob и также ссылки на другие объекты-деревья.
    Запись состоит из одной строки вида:
            <права файла> <тип объекта(tree or blob)> <sha1 объекта> <имя файла>
    """

    def __init__(self, input_dir='./', output_dir='.igit/objects/'):
        self.input_dir = input_dir  # папка которую нужно обработать
        self.output_dir = output_dir  # папка в которую сохранять результат дерева в виде файла
        self.obj = set()  # все записи дерева
        self.parent_tree = None  # Tree родитель
        self._files = set()  # все найденные файлы в папке self.input_dir
        self._directory = set()  # все найденные папки в папке self.input_dir

    def get_all_files_and_directory(self):
        """
        поиск всех файлов и папок в self.input_dir
        :return:
        """
        self._files, self._directory = get_file_dirs(self.input_dir)


    def generate(self):
        """
        генерация содержимого дерева
        """
        pass

    def save(self, filename=''):
        """
        сохранение тектового представления дерева в файл filename
        """
        pass


def main():
    pass


if __name__ == '__main__':
    main()
