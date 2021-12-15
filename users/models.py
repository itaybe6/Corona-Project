from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime


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


class MassegeT(models.Model):
    author = models.ForeignKey(Manager ,on_delete =models.CASCADE,default = None)
    subject = models.CharField(max_length = 255)
    content = models.TextField(max_length = 2500,null = True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name author : {self.author},subject: {self.subject}, ID: {self.content}' 

class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True , default = None )
    user_id = models.CharField(max_length=200, null = True)
    status = models.BooleanField(null= True,default = True)
    phone_number = models.CharField(max_length=200, null=True,default = None)
    password = models.CharField(max_length=200, null=True,default = None)
    my_class= models.CharField(max_length=200, null=True,default = None)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE,default = None)
    masseges = models.ManyToManyField(MassegeT,default = None)


    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'

class Student(models.Model):
    name = models.CharField(max_length=200, null = True,default = None)
    user_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True , default = False)
    phone_number = models.CharField(max_length=200, null=True,default = None)
    password = models.CharField(max_length=200, null=True,default = None)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE,default = None)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE,default = None)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'



