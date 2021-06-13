from django.db import models
from datetime import datetime

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Parent(models.Model):
    first_name = models.CharField(max_length=200, default='name')
    last_name = models.CharField(max_length=200, default='name')
    email = models.CharField(max_length=200)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.first_name + self.last_name

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=200, default='name')
    last_name = models.CharField(max_length=200, default='name')
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Week(models.Model):
    child = models.ManyToManyField(Child)
    start_date = models.DateField()
    end_date = models.DateField()
    registered = models.BooleanField()

    def __str__(self):
        smonth = self.start_date.strftime("%m")
        sday = self.start_date.strftime("%d")
        emonth = self.end_date.strftime("%m")
        eday = self.end_date.strftime("%d")

        # converts dates to strings
        return smonth + '/' + sday + '-' + emonth + '/' + eday


class Day(models.Model):
    week = models.ForeignKey(Week, on_delete = models.CASCADE)
    date = models.DateField()
    itinerary = models.TextField()

    