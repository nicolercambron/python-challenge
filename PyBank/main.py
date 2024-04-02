import os
import csv

# Path to collect data from the Resources folder + create text file with results
budget_csv_path = os.path.join('Resources', 'budget_data.csv')
output_file_path = "financial_analysis.txt"

# Open the CSV file
with open(budget_csv_path, 'r') as file:
    budget_csv_reader = csv.reader(file)

    # Skip the header row
    next(budget_csv_reader)
    
    # Initialize variable to store total number of cells under Date column
    date_count = 0

    # Iterate over each row in the CSV file
    for row in budget_csv_reader:
        # Check if the row has enough cells
        if row[0]:
            # Count the cell under the Date column
            date_count += 1

# Find Total Profit/Losses
def total_profitlosses(budget_csv):
    total = 0

    with open(budget_csv, 'r') as file:
        budget_csv_reader = csv.reader(file)
        next(budget_csv_reader)
        for row in budget_csv_reader:
            # Convert the value to integer and add it to the total
            total += int(row[1])
    
    return total

total = total_profitlosses(budget_csv_path)

#Find Average Change
with open(budget_csv_path, 'r') as file:
    budget_csv_reader = csv.reader(file)
    next(budget_csv_reader)
    
    # Initialize variables
    changes_total = 0
    previous_value = None

    for row in budget_csv_reader:
        # Check if the row has enough cells
        if len(row) > 1:
            # Convert profit/losses value to integer
            value = int(row[1])
            if previous_value is not None:
                # Calculate change from previous value
                change = value - previous_value
                # Add change to total
                changes_total += change
            # Update previous value for next iteration
            previous_value = value

# Divide the total changes by 85 (number of changes in between months)
average_change = changes_total / 85

#Find Greatest Increase + Greatest Decrease

# Initialize variables to store greatest increase, decrease, and their corresponding dates
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(budget_csv_path, 'r') as file:
    budget_csv_reader = csv.reader(file)
    next(budget_csv_reader)
    
    # Initialize variables
    previous_value = None

    for row in budget_csv_reader:
        # Check if the row has enough cells
        if len(row) > 1:
            # Convert profit/losses value to integer
            value = int(row[1])
            date = row[0]

            if previous_value is not None:
                # Calculate change from previous value
                change = value - previous_value
                
                # Check for greatest increase and decrease
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = date
                elif change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = date
                    
            # Update previous value for next iteration
            previous_value = value

#Print results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {date_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Write results to text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {date_count}\n")
    output_file.write(f"Total: ${total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")