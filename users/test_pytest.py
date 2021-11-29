from users.models import Manager , Teacher,Student
from . import views




def testCheckIfManagerExist():
    assert views.CheckIfManagerExist('12345') == True
    assert views.CheckIfManagerExist('154') == False

def testCheckIfStudentExist():    
    assert views.CheckIfStudentExist('123456') == True
    assert views.CheckIfStudentExist('154') == False

def testCheckIfTeacherExist():
    assert views.CheckIfTeacherExist('199') == True
    assert views.CheckIfTeacherExist('1111') == False      