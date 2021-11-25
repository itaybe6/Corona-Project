from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=200, null = True)
    user_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.Manager_id}'

class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True)
    user_id = models.CharField(max_length=200, null = True)
    status = models.BooleanField(null= True)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.Teacher_id}'

class Student(models.Model):
    name = models.CharField(max_length=200, null = True)
    user_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.student_id}'
