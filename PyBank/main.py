import os
import csv
from statistics import mean
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

convertrow = [int(row[1]) for row in bankfile]
netpl= sum(convertrow)
print(netpl)

#Avg of Change in Profit/Loss
change = convertrow[-1]-convertrow[0]
print(change)
avgchange = (change / (len(convertrow)-1))
print(avgchange)


profits = [row for row in convertrow if row>0]
losses=[row for row in convertrow if row<0]
totalprofit = sum(profits)
avgprofit = mean(profits)
totalloss = sum(losses)
avgloss = mean(losses)
print(totalprofit)
print(totalloss)
print(avgloss)
print(avgprofit)
print(avgprofit+avgloss)
