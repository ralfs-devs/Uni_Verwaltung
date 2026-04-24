from django.conf import settings
from django.db import models

# Create your models here.


class Semester(models.Model):
    semester_name = models.CharField(max_length=20, unique=True)

class Professor(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)    
    
class Kurs(models.Model):
    kurs_name = models.CharField(max_length=100)
    # wenn Semester gelöscht wird, werden auch alle Kurse die dem Semester zugeordnet sind gelöscht
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,
                                 related_name='semester_kurse', related_query_name='semester_kurs')
    # ein Professor kann nicht gelöscht werden, wenn ihm noch Kurse zugeordnet sind. Es muss erst die Zuordnung zu den Kursen entfernt werden, bevor der Professor gelöscht werden kann.
    professor = models.ForeignKey(Professor, on_delete=models.RESTRICT,
                                  related_name='professor_kurse', related_query_name='professor_kurs')

class Student(models.Model):
    matrikel_nummer = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    kurs = models.ManyToManyField(Kurs, related_name='studenten') #ein Student kann mehrere Kurse belegen und ein Kurs kann von mehreren Studenten belegt werden. Die Beziehung wird über eine ManyToManyField definiert.

class Kursbeschreibung(models.Model):
    kurs = models.OneToOneField(Kurs, on_delete=models.CASCADE)
    kurs_name = models.CharField(max_length=100)
    beschreibung = models.TextField()

class Studentenausweis(models.Model):
    ausweis_nummer = models.CharField(max_length=20, unique=True)
    #student = models.OneToOneField(Student, on_delete=models.CASCADE)
    student_matrikel_nummer = models.ForeignKey(Student, to_field='matrikel_nummer', on_delete=models.CASCADE, unique=True, related_name='studentenausweise', related_query_name='studentenausweis')
