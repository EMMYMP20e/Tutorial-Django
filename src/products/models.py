from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.TextField()
    descriptio = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')
