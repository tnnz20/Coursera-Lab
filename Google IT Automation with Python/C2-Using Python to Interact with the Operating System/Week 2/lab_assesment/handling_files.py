#!/usr/bin/env python3

import csv
import os

def read_employees(csv_file_location):
    with open(csv_file_location) as f:
        # register dialect
        # dialect use to create key of dictionary
        # by first row
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(f, dialect='empDialect')
        
        # add dictionary into a list
        employee_list = []
        for data in employee_file:
            employee_list.append(data)
    
    return employee_list

# Count department exists
def process_data(employee_list):
    department_list = []

    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    
    return department_data

# Create file
def write_report(dictionary, report_file):
    with open(report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()
    


# Create current path with this file exist
path = os.path.dirname(__file__)

employee_list = read_employees(os.path.join(path, 'employees.csv'))
# print(employee_list) 

dictionary = process_data(employee_list)
# print(dictionary)

write_report(dictionary, os.path.join(path, 'report.txt'))
