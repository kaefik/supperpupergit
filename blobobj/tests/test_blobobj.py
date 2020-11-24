import unittest
import os

from blobobj.blob_obj import BlobObject


class BlobObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Blob """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))

    def test_check_FileErrorFound(self):
        """
        BlobOblect: проверка на обработку ошибки на не существования файла
        :return:
        """
        self.assertRaises(FileNotFoundError, BlobObject, filename='11', output_dir='')

    def test_check_FileSize(self):
        """
        BlobOblect: проверка на правильное определение размера файла
        :return:
        """
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/image_670610.png', output_dir='')
        self.assertEqual(b_obj.size, 670610)

    def test_check_exist_blob_novalid(self):
        """
        BlobOblect: проверка на существование файла blob, но невалидного с точки зрения хеша
        :return:
        """
        pass

    def test_check_exist_blob_valid(self):
        """
        BlobOblect: проверка на существование файла blob, правильного с точки зрения хеша
        :return:
        """
        pass

    def test_restore_textfile(self):
        """
        проверка корректно ли восстановился текстовый файл, т.е. совпадает размер, хеш и сам вид файла
        :return:
        """
        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/text_for_blobobj.txt', output_dir=self.current_dir_test + '/test-files/out/')
        b_obj.save()
        b_obj.restore(input_directory=self.current_dir_test+'/test-files/out/', output_file=self.current_dir_test+'/test-files/out/restore_text.txt')


    def test_restore_imagefile(self):
        """
        проверка корректно ли восстановился файл изображения png, т.е. совпадает размер, хеш и сам вид файла
        :return:
        """

        b_obj = BlobObject(filename=self.current_dir_test + '/test-files/image_670610.png', output_dir=self.current_dir_test + '/test-files/out/')
        b_obj.save()
        b_obj.restore(input_directory=self.current_dir_test+'/test-files/out/', output_file=self.current_dir_test+'/test-files/out/restore_image.png')


if __name__ == '__main__':
    unittest.main()
