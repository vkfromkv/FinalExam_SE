from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    semester = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.course
