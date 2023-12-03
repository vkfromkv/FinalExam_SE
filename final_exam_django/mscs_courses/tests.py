from django.test import TestCase
from .models import Course
import json

class CourseImportTest(TestCase):
    """
    A TestCase class for testing the import of course data from a JSON file into the Course model.

    This test class includes methods to load data from a JSON file, create course objects,
    and run specific tests to verify the correctness of data import and object creation.
    """

    def load_data_from_json(self):
        """
        Loads course data from a JSON file.

        Opens the 'courses.json' file and loads its content to be used in tests.

        Returns:
            list: A list of dictionaries, each representing a course.
        """
        json_file_path = 'courses.json'
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)

    def create_course_objects(self, data):
        """
        Creates Course objects from the provided data.

        Iterates over the data list, creating a Course object for each entry.

        Args:
            data (list): A list of dictionaries, each containing course information.
        """
        for item in data:
            Course.objects.create(
                semester=item["semester"],
                course=item["course"],
                instructor=item["instructor"],
                location=item["location"]
            )

    def setUp(self):
        """
        Setup method for the test case.

        Called before each test method. It loads the JSON data to be used in the tests.
        """
        self.json_data = self.load_data_from_json()

    def test_import_from_json(self):
        """
        Test method to verify correct import from JSON.

        Creates Course objects using the JSON data and then checks if the number
        of Course objects created matches the expected count. Also verifies the attributes
        of a specific Course object.
        """
        self.create_course_objects(self.json_data)
        expected_count = len(self.json_data)
        actual_count = Course.objects.count()
        self.assertEqual(actual_count, expected_count)

        course = Course.objects.get(course="ACS 560")
       
