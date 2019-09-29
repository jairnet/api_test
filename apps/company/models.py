from django.db import models
from rest_framework.authtoken.models import Token


class Company(models.Model):
    name = models.CharField(max_length=20, default='')
    nit = models.CharField(max_length=20, default='')
    token = models.ForeignKey(Token, null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
