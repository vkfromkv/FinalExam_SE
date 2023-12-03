from django.db import IntegrityError
from mscs_courses.models import Course

class CourseDatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.setup()
        return cls._instance

    def setup(self):
        pass

    def create_course(self, semester, course, instructor, location):
        try:
            Course.objects.create(semester=semester, course=course, instructor=instructor, location=location)
        except IntegrityError:
            # Handle duplicate course if needed
            pass

    def get_courses(self):
        return Course.objects.all()