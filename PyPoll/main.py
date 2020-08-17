import os
import csv
import statistics
file_path = os.path.join('Resources','election_data.csv')
with open(file_path,'r') as mainfile:
    pypoll = csv.reader(mainfile, delimiter=',')
    header = next(pypoll)
    print(header)

    py_poll=[]
    for line in pypoll:
        py_poll.append(line)
    

print("*"*80)
print("Calculating total number of votes")

total_votes = len(py_poll)
print("Total Votes: {}".format(total_votes))