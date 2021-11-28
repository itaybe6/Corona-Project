from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=200, null = True, default = None)
    user_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True,default = True)
    phone_number = models.CharField(max_length=200, null=True, default = None)
    password = models.CharField(max_length=200, null=True, default = None)
    school = models.CharField(max_length=200, null=True, default = None)

    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'

class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True , default = None )
    user_id = models.CharField(max_length=200, null = True)
    status = models.BooleanField(null= True,default = True)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE)
    my_class= models.CharField(max_length=200, null=True,default = None)
    class_num = models.IntegerField(null=True,default = None)
    phone_number = models.CharField(max_length=200, null=True,default = None)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'

class Student(models.Model):
    name = models.CharField(max_length=200, null = True,default = None)
    user_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True , default = False)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=200, null=True,default = None)
    password = models.CharField(max_length=200, null=True,default = None)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'
