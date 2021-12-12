from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Manager(models.Model):
    name = models.CharField(max_length=200, null=True, default=None)
    user_id = models.CharField(max_length=200, null=True)
    status = models.BooleanField(null=True, default=True)
    phone_number = models.CharField(max_length=200, null=True, default=None)
    password = models.CharField(max_length=200, null=True, default=None)
    school = models.CharField(max_length=200, null=True, default=None)

    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True, default=None)
    user_id = models.CharField(max_length=200, null=True)
    status = models.BooleanField(null=True, default=True)
    phone_number = models.CharField(max_length=200, null=True, default=None)
    password = models.CharField(max_length=200, null=True, default=None)
    my_class = models.CharField(max_length=200, null=True, default=None)
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'


class Student(models.Model):
    name = models.CharField(max_length=200, null=True, default=None)
    user_id = models.CharField(max_length=200, null=True)
    status = models.BooleanField(null=True, default=False)
    phone_number = models.CharField(max_length=200, null=True, default=None)
    password = models.CharField(max_length=200, null=True, default=None)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, default=None)
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Name: {self.name}, ID: {self.user_id}'
<<<<<<< HEAD
=======

>>>>>>> 18e6f65f93eface58a7340394e1aa570ec93976d
