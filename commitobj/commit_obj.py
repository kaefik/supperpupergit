"""
 реализация Объектов типа Commit
"""

from datetime import datetime
import time
from tools_objects import obj_sha1, get_file_dirs


class CommitObject:
    """
    одному коммиту соответствует только одно дерево, хранить также ссылку на родительский коммит (-ы)
        (кроме первого коммита), на автора, сообщение коммита.
    """

    def __init__(self, treeobj_sha1=None, parrent_commint=None,
                 author={'name': None, 'email': None},
                 commiter={'name': None, 'email': None}, message_commit=None):
        """
        author и commiter  словарь вида: {'name': None, 'email': None}
        """
        self.treeobj_sha1 = treeobj_sha1  # sha1 объекта TreeObject
        self.parrent_commint = parrent_commint  # родительский коммит (-ы) в виде массива id коммитов
        self.author = author  # автор коммита
        self.commiter = commiter  # коммитер
        self.message_commit = message_commit  # текстовое сообщение коммита
        self.sha1 = None
        self.date = None  # автоматически дата должна генерироваться

    def generate(self):
        """
        генерация содержимого коммита
        return: содержимое коммита
        """
        result = ''
        # если нет дерева на который ссылается коммит, то это не коммит.
        # также если нет комментария к коммиту
        if self.treeobj_sha1 is None or self.message_commit is None:
            return None

        # TODO: проверить что поля author и commiter заполнены,
        #  если нет то возвращаем исключение? или что-то другое

        self.date = datetime.now()
        unixtime = time.mktime(self.date.timetuple())  # перевод в Unix Time
        delta_hour_timezone = int(time.altzone / 3600) * (-1)
        if delta_hour_timezone > 0:
            timezone = f'+{delta_hour_timezone}'  # часовая зона
        else:
            timezone = f'-{delta_hour_timezone}'  # часовая зона
        result += f'tree {self.treeobj_sha1}\n'
        if self.parrent_commint is not None:
            parent = ''
            for p in self.parrent_commint:
                parent += p + ' '
            result += f'parent {parent}\n'
        result += f'author {self.author["name"]} {self.author["email"]} {unixtime} {timezone}\n'
        result += f'committer {self.commiter["name"]} {self.commiter["email"]} {unixtime} {timezone}\n'
        result += '\n'
        result += f'{self.message_commit}'
        return result

    def check_exist_blob(self, check_dir=""):
        """
        проверка на существования такого же commit файла
        :param check_dir  - папка там где находится файл blobobject
        :return: True - если такой файл существует
        """
        # TODO: сделать функцию проверки существования файла коммита
        # if check_dir == "":
        #     check_dir = self.output_dir
        #
        # directory = self.sha1[:2] + '/'
        # filename = self.sha1[2:]
        # full_filename = check_dir + directory + filename
        # flag_exist_file = os.path.exists(full_filename)
        #
        # if flag_exist_file:
        #     with open(full_filename, "br") as f:
        #         filecontent = f.read()
        #
        #     sha1_file = obj_sha1(filecontent)
        #     if sha1_file != self.sha1:
        #         error_text = f"FATAL ERROR: Файл {directory + filename} существует, но содержимое скомпрометировано."
        #         # print(error_text)
        #         raise BaseException(error_text)
        # else:
        #     return False

        return True

    def save(self, output_dir='./'):
        """
        сохранение коммита в папку output_dir
        return: True - если сохранился коммит в файл, иначе False
        """
        self.generate()
        # TODO: здесь должно быть  сохранение коммита

        filecontent = self.generate()

        if filecontent is None:
            return False

        self.sha1 = obj_sha1(filecontent.encode())

        if self.sha1 is None:
            return False

        commit_dir = output_dir + self.sha1[:2] + '/'
        # проверка на существование корректного commit-файла
        if self.check_exist_blob(output_dir):
            return True

        try:
            os.makedirs(commit_dir)
        except FileExistsError:
            # если файл существует проверяем на то что он корректный с точки зрения хеша
            flag = self.check_exist_blob(output_dir)
            if flag:
                return self.sha1

        with open(commit_dir + self.sha1[2:], "tw") as f:
            f.write(filecontent)
        return True


def main():
    # c = CommitObject(treeobj_sha1='123456789', parrent_commint=['dekadklsahdkas', '13131313'],
    #                  author={'name': 'Ilnur Saifutdinov', 'email': 'my@my.com'},
    #                  commiter={'name': 'Amir Saifutdinov', 'email': 'my@my2.com'},
    #                  message_commit='first commit')

    c = CommitObject()

    print(c.generate())


if __name__ == '__main__':
    main()
