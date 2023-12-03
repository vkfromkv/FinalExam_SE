# courses/management/commands/import_courses.py
import json
from django.core.management.base import BaseCommand
from mscs_courses.course_utils import CourseDatabaseManager

class Command(BaseCommand):
    help = 'Import courses from a JSON file and save them to the database'

    def handle(self, *args, **options):
        try:
            with open('courses.json', 'r') as file:
                data = json.load(file)
                manager = CourseDatabaseManager()
                for course_info in data:
                    manager.create_course(**course_info)
            self.stdout.write(self.style.SUCCESS('Successfully imported courses'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('courses.json not found'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))
