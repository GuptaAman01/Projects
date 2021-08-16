from django.db import models

# Create your models here.
class product(models.Model):
    pname = models.CharField(default= 0, max_length=100)
    price = models.IntegerField(default=0)
    create = models.IntegerField(default=0)
    update = models.IntegerField(default=0)
    
    def __init__(self,pname,price,cat,uat):
        self.pname = pname
        self.price = price
        self.cat = cat
        self.uat = uat

class User(models.Model):
    first_name = models.CharField(default = 0, max_length=100)
    last_name = models.CharField(default = 0, max_length=100)
    email = models.EmailField(default = 0, max_length=100)
    password = models.CharField(default = 0, max_length=100)
    username = models.CharField(default = 0, max_length=100)