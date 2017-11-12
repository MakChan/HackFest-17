from django.db import models

# Create your models here.
class Hospital(models.Model):
    doctors = models.ForeignKey('Doctors')
    patient = models.ForeignKey('Patient')

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class Blogs(models.Model):
    author = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
