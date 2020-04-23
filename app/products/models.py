from django.db import models

# Create your models here.
class ProductOne(models.Model):
    name = models.TextField()
    description = models.TextField(default='CocaCola')
    price = models.TextField()
    supplier = models.TextField()
