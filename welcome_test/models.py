from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField(max_length=200, unique=True)
    description = models.CharField(max_length=500,blank=True)
    start_date  = models.DateTimeField(auto_now_add=True)
