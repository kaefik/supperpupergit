"""
 реализация Объектов типа Blob
"""
import os

from tools_objects import obj_sha1


class BlobObject:
    """
    Blob-объект - однозвначно определяет хеш по его содержимому и  размеру файла
    """

    def __init__(self, filename="", output_dir='.igit/blobobj/'):
        self.output_dir = output_dir
        self.filename = filename
        self.sha1 = ""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл {filename} не существует.")
        self.size = os.path.getsize(self.filename)  # размер файла

    def save(self):
        """
        сохранить blob файл в указанную папку, также если существует blob файл проверить на целостность
        :return:
        """
        with open(self.filename, 'br') as f:
            filecontent = f.read()
        # filecontent = str(self.size) + ' ' + filecontent
        # print(type(filecontent))
        self.sha1 = obj_sha1(filecontent)

        blob_dir = self.output_dir + self.sha1[:2] + '/'

        # проверка на существование корректного blob-файла
        if self.check_exist_blob():
            return self.sha1

        try:
            os.makedirs(blob_dir)
        except FileExistsError:
            # если файл существует проверяем на то что он корректный с точки зрения хеша
            self.check_exist_blob()
            return self.sha1

        bstr_size = str.encode(str(self.size)+'\n')
        # первой строкой добавляем размер файла, остальное самим файлом
        with open(blob_dir + self.sha1[2:], "bw") as f:
            f.write(bstr_size)
            f.write(filecontent)

        return self.sha1

    def check_exist_blob(self, check_dir=""):
        """
        проверка на существования такого же blob файла
        :param check_dir  - папка там где находится файл blobobject
        :return: True - если такой файл существует
        """
        if check_dir=="":
            check_dir = self.output_dir

        directory = self.sha1[:2] + '/'
        filename = self.sha1[2:]
        # print(directory+filename)
        flag_exist_file = os.path.exists(directory + filename)

        if flag_exist_file:
            with open(directory + filename, "r") as f:
                filecontent = f.read()

            sha1_file = obj_sha1(filecontent)

            if sha1_file == self.sha1:
                return True
            else:
                error_text = f"FATAL ERROR: Файл {directory + filename} существует, но содержимое скомпрометировано."
                # print(error_text)
                assert False, error_text
                return False

        return False

    def restore(self, input_directory='', output_file=''):
        """
        восстановление из файла blob object в исходный файл
        :param  input_directory - папка где лежит текущий blob object
                output_file - папка куда сохранится исходный файл
        :return:
        """
        file_dir = self.sha1[:2]+'/'
        file_name = self.sha1[2:]

        with open(input_directory+file_dir+file_name, 'br') as f:
            file_size = f.readline()
            filecontent = f.read()

        with open(output_file, 'bw') as f:
            f.write(filecontent)

        # проверка размера файла каким был изначальный файл и каким получился новый (простая проверка против компрометации данных)



def main():
    pass


if __name__ == '__main__':
    main()
