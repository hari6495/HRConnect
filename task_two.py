"""
To get "HIRE DATE" of employee who's department is within range (30 - 110) AND who's salary is >4200
"""
from pprint import pprint
from my_utils.csv_operations import HandleCSV
from my_utils.date_converter import convert_date


def do_task_two():
    emp_details = {}  # to store hire date and name of employees
    for emp in HandleCSV.read_csv_line_by_line():
        # pulls details of each employee in csv file
        if int(emp["DEPARTMENT_ID"]) in range(30, 111) and int(emp["SALARY"]) > 4200:
            hire_date = convert_date(emp["HIRE_DATE"])  # converts date into "YYYY-MM-DD" format
            name = emp.get("FIRST_NAME") + " " + emp.get("LAST_NAME")
            if emp_details.get(hire_date) is None:
                # if employee is not in dictionary makes new entry
                emp_details.setdefault(hire_date, [name])
            else:
                # if employee exists, appends name
                emp_details[hire_date].append(name)

    return emp_details