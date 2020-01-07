from django.db import models
class RegistrationData(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    mobile= models.BigIntegerField()
    email= models.EmailField(max_length=100)
    gender= models.CharField(max_length=100)
    date_of_birth=models.DateField(max_length=100)
