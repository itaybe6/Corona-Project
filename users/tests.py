import unittest
from django.db import models
from django.db.models import manager
from django.test import TestCase
from users.models import Manager
from users.models import Teacher
from users.models import Student


class CreateUserTastCase(unittest.TestCase):

    def create_manager(self):
        """if we can create manager user for school"""
        manager = Manager.user_id(123456789)

        self.assertTrue(Manager.user_id(123456789, manager))


if __name__ == '__main__':
    unittest.main()
# Create your tests here.
