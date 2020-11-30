"""
 реализация Объектов типа Blob
"""
import os

from tools_objects import obj_sha1


class BlobObject:
    """
    Blob-объект - однозвначно определяет хеш по его содержимому и  размеру файла
    """

    def __init__(self, filename="", output_dir='.igit/objects/'):
        self.output_dir = output_dir
        self.filename = filename
        self.sha1 = ""
        if not os.path.exists(self.filename):
            self.size = 0
        else:
            self.size = os.path.getsize(self.filename)  # размер файла

    def save(self):
        """
        сохранить blob файл в указанную папку, также если существует blob файл проверить на целостность
        :return:
        """
        if not os.path.exists(self.filename):
            str_err = f'Файл {self.filename} не существует.'
            raise FileNotFoundError(str_err)

        self.size = os.path.getsize(self.filename)

        bstr_size = str.encode(str(self.size) + '\n')

        with open(self.filename, 'br') as f:
            filecontent = f.read()

        filecontent = bstr_size + filecontent
        self.sha1 = obj_sha1(filecontent)
        blob_dir = self.output_dir + self.sha1[:2] + '/'

        # проверка на существование корректного blob-файла
        if self.check_exist_blob():
            return self.sha1

        try:
            os.makedirs(blob_dir)
        except FileExistsError:
            # если файл существует проверяем на то что он корректный с точки зрения хеша
            flag = self.check_exist_blob()
            if flag:
                return self.sha1

        # первой строкой добавляем размер файла, остальное самим файлом
        with open(blob_dir + self.sha1[2:], "bw") as f:
            f.write(filecontent)
        return self.sha1

    def check_exist_blob(self, check_dir=""):
        """
        проверка на существования такого же blob файла
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

    def restore(self, input_directory='', output_file=''):
        """
        восстановление из файла blob object в исходный файл
        :param  input_directory - папка где лежит текущий blob object
                output_file - папка куда сохранится исходный файл
        :return:
        """
        file_dir = self.sha1[:2] + '/'
        file_name = self.sha1[2:]

        with open(input_directory + file_dir + file_name, 'br') as f:
            file_size = f.readline()
            filecontent = f.read()

        with open(output_file, 'bw') as f:
            f.write(filecontent)

        # проверка размера файла каким был изначальный файл и каким получился новый (простая проверка против компрометации данных)


def main():
    pass


if __name__ == '__main__':
    main()
