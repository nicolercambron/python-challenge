# python-challenge
Module 3

Source: ChatGPT -
(PyBank)
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

(PyPoll)
Pseudocode under "#Make list of candidates, votes, and percentage of vote" to give a skeleton of how to create code
