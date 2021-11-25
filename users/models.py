from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200, null = True)
    student_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True)
    def __str__(self):
        return f'Name: {self.name}, ID: {self.student_id}'


class Manager(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Manager_id = models.CharField(max_length=200,null = True)
    status = models.BooleanField(null= True)

    def __str__(self):
        return f'Name: {self.name}, ID: {self.Manager_id}'

