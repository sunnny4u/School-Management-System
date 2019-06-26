from django.db import models

# Create your models here.

class StudentInfo(models.Model):
		name = models.CharField(max_length=50)
		age = models.IntegerField()
		roll = models.IntegerField()
		subject = models.CharField(max_length=10)
		department = models.CharField(max_length=15)

		def __str__(self):
			return self.name

class DistrictInfo(models.Model):
		name = models.CharField(max_length=50)
		area = models.IntegerField()
		population = models.IntegerField()
		division = models.CharField(max_length=50)


		def __str__(self):
			return self.name


class UpazilaInfo(models.Model):
		name = models.CharField(max_length=50)
		area = models.IntegerField()
		population = models.IntegerField()
		division = models.CharField(max_length=50)


		def __str__(self):
			return self.name



class ShopInfo(models.Model):
		ShopName = models.CharField(max_length=80)
		Rent = models.IntegerField()
		PaidRent = models.IntegerField()
		comments = models.CharField(max_length=50)


		def __str__(self):
			return self.ShopName
