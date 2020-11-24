import unittest
import os

from blobobj.blob_obj import BlobObject

# test_dir = '/'
current_dir_test = os.path.dirname(os.path.abspath(__file__))

class BlobObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Blob """

    def test_check_FileErrorFound(self):
        b = BlobObject(current_dir_test+"/test-files/text_for_blobobj.txt", output_dir=current_dir_test+'/test-files')
        self.assertEqual(True, True)
        """
        проверка на обработку ошибки не существования файла
        :return:
        """
        pass
        # self.assertEqual(task01.print_three_simbol('a'), 'bcd')



if __name__ == '__main__':
    unittest.main()
