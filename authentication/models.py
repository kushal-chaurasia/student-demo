from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def get_full_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        return ""
    
    def update_subjects(self, subjects):
        self.subjects.add(subjects)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)

    def get_full_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        return ""


    





