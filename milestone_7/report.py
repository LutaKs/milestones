import csv 
import sys
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

months = {1: "january", 2 : "february", 3: "march", 4: "april", 5: "may", 6 : "june",
          7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

months_2_num = {"january": 1, "february": 2, "march" : 3, "april": 4, "may": 5, "june": 6,
                "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}

filename = sys.argv[1]
is_first = True

dep_birthdays_employees = {}
dep_anniversary_employees = {}
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if is_first:
            is_first = False
            continue
        employee = row
        birthday = datetime.datetime.strptime(employee[2], '%Y-%m-%d').date().month
        hire_date = datetime.datetime.strptime(employee[3], '%Y-%m-%d').date().month
        department = employee[0]
        if department in dep_birthdays_employees:
            if birthday in dep_birthdays_employees[department]:
                dep_birthdays_employees[department][birthday].append(employee)
            else:
                dep_birthdays_employees[department][birthday] = []
                dep_birthdays_employees[department][birthday].append(employee)
        else:
            dep_birthdays_employees[department] = {}
            dep_birthdays_employees[department][birthday] = [employee]
        
        if department in dep_anniversary_employees:
            if hire_date in dep_anniversary_employees[department]:
                dep_anniversary_employees[department][hire_date].append(employee)
            else:
                dep_anniversary_employees[department][hire_date] = []
                dep_anniversary_employees[department][hire_date].append(employee)
        else:
            dep_anniversary_employees[department] = {}
            dep_anniversary_employees[department][hire_date] = [employee]

@app.route("/birthdays", methods=['GET'])
def get_birthdays():
    if len(request.args) != 2:
        return jsonify({"Error": "wrong arguments count"}), 400
    if not ("month" in request.args) or not ("department" in request.args):
        return jsonify({"Error": "wrong arguments"}), 400  
    month = request.args['month']
    dep = request.args['department']

    m = months_2_num[month.lower()]
    if dep not in dep_birthdays_employees:
        return jsonify({}), 200
    elif m not in dep_birthdays_employees[dep]:
        return jsonify({}), 200
    
    return jsonify(dep_birthdays_employees[dep][months_2_num[month.lower()] ]), 200

@app.route("/anniversaries", methods=['GET'])
def get_anniversaries():
    if len(request.args) != 2:
        return jsonify({"Error": "wrong arguments count"}), 400
    if not ("month" in request.args) or not ("department" in request.args):
        return jsonify({"Error": "wrong arguments"}), 400

    month = request.args['month']
    dep = request.args['department']

    m = months_2_num[month.lower()]

    if dep not in dep_anniversary_employees:
        return jsonify({}), 200
    elif m not in dep_anniversary_employees[dep]:
        return jsonify({}), 200

    return jsonify(dep_anniversary_employees[dep][m]), 200

if __name__ == '__main__':
    app.run(debug=True)
