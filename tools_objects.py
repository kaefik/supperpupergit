"""
инструменты для работы с Объектами - это файл специального формата.
у каждого Объекта имя записывается как 16-ричное представление этого хеша. длина хэша равна 20 байт.
Первые два символа имеет объект и создает подиректорию с этим именем.
"""
import os
import hashlib


def obj_sha1(bstr):
    """
    функция хеширования на SHA1
    :param input_string: строка которую нужно хешировать
    :return: вовращает 16-ричный хеш
    """
    # bstr = str.encode(input_string)
    hash_object = hashlib.sha1(bstr)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def get_file_dirs(input_dir):
    """
    получить все файлы и папки в указанной папке input_dir
    """
    files = set()
    directory = set()
    for f in os.listdir(input_dir):
        if os.path.isfile(os.path.join(input_dir, f)):
            files.add(f)
        else:
            directory.add(f)
    return files, directory


def main():
    # f, d = get_file_dirs('/home/oilnur/prj/prj-py/supperpupergit')
    # print(d)


if __name__ == '__main__':
    main()
