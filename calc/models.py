from django.db import models

# Create your models here.
class signup(models.Model):
    username = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    
class register(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    username =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    password1 =models.CharField(max_length=100)
    password2 =models.CharField(max_length=100)

    
class add(models.Model):
    full_name =models.CharField(max_length=200)
    age =models.IntegerField()
    blood =models.CharField(max_length=100)
    phone_no =models.IntegerField()
    gender =models.CharField(max_length=100)