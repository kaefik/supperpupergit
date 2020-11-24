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
        self.size = os.path.getsize(self.filename)  # размер файла

    def save(self):
        """
        сохранить blob файл в указанную папку, также если существует blob файл проверить на целостность
        :return:
        """
        with open(self.filename, 'r') as f:
            filecontent = f.read()
        filecontent = str(self.size) + ' ' + filecontent
        self.sha1 = obj_sha1(filecontent)

        blob_dir = self.output_dir + self.sha1[:2] + '/'

        # проверка на существование корректного blob-файла
        if self.check_exist_blob():
            return self.sha1

        os.makedirs(blob_dir)

        with open(blob_dir + self.sha1[2:], "w") as f:
            f.write(filecontent)
        return self.sha1

    def check_exist_blob(self):
        """
        проверка на существования такого же blob файла
        :param sha1 -
        :return: True - если такой файл существует
        """
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


def main():
    # bobj = BlobObject("test/text_for_blobobj.txt", output_dir='')
    bobj = BlobObject("test/test-files/text_for_blobobj (copy).txt", output_dir='')
    # bobj = BlobObject("test/image.png", output_dir='')
    s = bobj.save()
    print(s)
    print(bobj.size)
    bobj.sha1 = '9b5f0e1bae22518287de10b7038ff2924fc1b1a8'
    print(bobj.check_exist_blob())


if __name__ == '__main__':
    main()
