import os
import csv
file_path =os.path.join('Recources','budget_data.csv')

with open (file_path,'r') as csvfile:
    pybank = csv.reader(csvfile,delimiter=',')
    header = next(pybank)
    print(header)
    bankfile = []

    for row in pybank:
        bankfile.append(row)
print(bankfile)


#Total Months

months = [row[0] for row in bankfile]
print(len(months))

#Net Profit/Loss

pl= [(row[1]) for row in bankfile]
print(sum(pl))

