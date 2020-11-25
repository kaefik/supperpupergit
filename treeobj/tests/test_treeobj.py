import unittest
import os

from treeobj.tree_obj import TreeObject


class BlobObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Tree """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__)) + '/'

    def test_get_all_files_and_directory_1(self):
        """
        проверка получения всех файлов и папок в папке  test-files/1/
        """
        treeObj = TreeObject(input_dir=self.current_dir_test + 'test-files/1/',
                             output_dir=self.current_dir_test + 'test-files/out/')
        treeObj.get_all_files_and_directory()

        self.assertEqual(treeObj._files, {'file1.txt'})
        self.assertEqual(treeObj._directory, set())

    def test_get_all_files_and_directory_2(self):
        """
        проверка получения всех файлов и папок в папке  test-files/2/
        """
        treeObj = TreeObject(input_dir=self.current_dir_test + 'test-files/2/',
                             output_dir=self.current_dir_test + 'test-files/out/')
        treeObj.get_all_files_and_directory()

        self.assertEqual(treeObj._files, {'1.py', 'file1.txt'})
        self.assertEqual(treeObj._directory, {'papka1'})
