from django.db import IntegrityError
from mscs_courses.models import Course

class CourseDatabaseManager:
    """
    A singleton class to manage database operations for the Course model.

    This class ensures that only one instance is created (Singleton pattern) 
    and provides methods to create and retrieve course records.

    Attributes:
        _instance (CourseDatabaseManager): A private class attribute to hold the singleton instance.
    """

    _instance = None

    def __new__(cls):
        """
        Overrides the default behavior of instance creation.
        Ensures that only one instance of CourseDatabaseManager exists.

        Returns:
            CourseDatabaseManager: The singleton instance of the class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.setup()
        return cls._instance

    def setup(self):
        """
        A setup method for the singleton instance.
        Currently, it performs no operation but can be used for initialization.
        """
        pass

    def create_course(self, semester, course, instructor, location):
        """
        Creates a new course record in the database.

        Args:
            semester (str): The semester for the course.
            course (str): The name of the course.
            instructor (str): The name of the instructor.
            location (str): The location where the course is held.

        Returns:
            None: The method does not return anything. It either successfully creates a course
                  or silently handles an IntegrityError in case of a duplicate record.
        """
        try:
            Course.objects.create(semester=semester, course=course, instructor=instructor, location=location)
        except IntegrityError:
            # To Handle duplicate course if needed
            pass

    def get_courses(self):
        """
        Retrieves all course records from the database.

        Returns:
            QuerySet: A Django QuerySet containing all Course instances.
        """
        return Course.objects.all()
