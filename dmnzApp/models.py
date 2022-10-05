from turtle import position
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Admin_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200,default="")
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50) 
    
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
    
class categories(models.Model):
    
    category_name = models.CharField(max_length=255)

class Product(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True,default='')
    modelname = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=255,default='')
    gib = models.FileField( upload_to="images/",null=True,blank=True,default='')
    price = models.FloatField(default='')
    types = models.CharField(max_length=255,default='')
    format = models.CharField(max_length=255,default='')
    modeltype = models.CharField(max_length=255,default='')
    image = models.ImageField(null=True, blank=True,default='')

class freelancer(models.Model):
    full_name=models.CharField(max_length=255,default='')
    country=models.CharField(max_length=255,default='')
    mobile=models.CharField(max_length=255,default='')
    email=models.CharField(max_length=255,default='')
    url=models.CharField(max_length=255,default='')
    project_title=models.CharField(max_length=255,default='')
    position2=models.CharField(max_length=255,default='')
    day=models.CharField(max_length=255,default='')
    company=models.CharField(max_length=255,default='')
    position=models.CharField(max_length=255,default='')
    coment=models.CharField(max_length=255,default='')
    language=models.CharField(max_length=255,default='')
    work_position=models.CharField(max_length=255,default='')
    startdate=models.DateField()
    enddate=models.DateField()
    college=models.CharField(max_length=255,default='')
    special=models.CharField(max_length=255,default='')
    education=models.CharField(max_length=255,default='')



    




