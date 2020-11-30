import unittest
import os
import shutil
from tools_objects import create_new_dir, get_file_dirs

from treeobj.tree_obj import TreeObject


class TreeObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Tree """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = cls.current_dir_test + '/test-files/'
        cls.output_dir = cls.current_dir_test + '/test-files/out/'

    # def setUp(self) -> None:
    #     # создаем папку для файлов которые создаются для тестов
    #     create_new_dir(self.output_dir)

    # def tearDown(self) -> None:
    #     # удаляем папку для файлов которые создаются для тестов
    #     shutil.rmtree(self.output_dir, ignore_errors=False, onerror=None)

    def test_get_all_files_and_directory_1(self):
        """
        проверка получения всех файлов и папок в папке  test-files/1/
        """
        treeObj = TreeObject(input_dir=self.input_dir + '1/',
                             output_dir=self.output_dir + '1/')
        treeObj.get_all_files_and_directory()

        self.assertEqual(treeObj._files, {'text_for_blobobj.txt'})
        self.assertEqual(treeObj._directory, set())

    def test_get_all_files_and_directory_2(self):
        """
        проверка получения всех файлов и папок в папке  test-files/2/
        """
        treeObj = TreeObject(input_dir=self.input_dir + '2/', output_dir=self.output_dir + '2/')
        treeObj.get_all_files_and_directory()

        self.assertEqual(treeObj._files, {'1.py', 'file1.txt'})
        self.assertEqual(treeObj._directory, {'papka1'})

    def test_generate_blobobject_1(self):
        """
        проверка сохранения blobobj из папки  test-files/1/
        """
        etalon_set = {'000000 blob c79c497f5012c3065de47887d819ecca426ac697 text_for_blobobj.txt'}
        treeObj = TreeObject(input_dir=self.input_dir + '1/',
                             output_dir=self.output_dir + '3/')
        treeObj.save()
        self.assertEqual((treeObj.obj == etalon_set), True)

    def test_generate_blobobject_and_directory_2(self):
        """
        проверка строк которые получаются из папки  test-files/2/
        эталон результата находится в папке out-etalon/2/
        """
        input_dir = self.input_dir + '2/'
        output_dir = self.output_dir + '4/'
        create_new_dir(output_dir)
        treeObj = TreeObject(input_dir=input_dir,
                             output_dir=output_dir)
        treeObj.save()
        # print(f'\n\n obj = ')
        # treeObj.print()
        # TODO: здесь сделать сравнение двух папок на идентичность содержимого
        files, directory = get_file_dirs(output_dir)
        files_etalon, directory_etalon = get_file_dirs(self.input_dir + 'out-etalon/2/')

        # print(f'\n\n{directory}')
        # print(f'\n\netalon = {directory_etalon}')
        # print(f'\n\nразность = {directory.difference(directory_etalon)}')

        self.assertEqual((files == files_etalon), True)
        self.assertEqual((directory == directory_etalon), True)

    def test_generate_blobobject_and_directory_0(self):
        """
        проверка строк которые получаются из папки пустой
        никакого объекта не должно быть

        """
        input_dir = self.input_dir + '0/'
        output_dir = self.output_dir + '5/'
        create_new_dir(input_dir)
        create_new_dir(output_dir)
        treeObj = TreeObject(input_dir=input_dir,
                             output_dir=output_dir)
        treeObj.save()
        files, directory = get_file_dirs(output_dir)

        self.assertEqual((files == set()), True)
        self.assertEqual((directory == set()), True)

    def test_generate_blobobject_and_directory_emptydirectories(self):
        """
        проверка строк которые получаются из вложенных папок без файлов
        никакого объектов не должно быть создано
        """
        input_dir = self.input_dir + '0/1/'
        output_dir = self.output_dir + '6/'
        create_new_dir(input_dir)
        create_new_dir(output_dir)
        treeObj = TreeObject(input_dir=self.input_dir + '0/',
                             output_dir=output_dir)
        treeObj.save()
        files, directory = get_file_dirs(output_dir)

        self.assertEqual((files == set()), True)
        self.assertEqual((directory == set()), True)

    def test_generate_blobobject_and_directory_3(self):
        """
        проверка как создаеются объекты когда есть папки и в них одинаковый файл с одинаковым именем
        """
        input_dir = self.input_dir + '3/'
        output_dir = self.output_dir + '7/'
        # создание тестового задания
        create_new_dir(input_dir)
        create_new_dir(input_dir + 'papka1/papka1_1')
        create_new_dir(input_dir + 'papka2')
        shutil.copy(self.input_dir + 'file1.txt', input_dir)
        shutil.copy(self.input_dir + 'file1.txt', input_dir + 'papka1')
        shutil.copy(self.input_dir + 'file1.txt', input_dir + 'papka2')

        create_new_dir(output_dir)

        treeObj = TreeObject(input_dir=input_dir,
                             output_dir=output_dir)
        treeObj.save()
        # print('\n\n')
        # treeObj.print()
        # print(f'\n{treeObj.obj}')
        files, directory = get_file_dirs(output_dir)

        self.assertEqual((files == set()), True)
        self.assertEqual((directory == {'08', '5b', '8e'}), True)
