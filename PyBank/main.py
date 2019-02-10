import os
import csv

path = os.path.join('Resources', 'budget_data.csv')

with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
      
    net = 0
    biggest_increase = 0
    biggest_increase_month = ""
    biggest_decrease = 0
    biggest_decrease_month = ""
    rowvalue = 0
    lastrowvalue = 0
    change = 0
    changelist = []
    months = 0
    average_change = 0
  
    for row in csvreader:
        months += 1
        net += int(row[1])
        rowvalue = int(row[1])
        change = int(rowvalue-lastrowvalue)
        changelist.append(change)
        rowvalue = int(0)
        lastrowvalue = int(row[1])
        if biggest_increase < int(row[1]) :
            biggest_increase = int(row[1])
            biggest_increase_month = row[0]
        if biggest_decrease > int(row[1]) :
            biggest_decrease = int(row[1])
            biggest_decrease_month = row[0]

average_change = round(sum(changelist)/(len(changelist)))

print(f"Total Months: {months}")
print(f"Total: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {biggest_increase_month} (${biggest_increase})")
print(f"Greatest Decrease in Profits: {biggest_decrease_month} (${biggest_decrease})")

output = open("FinancialAnalysis.txt", "w+")
output.write(f"Total Months: {months}")
output.write(f" Total: ${net}")
output.write(f" Average Change: ${average_change}")
output.write(f" Greatest Increase in Profits: {biggest_increase_month} (${biggest_increase})")
output.write(f" Greatest Decrease in Profits: {biggest_decrease_month} (${biggest_decrease})")
output.close()

