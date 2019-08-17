from django.db import models
from datetime import datetime
# Create your models here.
class Barbers(models.Model):
    barber_name=models.CharField(max_length=200)
    post=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    joined_date=models.DateTimeField(default=datetime.now,blank=True)
    facebook_link = models.CharField(max_length=300,default='SOME STRING')
    github_link = models.CharField(max_length=300,default='SOME STRING')
    twitter_link = models.CharField(max_length=300,default='SOME STRING')
    linkedin_link = models.CharField(max_length=300,default='SOME STRING')


    def __str__(self):
        return self.barber_name




class Opening(models.Model):
    day=models.CharField(max_length=100)
    datetime=models.CharField(max_length=100)

    def __str__(self):
        return self.day

class Appointment(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    more_details=models.TextField(blank=True)

    def __str__(self):
        return self.first_name

class Services(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    more_details=models.TextField(blank=True)

    def __str__(self):
        return self.first_name





