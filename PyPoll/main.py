import os
import csv
import statistics

def pypoll(data_csv):
    file_path = os.path.join('Resources','data_csv'):
    with open(file_path,'r') as mainfile:
        py_poll = csv.reader(mainfile, delimiter=',')
        print(pypoll[0])
