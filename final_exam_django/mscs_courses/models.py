from django.db import models

class Course(models.Model):
    """
    A Django model representing a course.

    This model is used to store information about courses in a database. Each course
    has details about the semester, course name, instructor, and location.

    Attributes:
        semester (models.CharField): The semester when the course is offered.
        course (models.CharField): The name of the course.
        instructor (models.CharField): The name of the course instructor.
        location (models.CharField): The location where the course is held.
    """

    semester = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns the string representation of the course.

        Overrides the default __str__ method to return the course name.

        Returns:
            str: The name of the course.
        """
        return self.course
