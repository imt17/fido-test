# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    friends = models.ManyToManyField('self', symmetrical=False, related_name='friends_list', blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
