import unittest
import os
import shutil

from blobobj.blob_obj import BlobObject
from tools_objects import get_file_dirs


class BlobObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Blob """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = ''
        cls.output_dir = cls.current_dir_test + '/test-files/out/'

    def setUp(self) -> None:
        # создаем папку для файлов которые создаются для тестов
        os.mkdir(self.output_dir)

    def tearDown(self) -> None:
        # удаляем папку для файлов которые создаются для тестов
        shutil.rmtree(self.output_dir, ignore_errors=False, onerror=None)

    def test_check_FileErrorFound(self):
        """
        BlobOblect: проверка на обработку ошибки на не существования файла
        :return:
        """
        bobj = BlobObject(filename='11', output_dir='')
        self.assertRaises(FileNotFoundError, bobj.save)

    def test_check_FileSize(self):
        """
        BlobOblect: проверка на правильное определение размера файла
        :return:
        """
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/image_670610.png', output_dir='')
        self.assertEqual(b_obj.size, 670610)

    def test_restore_textfile(self):
        """
        BlobOblect: проверка корректно ли восстановился текстовый файл, т.е. совпадает размер, хеш и сам вид файла
        :return:
        """
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/text_for_blobobj.txt',
                           output_dir=self.output_dir)
        b_obj.save()
        b_obj.restore(input_directory=self.output_dir,
                      output_file=self.output_dir + 'restore_text.txt')
        size_restore = os.path.getsize(self.output_dir + 'restore_text.txt')
        self.assertEqual(b_obj.size, size_restore)

    def test_restore_imagefile(self):
        """
        BlobOblect: проверка корректно ли восстановился файл изображения png, т.е. совпадает размер, хеш и сам вид файла
        :return:
        """

        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/image_670610.png',
                           output_dir=self.output_dir)
        b_obj.save()
        b_obj.restore(input_directory=self.output_dir,
                      output_file=self.output_dir + 'restore_image.png')
        size_restore = os.path.getsize(self.output_dir + 'restore_image.png')
        self.assertEqual(b_obj.size, size_restore)

    def test_check_valid_blobobj_file(self):
        """
        BlobOblect: проверка соответствия хеша содержимому файла который корректный
        :return:
        """
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/text_for_blobobj.txt',
                           output_dir=self.output_dir)
        b_obj.sha1 = 'c79c497f5012c3065de47887d819ecca426ac697'
        res = b_obj.check_exist_blob(check_dir=self.current_dir_test + '/test-files/out-etalon/valid-blobobj/')
        self.assertEqual(res, True)

    def test_check_novalid_blobobj_file(self):
        """
        BlobOblect: проверка соответствия хеша содержимому файла который НЕ корректный
        :return:
        """
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/text_for_blobobj.txt',
                           output_dir=self.output_dir)
        b_obj.sha1 = 'c79c497f5012c3065de47887d819ecca426ac697'
        self.assertRaises(BaseException, b_obj.check_exist_blob,
                          check_dir=self.current_dir_test + '/test-files/out-etalon/novalid-blobobj/')

    def test_check_dublicate_name_directory_blobobj(self):
        """
        BlobOblect: проверка того что если есть папка blobobj, но файлы с другими blob-файлами
        """

        # создание папки в которой будет проверяться
        shutil.copytree(self.current_dir_test + '/test-files/out-etalon/dublicate-folder/c7/',
                        self.output_dir + 'c7/')
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/text_for_blobobj.txt',
                           output_dir=self.output_dir)
        sha1 = b_obj.save()
        f, d = get_file_dirs(self.output_dir + 'c7/')
        self.assertEqual(f, {'9c497f5012c3065de47887d819ecca426ac696', '9c497f5012c3065de47887d819ecca426ac697'})


if __name__ == '__main__':
    unittest.main()
