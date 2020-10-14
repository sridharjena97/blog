from django.db import models

# Create your models here.
class Contact(models.Model):
    srl= models.AutoField(primary_key=True)
    name= models.CharField(max_length=150, default='')
    email= models.EmailField(max_length=254, default='')
    mobileNumber= models.CharField(max_length=13, null=True, default='')
    messageTitle= models.CharField(max_length=500, default='NA')
    messageBody= models.CharField(max_length=1000, default='NA')
    tmeStamp= models.TimeField(auto_now=True, blank=True)
    def __str__(self):
        return self.messageTitle
    


