import csv 
import sys
import datetime

months = {1: "january", 2 : "february", 3: "march", 4: "april", 5: "may", 6 : "june",
          7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

filename = sys.argv[1]
month = sys.argv[2]

verbose = False
if len(sys.argv) == 4:
    if sys.argv[3] == '-v':
        verbose = True

birthday_dict = {}
anniversary_dict = {}
total_birthday = 0
total_anniversary = 0
is_first = True
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if not is_first:
            employee = row
            birthday = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            hire_date = datetime.datetime.strptime(row[3], '%Y-%m-%d').date()

            if months[birthday.month] == month.lower():
                total_birthday += 1
                if employee[0] in birthday_dict:
                    birthday_dict[employee[0]].append(employee[1])
                else:
                    birthday_dict[employee[0]] = [employee[1]]

            if months[hire_date.month] == month.lower():
                total_anniversary += 1
                if employee[0] in anniversary_dict:
                    anniversary_dict[employee[0]].append(employee[1])
                else:
                    anniversary_dict[employee[0]] = [employee[1]]
        is_first = False


result = f'python report.py {filename} {month}\n\
Report for {month} generated\n\
--- Birthdays ---\n\
Total: {total_birthday}\n\
By department:\n'

for dep in birthday_dict:
    result += f'- {dep}: {len(birthday_dict[dep])}\n'
    if verbose:
        result += f'Names: {birthday_dict[dep]}\n'

result += f'--- Anniversaries ---\n \
Total: {total_anniversary} \
By department:\n'
for dep in anniversary_dict:
    result += f'- {dep}: {len(anniversary_dict[dep])}\n'
    if verbose:
        result += f'Names: {anniversary_dict[dep]}\n'

print(result)
