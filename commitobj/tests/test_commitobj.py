import unittest
import os

from commitobj.commit_obj import CommitObject


class CommitObjectTest(unittest.TestCase):
    """ проверяем работоспособность объектов Commit """

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_dir_test = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = cls.current_dir_test + '/test-files/'
        cls.output_dir = cls.current_dir_test + '/test-files/out/'
