
from faker import Faker
from faker.providers import DynamicProvider
import datetime
import csv 

fake = Faker()
employees = []
personal_sount = 500

Faker.seed(0)

departments_provider = DynamicProvider(
     provider_name="departments",
     elements=["HR", "Finance", "Engineering", "R&D"],
)
fake.add_provider(departments_provider)

d = datetime.date(2020, 12, 25)
for _ in range(personal_sount):
    employee = {}
    employee['dep'] = fake.departments()
    employee['name'] = fake.unique.name()
    employee['birthday'] = fake.date_of_birth(minimum_age = 19, maximum_age = 65)
    employee['hire_date'] = fake.date_between_dates(date_start = d)
    employees.append(employee)

filename = input("Enter filename: ")
filename += ".csv"

with open (filename , mode='w') as file:
    employee_info = ['dep', 'name', 'birthday', 'hire_date']
    writer = csv.DictWriter(file, fieldnames=employee_info)
    writer.writeheader()
    for employee in employees:
        writer.writerow(employee)







