from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='homework',null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
