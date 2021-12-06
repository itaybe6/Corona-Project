from django.test import TestCase
from users.models import Manager,Student,Teacher
from . import views


class UsersTestCase(TestCase):
   
    def test_CheckIfManagerExist(self):
        man = Manager(user_id='123456')
        man.save()
        self.assertTrue(views.CheckIfManagerExist('123456'),True)
        self.assertFalse(views.CheckIfManagerExist('1'),False)
        self.assertNotEqual(views.CheckIfManagerExist('2'),views.CheckIfManagerExist('123456'),True)

        man.delete()

    def test_CheckIfTeacherExist(self):
        man = Manager(user_id='123456')
        man.save()
        tea = Teacher(user_id='987',manager = man)
        tea.save()
        self.assertTrue(views.CheckIfTeacherExist('987'),True)
        self.assertFalse(views.CheckIfTeacherExist('96'),False)
        self.assertNotEqual(views.CheckIfTeacherExist('2'),views.CheckIfTeacherExist('987'),True)

        tea.delete()
        man.delete()

    def test_CheckIfStudentExist(self):
        man = Manager(user_id='123456')
        man.save()
        tea = Teacher(user_id='987',manager = man)
        tea.save()
        stu = Student(user_id = '111', manager = man , teacher = tea)
        stu.save()
        self.assertTrue(views.CheckIfStudentExist('111'),True)
        self.assertFalse(views.CheckIfStudentExist('8'),False)
        self.assertNotEqual(views.CheckIfStudentExist('2'),views.CheckIfStudentExist('111'),True)

        stu.delete()
        tea.delete()
        man.delete()

