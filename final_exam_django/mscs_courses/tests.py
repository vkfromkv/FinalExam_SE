from django.test import TestCase
from  .models import Course  # Import your Course model
import json

class CourseImportTest(TestCase):
    def load_data_from_json(self):
        # Define the path to your courses.json file
        json_file_path = 'courses.json'

        # Open and read the JSON file
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)

    def create_course_objects(self, data):
        # Create Course objects from JSON data
        for item in data:
            Course.objects.create(
                semester=item["semester"],
                course=item["course"],
                instructor=item["instructor"],
                location=item["location"]
            )

    def setUp(self):
        self.json_data = self.load_data_from_json()

    def test_import_from_json(self):
        self.create_course_objects(self.json_data)

        # Check if the correct number of Course objects were created
        expected_count = len(self.json_data)
        actual_count = Course.objects.count()
        self.assertEqual(actual_count, expected_count)

        # Check the attributes of a specific Course object
        course = Course.objects.get(course="ACS 560")
        self.assertEqual(course.semester, "Fall 2023")
        self.assertEqual(course.instructor, "Parker, Matthew")
        self.assertEqual(course.location, "KT 246")

    def test_another_import(self):
        self.create_course_objects(self.json_data)

        # Check if the correct number of Course objects were created
        expected_count = len(self.json_data)  # Example: Creating duplicates
        actual_count = Course.objects.count()
        self.assertEqual(actual_count, expected_count)

        # Check the attributes of another specific Course object
        course = Course.objects.get(course="ACS 545")
        self.assertEqual(course.semester, "Spring 2024")
        self.assertEqual(course.instructor, "Chen, Zesheng")
        self.assertEqual(course.location, "ET 112")

    # Add more test methods as needed for other scenarios
