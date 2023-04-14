from unicodedata import name
from django.core.management.base import BaseCommand
from employees.models import Employee
import os
import pandas as pd


class Command(BaseCommand):
    help = 'Usage: import_employees <csv_file>'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **kwargs):

        file = kwargs['file']

        if os.path.isfile(file):
            dataset = pd.read_csv(file, header=0)

            for index, row in dataset.iterrows():
                employee = Employee(
                    firstname=row['First Name'], lastname=row['Last Name'], dob=row['Date of Birth'], salary=row['Salary'])
                employee.save()

            self.stdout.write('Successfully imported!')
