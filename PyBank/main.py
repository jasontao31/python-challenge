import os
import csv

csvpath = os.path.join('/Users/jasonlei/python-challenge/PyBank/Resources/budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_month = []
    total_profit = []
    monthly_change = []

    for row in csvreader:
        total_month.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):
        monthly_change.append(int(total_profit[i+1])-int(total_profit[i]))

max_increase = max(monthly_change)
max_month = monthly_change.index(max(monthly_change)) + 1

max_decrease = min(monthly_change)
min_month = monthly_change.index(min(monthly_change)) + 1

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(total_month)}\n"
    f"Total: ${sum(total_profit)}\n"
    f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}\n"
    f"Greatest Increase in Profits: {total_month[max_month]} (${(str(max_increase))})\n"
    f"Greatest Decrease in Profits: {total_month[min_month]} (${(str(max_decrease))})\n")

print(output)

results_output = os.path.join('/Users/jasonlei/python-challenge/PyBank/Analysis/Bank_result.txt')
with open(results_output, "w") as txt_file:
    for result in output:
        txt_file.write(result)

