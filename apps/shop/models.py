from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    code = models.CharField(max_length=255, default='') 

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    site = models.CharField(max_length=255, default='')
    email = models.EmailField()
    country = models.CharField(max_length=255, default='')
    district = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    category = models.ManyToManyField(Category)
    description = models.TextField(max_length=2000)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
