"""
 реализация Объектов типа Tree
"""
import os

from tools_objects import obj_sha1, get_file_dirs
from blobobj.blob_obj import BlobObject

from os.path import isfile, join

# тип объекта
NOOBJ = None  # нет объекта
BLOB = 'blob'  # объект Blob
TREE = 'tree'  # объект Tree


class ItemTreeObject:
    """
        элемент объекта Tree (одна запись), в TreeObject таких записей может быть несколько.
        содержит следующие данные:
            * <права файла>
            * <тип объекта(tree or blob)>
            * <sha1 объекта>
            * <имя файла>
    """

    def __init__(self, input_name=''):
        self.obj = None  # ссылка на объект
        self.input_name = input_name
        self.right_access = '000000'  # <права файла>
        self.typeobj = NOOBJ  # <тип объекта(tree or blob)>
        self.sha1 = '0000000000000000000000000000000000000000'  # <sha1 объекта>
        self.name = ''  # <имя файла или папки>

    def save(self, output_dir='./'):
        """
        получение данных
        """
        result = ''
        if isfile(join(self.name, self.input_name)):
            self.obj = BlobObject(filename=self.input_name, output_dir=output_dir)
            self.sha1 = self.obj.save()
            self.typeobj = BLOB
            self.name = os.path.basename(self.input_name)
            self.right_access = '000000'
        else:
            # TODO: вставить создание объекта TreeObject
            self.obj = TreeObject(input_dir=self.input_name, output_dir=output_dir)
            self.typeobj = TREE
            self.right_access = '000000'
            self.sha1 = self.obj.save()
            self.name = os.path.basename(self.input_name)

    def get(self):
        """
        получение строки для сохранения результата
        """
        result = f'{self.right_access} {self.typeobj} {self.sha1} {self.name}'
        # result = {'access': self.right_access, 'type': self.typeobj, 'sha1': self.sha1, 'name': self.name}
        return result


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
        self.sha1 = None  # '0000000000000000000000000000000000000000'

    def print(self):
        for item in self.obj:
            print(item)

    def get_all_files_and_directory(self):
        """
        поиск всех файлов и папок в self.input_dir
        :return:
        """
        self._files, self._directory = get_file_dirs(self.input_dir)

    def get_sha1(self):
        """
        получение sha1 по содержимому obj
        """
        sort_obj = sorted(self.obj)
        res = '\n'.join(str(e) for e in sort_obj)
        return obj_sha1(res.encode())

    def generate(self):
        """
        генерация содержимого дерева
        return: False - значит папка пустая, т.е. нет ни папок ни файлов
        """
        self.obj = set()
        self.get_all_files_and_directory()

        if self._files == set() and self._directory == set():
            self.sha1 = None
            self.obj = set()
            return False

        # создание объектов типа blob
        for item in self._files:
            item_obj = ItemTreeObject(input_name=self.input_dir + '/' + item)
            item_obj.save(self.output_dir)
            res = item_obj.get()
            self.obj.add(res)

        # создание объектов типа tree
        for item in self._directory:
            item_obj = ItemTreeObject(input_name=self.input_dir + '/' + item)
            item_obj.save(self.output_dir)
            # if sha1 is None:
            #     return False
            res = item_obj.get()
            self.obj.add(res)
        return True

    def check_exist_blob(self, check_dir=""):
        """
        проверка на существования такого же tree файла
        :param check_dir  - папка там где находится файл blobobject
        :return: True - если такой файл существует
        """
        if check_dir == "":
            check_dir = self.output_dir

        directory = self.sha1[:2] + '/'
        filename = self.sha1[2:]
        full_filename = check_dir + directory + filename
        flag_exist_file = os.path.exists(full_filename)

        if flag_exist_file:
            with open(full_filename, "br") as f:
                filecontent = f.read()

            sha1_file = obj_sha1(filecontent)
            if sha1_file != self.sha1:
                error_text = f"FATAL ERROR: Файл {directory + filename} существует, но содержимое скомпрометировано."
                # print(error_text)
                raise BaseException(error_text)
        else:
            return False

        return True

    def save(self):
        """
        сохранение тектового представления дерева в файл filename
        return: sha1 объекта
        """
        # если нет объектов, то нечего сохранять
        # генерация перед сохранением данных
        flag_empty_dir = self.generate()

        if not flag_empty_dir:
            return None

        sort_obj = sorted(self.obj, reverse=True)
        filecontent = '\n'.join(str(e) for e in sort_obj)

        self.sha1 = obj_sha1(filecontent.encode())

        if self.sha1 is None:
            return None

        tree_dir = self.output_dir + self.sha1[:2] + '/'
        # проверка на существование корректного tree-файла
        if self.check_exist_blob():
            return self.sha1

        try:
            os.makedirs(tree_dir)
        except FileExistsError:
            # если файл существует проверяем на то что он корректный с точки зрения хеша
            flag = self.check_exist_blob()
            if flag:
                return self.sha1

        # первой строкой добавляем размер файла, остальное самим файлом
        with open(tree_dir + self.sha1[2:], "tw") as f:
            f.write(filecontent)
        return self.sha1


def main():
    pass


if __name__ == '__main__':
    main()
