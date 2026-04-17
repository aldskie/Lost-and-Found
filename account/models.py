from django.db import models

# Create your models here.
class Account(models.Model):
    user_level = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]



    firstName = models.CharField()
    lastName = models.CharField()
    email = models.CharField()
    user_level = models.CharField(choices=user_level)
    username = models.CharField()
    password = models.CharField()

    def __str__(self):
        return self.user_level
