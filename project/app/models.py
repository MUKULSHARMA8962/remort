from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Product(models.Model):
    priority=models.CharField(max_length=100,null=True,blank=True)
    issue=models.CharField(max_length=100,null=True,blank=True)
    time1=models.CharField(max_length=100,null=True,blank=True)
    sla=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        db_table="Product"

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
