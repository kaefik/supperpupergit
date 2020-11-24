"""
инструменты для работы с Объектами - это файл специального формата.
у каждого Объекта имя записывается как 16-ричное представление этого хеша. длина хэша равна 20 байт.
Первые два символа имеет объект и создает подиректорию с этим именем.
"""
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


def main():
    hh = obj_sha1('Privet как дела?')
    print(type(hh))

if __name__ == '__main__':
    main()
