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
 #--------------------------------------------------------------------   
#Calculating Total votes

heading = "Election Results"
lines = "*"*80


total_votes = len(py_poll)
ans= "Total Votes: {}".format(total_votes)

print(py_poll[0:3])
voter_set = set()
for row in py_poll:
    voter_set.add(row[2])
print(voter_set)



print("*"*80)
print("Calculating total votes for each candidate")

voter_bank={}
li_vote=0
correy_vote = 0
otooley_vote = 0
khan_vote = 0
for row in py_poll:
    if row[2]=='Khan':
        khan_vote+=1
        voter_bank['Khan']=khan_vote
    elif row[2]=='Li':
        li_vote+=1
        voter_bank['Li']=li_vote
    elif row[2]=='Correy':
        correy_vote+=1
        voter_bank['Correy']=correy_vote
    elif row[2]=="O'Tooley":
        otooley_vote+=1
        voter_bank["O'Tooley"]=otooley_vote



print(voter_bank)
voter_precent=0
s=[]

for v in voter_bank.values():
    s.append((v/total_votes)*100)

print(s)
    
khan_percent = (voter_bank['Khan']/total_votes)*100

li_percent = (voter_bank['Li']/total_votes)*100

otooley_percent = (voter_bank["O'Tooley"]/total_votes)*100

correy_percent = (voter_bank['Correy']/total_votes)*100

print(round(khan_percent,2), round(otooley_percent,2),round(li_percent,2),round(correy_percent,2))


