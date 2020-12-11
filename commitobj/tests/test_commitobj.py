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

    def test_generate_with_one_parent(self):
        mycommit = CommitObject(treeobj_sha1='123456789', parrent_commint=['13131313'],
                                author={'name': 'Ilnur Saifutdinov', 'email': 'my@my.com'},
                                commiter={'name': 'Amir Saifutdinov', 'email': 'my@my2.com'},
                                message_commit='first commit')

        gen_commit = mycommit.generate()
        self.assertNotEqual(gen_commit, None)
        gen_commit_list = gen_commit.split('\n')
        print(gen_commit_list)

        self.assertEqual('tree 123456789', gen_commit_list[0])
        self.assertEqual('parent 13131313', gen_commit_list[1])
        self.assertEqual(gen_commit_list[2].index('author Ilnur Saifutdinov my@my.com') == 0, True)
        self.assertEqual(gen_commit_list[3].index('committer Amir Saifutdinov my@my2.com') == 0, True)
        self.assertEqual('', gen_commit_list[4])
        self.assertEqual('first commit', gen_commit_list[5])

    def test_generate_with_parents(self):
        mycommit = CommitObject(treeobj_sha1='123456789', parrent_commint=['dekadklsahdkas', '13131313'],
                                author={'name': 'Ilnur Saifutdinov', 'email': 'my@my.com'},
                                commiter={'name': 'Amir Saifutdinov', 'email': 'my@my2.com'},
                                message_commit='first commit')

        gen_commit = mycommit.generate()
        self.assertNotEqual(gen_commit, None)
        gen_commit_list = gen_commit.split('\n')

        self.assertEqual('tree 123456789', gen_commit_list[0])
        self.assertEqual('parent dekadklsahdkas 13131313', gen_commit_list[1])
        self.assertEqual(gen_commit_list[2].index('author Ilnur Saifutdinov my@my.com') == 0, True)
        self.assertEqual(gen_commit_list[3].index('committer Amir Saifutdinov my@my2.com') == 0, True)
        self.assertEqual('', gen_commit_list[4])
        self.assertEqual('first commit', gen_commit_list[5])

    def test_generate_without_parent(self):
        mycommit = CommitObject(treeobj_sha1='123456789', parrent_commint=[],
                                author={'name': 'Ilnur Saifutdinov', 'email': 'my@my.com'},
                                commiter={'name': 'Amir Saifutdinov', 'email': 'my@my2.com'},
                                message_commit='first commit')

        gen_commit = mycommit.generate()
        self.assertNotEqual(gen_commit, None)
        gen_commit_list = gen_commit.split('\n')

        self.assertEqual('tree 123456789', gen_commit_list[0])
        # self.assertEqual('parent dekadklsahdkas 13131313', gen_commit_list[1])
        self.assertEqual(gen_commit_list[1].index('author Ilnur Saifutdinov my@my.com') == 0, True)
        self.assertEqual(gen_commit_list[2].index('committer Amir Saifutdinov my@my2.com') == 0, True)
        self.assertEqual('', gen_commit_list[3])
        self.assertEqual('first commit', gen_commit_list[4])

    def test_generate_without_parent2(self):
        mycommit = CommitObject(treeobj_sha1='123456789', parrent_commint=None,
                                author={'name': 'Ilnur Saifutdinov', 'email': 'my@my.com'},
                                commiter={'name': 'Amir Saifutdinov', 'email': 'my@my2.com'},
                                message_commit='first commit')

        gen_commit = mycommit.generate()
        self.assertNotEqual(gen_commit, None)
        gen_commit_list = gen_commit.split('\n')

        self.assertEqual('tree 123456789', gen_commit_list[0])
        # self.assertEqual('parent dekadklsahdkas 13131313', gen_commit_list[1])
        self.assertEqual(gen_commit_list[1].index('author Ilnur Saifutdinov my@my.com') == 0, True)
        self.assertEqual(gen_commit_list[2].index('committer Amir Saifutdinov my@my2.com') == 0, True)
        self.assertEqual('', gen_commit_list[3])
        self.assertEqual('first commit', gen_commit_list[4])
