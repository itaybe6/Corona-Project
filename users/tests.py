import unittest
from django.db import models
from django.test import TestCase
from users.models import Manager , Teacher,Student



class Testviwes(unittest.TestCase):

    def testCheckIfManagerExist(self):
        Man = Manager(user_id = '12345')
        Man.save()
        
        self.assertTrue(views.CheckIfManagerExist(Man.user_id),'must to be True')
        self.assertFalse(views.CheckIfManagerExist('154'),'must to be False')
        self.assertNotEqual(views.CheckIfManagerExist('154'),views.CheckIfManagerExist(Man.user_id),'must to be True')
        Man.delete()
    
    def testCheckIfStudentExist(self):
        stu = Student(user_id = '123456',manager = Manager.objects.get(user_id ='123456789') , teacher = Teacher.objects.get(user_id = '123'))
        stu.save()

        self.assertTrue(views.CheckIfStudentExist(stu.user_id),'must to be True')
        self.assertFalse(views.CheckIfStudentExist('154'),'must to be False')
        self.assertNotEqual(views.CheckIfStudentExist('198'),views.CheckIfStudentExist(stu.user_id),'must to be True')
        stu.delete()

    def testCheckIfTeacherExist(self):
        tea = Teacher(user_id = '199' , manager = Manager.objects.get(user_id ='123456789'))
        tea.save()

        self.assertTrue(views.CheckIfTeacherExist(tea.user_id),'must to be True')
        self.assertFalse(views.CheckIfTeacherExist('1111'),'must to be False')
        self.assertNotEqual(views.CheckIfTeacherExist('777'),views.CheckIfTeacherExist(tea.user_id),'must to be True')
        tea.delete()


    


        


    

    def 


if __name__ == '__main__':
    unittest.main()
# Create your tests here.
