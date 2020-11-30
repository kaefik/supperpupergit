import unittest
import os
import shutil
from tools_objects import create_new_dir, get_file_dirs

from treeobj.tree_obj import TreeObject, restore_from_obj, get_from_text


class RestoreObjectTest(unittest.TestCase):
    """ проверяем работоспособность восстановления из объектов в папки """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = cls.current_dir_test + '/test-files/'
        cls.output_dir = cls.current_dir_test + '/test-files/out/'

    def test_get_from_text(self):
        """
        проверка разбиения строки в файле TreeObj
        """
        ex_line = '001000 blob dd69304ab57e87704fd8d8f57827c72124e40016 файл 1.py'
        result = get_from_text(ex_line)
        # print(result)
        self.assertEqual(result[0] == '001000', True)
        self.assertEqual(result[1] == 'blob', True)
        self.assertEqual(result[2] == 'dd69304ab57e87704fd8d8f57827c72124e40016', True)
        self.assertEqual(result[3] == 'файл 1.py', True)

    # def setUp(self) -> None:
    #     # создаем папку для файлов которые создаются для тестов
    #     create_new_dir(self.output_dir)

    # def tearDown(self) -> None:
    #     # удаляем папку для файлов которые создаются для тестов
    #     shutil.rmtree(self.output_dir, ignore_errors=False, onerror=None)

    def test_restore_directory(self):
        """
        проверка восстановление дерева папок и файлов из объектов out-etalon/2/
        """
        input_dir = self.input_dir + 'out-etalon/2/'
        output_dir = self.output_dir + 'restore/'
        etalon_dir = self.input_dir + '2/'
        create_new_dir(output_dir)
        restore_from_obj(input_dir=input_dir, file_treeobj='f8/378c9d4b73baf88a4074f3d4b45fb0bc68c52c',
                         output_dir=output_dir)
        files_etalon, directory_etalon = get_file_dirs(etalon_dir)
        files, directory = get_file_dirs(output_dir)
        files_papka1, directory_papka1 = get_file_dirs(output_dir + '/papka1')
        self.assertEqual((files == files_etalon), True)
        self.assertEqual((directory == directory_etalon), True)
        self.assertEqual((files_papka1 == {'file1.txt'}), True)
        self.assertEqual((directory_papka1 == set()), True)
