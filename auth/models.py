from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=10)
    access = models.CharField(max_length=10)
    userCode = models.CharField(max_length=10)
