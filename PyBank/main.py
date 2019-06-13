# Dependencies
import os
import csv

# File to load
csvpath = os.path.join('..', 'PythonHome', 'budget.csv')

# Output
output_path = os.path.join('..', 'PythonHome', 'bank.txt')

# To open and read file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvreader)

# Variables to track
    total_months = 0
    total_revenue = 0
    prev_revenue = 0
    revenue_change = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999]
    revenue_changes = []

    for row in csvreader:
# Calculate total months
        total_months = total_months + 1 
# Calculate the total revenue (profit/losses in over the entire period)
        total_revenue = total_revenue + int(row[1]) 
# Keep track of changes
        revenue_change = int(row[1]) - prev_revenue


# Reset the value of prev_revenue to the row where analysis was performed
        prev_revenue = int(row[1])

# Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]

# Add to the revenue_changes list
        revenue_changes.append(int(row[1]))

# Set the revenue_avg
        revenue_avg = sum(revenue_changes) / len(revenue_changes)

# Output
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

with open(output_path, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
