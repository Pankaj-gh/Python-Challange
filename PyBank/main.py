import os
import csv
from statistics import mean
file_path =os.path.join('Recources','budget_data.csv')

with open (file_path,'r') as csvfile:
    pybank = csv.reader(csvfile,delimiter=',')
    header = next(pybank)
    #print(header)
    bankfile = []

    for row in pybank:
        bankfile.append(row)
#print(bankfile[0])

#--------------------------------------------------------

#Creating textfile headers and formatting

heading=("Financial Analysis")
ans= ("-"*50)
print(heading)
print(ans)
#-------------------------------------------------------


#Calculating Total Months
months = [row[0] for row in bankfile]

ans1=("Total Months: {}".format(len(months)))
print(ans1)

#-------------------------------------------------------


#Calculating Total Amount
convertrow = [int(row[1]) for row in bankfile]
netpl= sum(convertrow)
ans2=("Total: ${}".format(netpl))
print(ans2)

#------------------------------------------------------


#Calculating Avg of Change in Profit/Loss
change = convertrow[-1]-convertrow[0]
#print(change)
avgchange = (change / (len(convertrow)-1))
ans3=('Average Change: ${}'.format(round(avgchange,2)))
print(ans3)

#------------------------------------------------------

#Calculating Greatest Increase in Profit
bankfileconverted = [[row[0],int(row[1])] for row in bankfile]      
#print(bankfileconverted)
maxprofit= max(bankfileconverted, key=lambda y:y[1])
#print(maxprofit)
y = maxprofit[1]                                                    
#print(y)
ind=0

for i in range(len(convertrow)):                                    
    if convertrow[i]==y:
        #print(ind)
        break
    else:
        ind+=1





greatest_profit_increase = convertrow[ind]-convertrow[ind-1]
ans4=("Greatest Increase in Profits: " + bankfileconverted[ind][0] + " (${})".format(greatest_profit_increase))
print(ans4)

#-------------------------------------------------------
#Calclulating Decrease in Profits
maxloss= min(bankfileconverted,key=lambda z:z[1])
z=maxloss[1]

lossind = 0

for i in range(len(convertrow)):
    if convertrow[i]==z:
        #print(lossind)
        break
    else:
        lossind+=1

greatest_profit_decrease = convertrow[lossind]-convertrow[lossind-1]
ans5=("Greatest Decrease in Profits: " + bankfileconverted[lossind][0] + " (${})".format(greatest_profit_decrease))
print(ans5)

#------------------------------------------------------------

#Adding All Solutions to a single variable


txtfile = ("{} \n{} \n \n {} \n {} \n {} \n {} \n {}".format(heading,ans,ans1,ans2,ans3,ans4,ans5,))

print(txtfile)

#----------------------------------------------------------

#Writing to .txt file and exporting to the appropriate location


txt_path = os.path.join("Analysis","Pybank_Results.txt")
with open(txt_path,'w') as f:
    f.write(txtfile)


