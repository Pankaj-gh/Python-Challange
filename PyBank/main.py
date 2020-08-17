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
#print(netpl)

#Avg of Change in Profit/Loss
change = convertrow[-1]-convertrow[0]
#print(change)
avgchange = (change / (len(convertrow)-1))
print(avgchange)


#convert to int for bankfile
bankfileconverted = [[row[0],int(row[1])] for row in bankfile]
print(bankfileconverted)
maxprofit= max(bankfileconverted, key=lambda y:y[1])
print(maxprofit)
print(y)
ind=0
#finding index value of maxprofit
for i in range(len(convertrow)):
    if convertrow[i]==y:
        print(ind)
        break
    else:
        ind+=1

#print(bankfileconverted[ind])

#calculating greatest increase in profit from ind and ind-1

greatest_profit_increase = convertrow[ind]-convertrow[ind-1]
print("Greatest Increase in Profits: " + bankfileconverted[ind][0] + " (${})".format(greatest_profit_increase))

#Calclulate greatest loss

maxloss= min(bankfileconverted,key=lambda z:z[1])
print(maxloss)

print(z)
lossind = 0

for i in range(len(convertrow)):
    if convertrow[i]==z:
        print(lossind)
        break
    else:
        lossind+=1

print(bankfileconverted[lossind])

greatest_profit_decrease = convertrow[lossind]-convertrow[lossind-1]
print("Greatest Decrease in Profits: " + bankfileconverted[lossind][0] + " (${})".format(greatest_profit_decrease))



