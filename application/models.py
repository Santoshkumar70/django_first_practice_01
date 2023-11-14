from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=15,primary_key=True)
    email = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    