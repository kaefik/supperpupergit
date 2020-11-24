import unittest
import os

from treeobj.tree_obj import TreeObject


class BlobObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов типа Tree """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))

    def test_empty(self):
        pass