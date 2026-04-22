from django.conf import settings
from django.db import models

# Create your models here.


class Semester(models.Model):
    semester_name = models.CharField(max_length=20, unique=True)
    
class Kurs(models.Model):
    kurs_name = models.CharField(max_length=100)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

class Student(models.Model):
    matrikel_nummer = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

class Professor(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

class Kursbeschreibung(models.Model):
    kurs = models.OneToOneField(Kurs, on_delete=models.CASCADE)
    beschreibung = models.TextField()    

class Studentenausweis(models.Model):
    ausweis_nummer = models.CharField(max_length=20, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
       
