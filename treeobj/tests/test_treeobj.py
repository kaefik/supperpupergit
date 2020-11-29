import unittest
import os
import shutil

from treeobj.tree_obj import TreeObject


class TreeObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Tree """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = cls.current_dir_test + '/test-files/'
        cls.output_dir = cls.current_dir_test + '/test-files/out/'

    def setUp(self) -> None:
        # создаем папку для файлов которые создаются для тестов
        try:
            os.mkdir(self.output_dir)
        except FileExistsError:
            shutil.rmtree(self.output_dir, ignore_errors=False, onerror=None)
            os.mkdir(self.output_dir)

    def tearDown(self) -> None:
        # удаляем папку для файлов которые создаются для тестов
        shutil.rmtree(self.output_dir, ignore_errors=False, onerror=None)

    def test_get_all_files_and_directory_1(self):
        """
        проверка получения всех файлов и папок в папке  test-files/1/
        """
        treeObj = TreeObject(input_dir=self.input_dir + '1/',
                             output_dir=self.output_dir)
        treeObj.get_all_files_and_directory()

        self.assertEqual(treeObj._files, {'text_for_blobobj.txt'})
        self.assertEqual(treeObj._directory, set())

    def test_get_all_files_and_directory_2(self):
        """
        проверка получения всех файлов и папок в папке  test-files/2/
        """
        treeObj = TreeObject(input_dir=self.input_dir + '2/', output_dir=self.output_dir)
        treeObj.get_all_files_and_directory()

        self.assertEqual(treeObj._files, {'1.py', 'file1.txt'})
        self.assertEqual(treeObj._directory, {'papka1'})

    def test_generate_blobobject_1(self):
        """
        проверка сохранения blobobj из папки  test-files/1/
        """
        etalon_set = {'000000 blob c79c497f5012c3065de47887d819ecca426ac697 text_for_blobobj.txt'}
        treeObj = TreeObject(input_dir=self.input_dir + '1/',
                             output_dir=self.output_dir)
        treeObj.generate()
        self.assertEqual((treeObj.obj == etalon_set), True)

    def test_generate_blobobject_and_directory_2(self):
        """
        проверка строк которые получаются из папки  test-files/2/
        эталон резщультата находится в папке out-etalon/2/
        """
        treeObj = TreeObject(input_dir=self.input_dir + '2/',
                             output_dir=self.output_dir)
        treeObj.save()

        print(f'\n\n obj = ')
        treeObj.print()
        # TODO: здесь сделать сравнение двух папок на идентичность содержимого
        # self.assertEqual((treeObj.obj == etalon_set), True)