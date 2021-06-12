from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Parent(models.Model):
    first_name = models.CharField(max_length=200, default='name')
    last_name = models.CharField(max_length=200, default='name')
    email = models.CharField(max_length=200)
    phone_number = PhoneNumberField()

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=200, default='name')
    last_name = models.CharField(max_length=200, default='name')
    age = models.IntegerField()

class Week(models.Model):
    child = models.ForeignKey(Child, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    registered = models.BooleanField()

class Day(models.Model):
    week = models.ForeignKey(Week, on_delete = models.CASCADE)
    date = models.DateField()
    itinerary = models.TextField()