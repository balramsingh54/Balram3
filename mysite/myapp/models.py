from django.db import models

# Create your models here.
class Register(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	fathername=models.CharField(max_length=20)
	addr=models.TextField(max_length=50)
	userid=models.CharField(max_length=20,primary_key=True)
	passwd=models.CharField(max_length=20)
	class Meta:
		db_table='Register'
