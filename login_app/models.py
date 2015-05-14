from django.db import models
from django.core.validators import MinValueValidator
from django import forms
# Create your models here.
SEX=(('M','Male'),('F','Female'))
BRANCH=(('CSE','Computer Science And Engineering'),('EE','Electrical Engineering'),('ECE','Electronics And Communication Engineering'),('MIED','Metalurgical Engineering'),('CE','Civil Engineering'),('ME','Mechanical Engineering'))
#not complete branch list

class user(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=256)
	email=models.EmailField(max_length=100,blank=False)
	def __str__(self):
		return self.username;

class profile(models.Model):
	username=models.OneToOneField(user,primary_key=True)
	#For one to one relationship between profile and user models
	name=models.CharField(max_length=100)
	enrollment=models.IntegerField(validators=[MinValueValidator(10000000)])
	branch=models.CharField(max_length=10,choices=BRANCH)
	date_of_birth=models.DateField()
	gender=models.CharField(max_length=1,choices=SEX)
	address=models.CharField(max_length=250)
	contact=models.CharField(max_length=15)
	about=models.CharField(max_length=500)
	def __str__(self):
		return self.name;
