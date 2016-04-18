from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.full_name


class User(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name

