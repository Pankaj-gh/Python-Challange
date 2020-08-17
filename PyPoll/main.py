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
    
#Calculating Total votes
print("*"*80)
print("Calculating total number of votes")

total_votes = len(py_poll)
print("Total Votes: {}".format(total_votes))

print(py_poll[0:3])
voter_set = set()
for row in py_poll:
    voter_set.add(row[2])
print(voter_set)



print("*"*80)
print("Calculating total votes for each candidate")
li = 0
correy = 0
otooley = 0
khan = 0

for row in py_poll:
    if row[2] == 'Khan':
        khan+=1
    elif row[2]=='Li':
        li+=1
    elif row[2]=='Correy':

        correy+=1
    elif row[2]=="O'Tooley":
        otooley +=1
print(li,correy,otooley,khan)