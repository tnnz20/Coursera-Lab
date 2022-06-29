import csv
import os

path = os.path.join(os.path.dirname(__file__), 'employees.csv')
with open(path) as f:
    reader = csv.reader(f)
    for data in reader:
        print(data)