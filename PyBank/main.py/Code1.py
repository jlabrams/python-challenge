#Import files
import os
import csv
csvpath = os.path.join('..''Resources', 'budget_data.csv')
with open (csvpath, newline = '') as csvfile:
 csvreader = csv.reader(csvfile, delimiter = ',')
print(csvreader)

#Create Lists
num_months = []
net_PL_total = []
PL_change = []
Average_Change = []


#Use Next function to skip over csv header labels
csv_header = next(csvreader)

#Ensure each row is read as a row
for row in csvreader:
 num_months.append(row[0])
net_PL_total.append(row[1])
Total_Profit_Losses = sum(net_PL_total)

#Total  num_months
print (len(num_months))

#Total Amount of Profit/Losses over period
#Get monthly change in profits through iteration
for i in range (len(net_PL_total)-1):
 PL_change.append (net_PL_total[i+1] - net_PL_total[i])

#Greatest Profit Increase and Greatest Profit Decrease
max_profit_increase = max(PL_change)
max_profit_decrease = min (PL_change)
x = PL_change.index(max(PL_change)) + 1
y = PL_change.index(min(PL_change)) + 1
Average_Change = {round(sum(PL_change)/len(PL_change),2)}

print ("Financial Records Analysis")
print (f'-----------------------------' + '\n')
print ("Total Number of Months:" + str(len(num_months)))
print ("Total Profit/Losses:" + str(int(Total_Profit_Losses)))
print("Average Change" + "$" + str(int[Average_Change]))
print(f"Greatest Increase in Profits: {num_months[x]} (${(str(x))})")
print(f"Greatest Decrease in Profits: {num_months[y]} (${(str(y))})")