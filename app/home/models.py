from django.db import models

# Create your models here.
class Contacts(models.Model):
    srl= models.AutoField(primary_key=True)
    name= models.CharField(max_length=150, default='')
    email= models.EmailField(max_length=254)
    mobileNumber= models.IntegerField(blank=True, null= True)
    mesaageTitle= models.CharField(max_length=500)
    messageBody= models.CharField(max_length=1000)
    


