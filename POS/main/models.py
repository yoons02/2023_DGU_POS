# Create your models here.
from django.db import models
from django import forms

# Create your models here.
class Table(models.Model):
    id = models.AutoField(primary_key=True)
    menu1 = models.IntegerField(default=0)
    menu2 = models.IntegerField(default=0)
    menu3 = models.IntegerField(default=0)
    menu4 = models.IntegerField(default=0)
    menu5 = models.IntegerField(default=0)
    menu6 = models.IntegerField(default=0)
    menu7 = models.IntegerField(default=0)
    menu8 = models.IntegerField(default=0)
    special_note = models.TextField(null=True, blank=True)
    total = models.IntegerField(default=0)

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0) 

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    menu1 = models.IntegerField(default=0)
    menu2 = models.IntegerField(default=0)
    menu3 = models.IntegerField(default=0)
    menu4 = models.IntegerField(default=0)
    menu5 = models.IntegerField(default=0)
    menu6 = models.IntegerField(default=0)
    menu7 = models.IntegerField(default=0)
    menu8 = models.IntegerField(default=0)
    special_note = models.TextField(null=True, blank=True)
    total = models.IntegerField(default=0)    

class Total(models.Model):
    id = models.AutoField(primary_key=True)
    menu1 = models.IntegerField(default=0)
    menu2 = models.IntegerField(default=0)
    menu3 = models.IntegerField(default=0)
    menu4 = models.IntegerField(default=0)
    menu5 = models.IntegerField(default=0)
    menu6 = models.IntegerField(default=0)
    menu7 = models.IntegerField(default=0)
    menu8 = models.IntegerField(default=0) 
    total = models.IntegerField(default=0)  