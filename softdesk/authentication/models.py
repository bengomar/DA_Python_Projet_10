from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model"""

    age = models.PositiveIntegerField()
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
