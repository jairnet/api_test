"""Model Users"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model Profile"""
    users = models.OneToOneField(User, on_delete=models.PROTECT)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=20)

    def __str__(self):
        """Return Username"""
        return self.user.username
