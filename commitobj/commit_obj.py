"""
 реализация Объектов типа Commit
"""


class CommitObject:
    """
    одному коммиту соответствует только одно дерево, хранить также ссылку на родительский коммит (-ы)
        (кроме первого коммита), на автора, сообщение коммита.
    """

    def __init__(self, treeobj=None, parrent_commint=None, author=None, commiter=None, message_commit=None):
        self.treeobj = treeobj  # ссылка на TreeObject
        self.parrent_commint = parrent_commint  # родительский коммит (-ы) в виде массива
        self.author = author  # автор коммита
        self.commiter = commiter  # коммитер
        self.message_commit = message_commit  # текстовое сообщение коммита
        self.sha1 = None
        self.date = None

    def generate(self):
        """
        генерация содержимого коммита
        return: возвращает sha1 содержимого коммита
        """
        return self.sha1

    def save(self, output_dir='./'):
        """
        сохранение коммита в папку output_dir
        """
        self.generate()
        # TODO: здесь должно быть  сохранение коммита

    def check_exist_commit(self, check_dir=""):
        pass

    pass
