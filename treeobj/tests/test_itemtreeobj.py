import unittest
import os

from treeobj.tree_obj import ItemTreeObject


# class ItemTreeObjectTest(unittest.TestCase):
#     """ проверяем работоспособность объектов типа ItemTree """
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.current_dir_test = os.path.dirname(os.path.abspath(__file__)) + '/'
#
#     def test_get_all_files_and_directory_1(self):
#         """
#         проверка получения всех файлов и папок в папке  test-files/1/
#         """
#         treeObj = TreeObject(input_dir=self.current_dir_test + 'test-files/1/',
#                              output_dir=self.current_dir_test + 'test-files/out/')
#         treeObj.get_all_files_and_directory()
#
#         self.assertEqual(treeObj._files, {'file1.txt'})
#         self.assertEqual(treeObj._directory, set())


