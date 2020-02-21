from django.db import models

# Create your models here.
class Postion(models.Model):
	title   =  models.CharField(max_length=40)

	def __str__(self):
		return self.title


class Employee(models.Model):
	fullname =   models.CharField(max_length=50)
	email    =   models.EmailField()
	content  =   models.TextField()
	position  =   models.ForeignKey(Postion, on_delete=models.CASCADE)

	def __str__(self):
		return self.fullname + "'s Information "