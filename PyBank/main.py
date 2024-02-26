import csv
import os  

# This is where my csv path is located. For example: Resources/budget_data/csv
INPUT_CSV_PATH = os.path.join("Resources", "budget_data.csv")
#This is where my output file is located.
OUTPUT_TXT_PATH = os.path.join("analysis", "PyBank_output.txt")

# This list will keep track of all of the months we've seen
month_years = []
net_total = 0
previous_profit_loss = None
total_changes = 0

greatest_change = None
greatest_change_month = None
lowest_change = None
lowest_change_month = None

# Change directory to where this file is. For example: 
# /Users/yongeunleeson/Desktop/bootcamp-repos/github/PyBank_PyPoll/PyBank
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Now that we are in the PyBank directory, we need to open budget_data
# in the Resources file. We can do this via open("Resources/budget_data.csv")
with open(INPUT_CSV_PATH) as csv_file:

    # Create an object to help us read a csv file
    csv_reader= csv.reader(csv_file)
    
    # The first row of the csv is the header. The next() function
    #  will read the header and move to the next row. 
    Header = next(csv_reader)

    # Start iterating through the rest of the rows
    for row in csv_reader:
        current_month_year = row[0]
        current_profit_loss = int(row[1])

        # Task 1: The total number of months included in the dataset
        # We will store all of the months in month_years and count
        # them at the end.  We will also check to see if there are duplicates.
        # We can check if we've seen the month_year before adding it
        # to our list with this "if" statement
        if current_month_year not in month_years:
            month_years.append(current_month_year)

        # Task 2: The net total amount of "Profit/Losses" over the entire period
        net_total = net_total + current_profit_loss

        # Task 3: The changes in "Profit/Losses" over the entire period, and then the average of those changes
        # Calculate the change from month to month (current_change). Add all changes together (total_changes)
        # and divide by the total number of changes (len(month_years)).
        
        # We check if previous_profit_loss is None. If so, we are on the first row and skip this logic
        #I found the none logic on Google.
        if previous_profit_loss is not None:
            current_change = current_profit_loss - previous_profit_loss
            total_changes = total_changes + current_change

            # Task 4: The greatest increase in profits (date and amount) over the entire period
            if greatest_change is None or current_change > greatest_change:
                greatest_change = current_change
                greatest_change_month = current_month_year
            
            # Task 5: The greatest decrease in profits (date and amount) over the entire period
            if lowest_change is None or current_change < lowest_change:
                lowest_change = current_change
                lowest_change_month = current_month_year

        # Update previous_profit_loss so we can compare it with the next row
        previous_profit_loss = current_profit_loss
        
        

print ("Financial Analysis")
print ("-----------------------")
print(f"Total Months: {len(month_years)}")
print(f"Total: ${net_total}")
print(f'Average Change: ${   round( total_changes   /  (len (month_years) - 1 ) , 2 )     }')
print(f'Greatest Increase in Profits: {greatest_change_month} (${greatest_change})')
print(f'Greatest Decrease in Profits: {lowest_change_month} (${lowest_change})')

# The function below will export to a text file 
with open(OUTPUT_TXT_PATH, 'w') as file:
    # Write the results to the file
    # I learned how to export to text file on chatGPT
    file.write ("Financial Analysis\n")
    file.write ("-----------------------\n")
    file.write (f"Total Months: {len(month_years)}\n")
    file.write (f"Total: ${net_total}\n")
    file.write (f'Average Change: ${   round( total_changes   /  (len (month_years) - 1 ) , 2 )     }\n')
    file.write (f'Greatest Increase in Profits: {greatest_change_month} (${greatest_change})\n')
    file.write (f'Greatest Decrease in Profits: {lowest_change_month} (${lowest_change})')
    
