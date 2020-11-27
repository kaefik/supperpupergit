import unittest
import os
import shutil

from treeobj.tree_obj import ItemTreeObject, BLOB, NOOBJ, TREE


class ItemTreeObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа ItemTree """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = cls.current_dir_test + '/test-files/'
        cls.output_dir = cls.current_dir_test + '/test-files/out_item/'

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

    def test_save_blob_object(self):
        """
        проверка правильно ли сформировалась запись BlobObject
        """
        item = ItemTreeObject(input_name=self.input_dir + 'text_for_blobobj.txt')
        item.save(output_dir=self.output_dir)
        # print('\n\n' + self.output_dir + 'c7/9c497f5012c3065de47887d819ecca426ac697')
        flag = os.path.exists(self.output_dir + 'c7/9c497f5012c3065de47887d819ecca426ac697')
        self.assertEqual(flag, True)

    def test_get_string_itemobj(self):
        """
        проверка правильно ли сформировалась строка записи
        """
        item = ItemTreeObject(input_name=self.input_dir + 'text_for_blobobj.txt')
        item.save(output_dir=self.output_dir)
        # print('\n\n' + self.output_dir + 'c7/9c497f5012c3065de47887d819ecca426ac697')
        etalon_string = '000000 blob c79c497f5012c3065de47887d819ecca426ac697 text_for_blobobj.txt'
        item.save(output_dir=self.output_dir)
        result_string = item.get()
        # print(f'\n\n {result_string}')
        self.assertEqual(result_string, etalon_string)
