from django.db.models import manager
from django.http import response
from django.test import TestCase, Client
from users.models import Manager,Student,Teacher
from . import views


class UsersTestCase(TestCase):

    def test_submit_Manager(self):
        """test submit_manager function:
        check that the Manager obj can sign-up to the web with the data below"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj
        self.client = Client()
        
        response = self.client.post('/users/manager/signup_success', 
        {'user_id':'123456',
        'name': 'Rotem',
        'phone_number': '0523244458', 
        'school': 'Amit school', 
        'password': '123456789' },
        HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)
        self.assertEqual(man.user_id,'123456') #check that the obj is created with the give ID
        self.assertNotEqual(man.user_id,None)  #check that the default value (None) has changed
        self.assertEqual(man.status,True) #check that the status is True (the default)


    def test_submit_Teacher(self):
        """test submit_Teacher function:
         check that the Teacher obj can sign-up to the web with the data below"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj
        teacher = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj
        self.client = Client()

        response = self.client.post('/users/teacher/signup_success', 
        {'user_id':'11111',
        'name': 'Rona',
        'phone_number': '0523244666', 
        'password': '123456789',
        'my_class': "A-2" },
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)
        self.assertEqual(teacher.user_id,'11111') #check that the obj is created with the give ID
        self.assertNotEqual(teacher.user_id,None)  #check that the default value (None) has changed
        self.assertEqual(teacher.status,True) #check that the status is True (the default)


    def test_submit_Student(self):
        """test submit_Student function 
        checks that the Student obj can sign-up to the web with the data below"""

        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        teach = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj of teacher for the student
        student = Student.objects.create(user_id='20997765', manager=man,teacher=teach) #build a temporary obj

        self.client = Client()

        response = self.client.post('/users/student/signup_success', 
        {'user_id':'20997765',
        'name': 'Harel',
        'phone_number': '0523244666', 
        'password': '123456789',
         },
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)
        self.assertEqual(student.user_id,'20997765') #check that the obj is created with the give ID
        self.assertNotEqual(student.user_id,None)  #check that the default value (None) has changed
        self.assertEqual(student.status,False) #check that the student's status is False


    def test_CheckIfManagerExist(self):
        man = Manager(user_id='123456')
        man.save()
        self.assertTrue(views.CheckIfManagerExist('123456'),True)#check if the manager with uer_id 123456 exist
        self.assertFalse(views.CheckIfManagerExist('1'),False)#check if the manager with uer_id 1 exist
        self.assertNotEqual(views.CheckIfManagerExist('2'),views.CheckIfManagerExist('123456'),True)#check not equal for manager exist and no exist

        man.delete()


    def test_CheckIfTeacherExist(self):
        man = Manager(user_id='123456')
        man.save()
        tea = Teacher(user_id='987',manager = man)
        tea.save()
        self.assertTrue(views.CheckIfTeacherExist('987'),True)#check if the teacher with uer_id 987 exist
        self.assertFalse(views.CheckIfTeacherExist('96'),False)#check if the teacher with uer_id 96 exist
        self.assertNotEqual(views.CheckIfTeacherExist('2'),views.CheckIfTeacherExist('987'),True)#check not equal for teacher exist and no exist

        tea.delete() 
        man.delete()


    def test_CheckIfStudentExist(self):
        man = Manager(user_id='123456')
        man.save()
        tea = Teacher(user_id='987',manager = man)
        tea.save()
        stu = Student(user_id = '111', manager = man , teacher = tea)
        stu.save()
        self.assertTrue(views.CheckIfStudentExist('111'),True)#check if the student with uer_id 111 exist
        self.assertFalse(views.CheckIfStudentExist('8'),False)#check if the student with uer_id 8 exist
        self.assertNotEqual(views.CheckIfStudentExist('2'),views.CheckIfStudentExist('111'),True)#check not equal for student exist and no exist


        stu.delete()
        tea.delete()
        man.delete()


    def test_get_chooseprofile(self):
        """check if the button "choose profile" works and takes us to the right page and not 404"""
        
        self.client = Client()
        response = self.client.post('/users/chooseprofile', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)


    def test_get_student_signup(self):
        """check if the button "sign up for student" works and takes us to the right page and not 404"""
        
        self.client = Client()
        response = self.client.post('/users/student/signup', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)


    def test_get_teacher_signup(self):
        """check if the button "sign up for teacher" works and takes us to the right page and not 404"""
        
        self.client = Client()
        response = self.client.post('/users/teacher/signup', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)


    def test_get_manager_signup(self):
        """check if the button "sign up for manager" works and takes us to the right page and not 404"""
        
        self.client = Client()
        response = self.client.post('/users/manager/signup', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)
    

    def test_logout_user(self):
        """check if logout buttom takes us to the homepage and disconnects us"""
        self.client = Client()
        response = self.client.post('', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)

    def test_Phones(self):
        """check if Phones buttom takes us to the phones page of the teacher"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        teach = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj of teacher for the student
        self.client = Client()
        response = self.client.post('/users/Phones/89711111654/', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)

    def test_PhonesTeacher(self):
        """check if Phones buttom takes us to the phones page of the manager"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        self.client = Client()
        response = self.client.post('/users/PhonesT/897123456654', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)

    def test_PhonesStudent(self):
        """check if Phones buttom takes us to the phones page of the teacher"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        teach = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj of teacher for the student
        student = Student.objects.create(user_id='20997765', manager=man,teacher=teach) #build a temporary obj

        self.client = Client()
        response = self.client.post('/users/PhoneStu/89720997765654', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)


    def test_StuAdministrativePhones(self):
        """check if Phones buttom takes us to the phones page of the teacher"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        teach = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj of teacher for the student
        student = Student.objects.create(user_id='20997765', manager=man,teacher=teach) #build a temporary obj

        self.client = Client()
        response = self.client.post('/users/StuAdministrativePhones/89720997765654', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)


    def test_HomePageBetweenPathTeacher(self):
        """check if the teacher user can get to the home page"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        teach = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj of teacher
        self.client = Client()
        response = self.client.post('/users/HomePageTeacher/89711111654/', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertNotEqual(response.status_code,404)

    def test_HomePageBetweenPathManager(self):
        """check if the manager user can get to the home page"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager
        self.client = Client()
        response = self.client.post('/users/HomePageManager/897123456654/', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)#check if move to path
        self.assertNotEqual(response.status_code,404)


    def test_HomePageBetweenPathStudent(self):
        """check if the teacher user can get to the home page"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        teach = Teacher.objects.create(user_id='11111', manager=man) #build a temporary obj of teacher
        student = Student.objects.create(user_id='20997765', manager=man,teacher=teach) #build a temporary obj

        self.client = Client()
        response = self.client.post('/users/HomePageStudent/89720997765654/', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)#check if move to path
        self.assertNotEqual(response.status_code,404)


    def test_ChanageStatusManager(self):
        """check if the manager status realy change-
        the defult status of the obj is True - test before and after the ChanageStatusManager for double check"""
        man = Manager.objects.create(user_id='123456') #build a temporary obj of manager for the teacher
        self.assertEqual(man.status,True) #before the function - default is True

        self.client = Client()
        response = self.client.post('/users/ChanageStatusManager/897123456654/', 
        HTTP_ACCEPT='application/json')
        response = self.client.post('/users/ChanageStatusManager/897123456654/', 
        HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)#check if move to path
        self.assertNotEqual(response.status_code,404)
        self.assertEqual(man.status,True) #after the function - change to False
