from collections import UserList
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Classes(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField(auto_now=False, auto_now_add=False)
    location=models.TextField()
    style=models.TextField(null=True, blank=True)
    detail=models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        db_table='classes'

class ClassDetail(models.Model):
    classdetailid=models.ForeignKey(Classes, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    detail=models.TextField()

    def __str__(self):
        return self.detail

    class Meta:
        db_table='classdetail'

class Pricing(models.Model):
    pricingid=models.ForeignKey(ClassDetail, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    description=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='pricing'


class Schedule(models.Model):
    title=models.CharField(max_length=255)
    location=models.TextField
    date=models.DateField()
    time=models.TimeField(auto_now=False, auto_now_add=False)
    description=models.TextField()

    def __str__(self):
            return self.title

    class Meta:
        db_table='schedule'