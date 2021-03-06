#import modules 
import os
import csv

#set path to open file
Pybank = os.path.join("bank.csv")

#set the variables
month_count = 0
total_profit = 0
value = 0
change = 0
dates = []
profits = []


#Open and reading the CSV file
with open(Pybank) as csvfile:
    csvreader = csv.reader(csvfile)

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row 
    first_row = next(csvreader)
    month_count += 1
    total_profit += int(first_row[1])
    value = int(first_row[1])
    
    #go through the rows 
    for row in csvreader:
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        #profits.append(change)
        value = int(row[1])
        dates +=[row[0]]
        
        #Total number of months
        month_count += 1

        #Total net amount of Profit/Losses
        #total_profit = total_profit + int(row[1])
        profits += [change]

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in profits/losses"
    avg_change = sum(profits)/len(profits)
    

#Print information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: ${str(total_profit)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


write_file = f"financial_analysis2.txt"
filewriter = open(write_file, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("---------------------\n")
filewriter.write(f"Total Months: {str(month_count)}\n")
filewriter.write(f"Total: ${str(total_profit)}\n")
filewriter.write(f"Average Change: ${str(round(avg_change,2))}\n")
filewriter.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n")
filewriter.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\n")

#close file
filewriter.close()