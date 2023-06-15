from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    education = models.CharField(max_length=500)
    address = models.CharField(max_length=500, default='Borivali')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=500)
    pincode = models.CharField(max_length=100, default='400103')
    country = models.CharField(max_length=500, default='India')
    salary_annul_ctc = models.CharField(max_length=500, default='3Lpa')
    
    