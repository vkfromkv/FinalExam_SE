import json
from django.core.management.base import BaseCommand
from mscs_courses.course_utils import CourseDatabaseManager

class Command(BaseCommand):
    """
    Django management command to import courses from a JSON file into the database.

    This command reads course data from a 'courses.json' file and uses the CourseDatabaseManager
    to create course records in the database. It is intended to be run as a Django management command.

    Attributes:
        help (str): A brief description of the command.
    """

    help = 'Import courses from a JSON file and save them to the database'

    def handle(self, *args, **options):
        """
        The main method that gets called when the command is executed.

        It reads the course data from 'courses.json', creates an instance of CourseDatabaseManager,
        and then iterates over the data to create course records.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments.

        Outputs:
            Writes success or error messages to stdout or stderr.
        """
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
