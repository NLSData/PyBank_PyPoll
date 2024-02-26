import csv
import os 

# This dictionary will store our candidates and their vote count
candidate_votes = {}

# This is where my csv path is located.
INPUT_CSV_PATH = os.path.join("Resources", "election_data.csv")
# This is where my output file is located.
OUTPUT_TXT_PATH = os.path.join("analysis", "PyPoll_output.txt")
# Change directory to where this file is. 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Now that we are in the Pypoll directory, we need to open election_data
with open(INPUT_CSV_PATH) as csv_file:
    # Open the csv and skip the header
    # The first row of the csv is the header. The next() function
    #  will read the header and move to the next row. 
    csv_reader= csv.reader(csv_file)                          
    Header = next(csv_reader)

 # Start iterating through the rest of the rows
    for row in csv_reader:
        name = row[2]
        if name in candidate_votes:
            # We've already seen this candidate, so add 1 to the vote count
            candidate_votes[name] = candidate_votes[name] + 1
        else:
            # New candidate, add to dict and assign "1" vote
            candidate_votes[name] = 1


# This variable will store the total number of votes
total_votes = 0

# These variables will be for identifying the winner (candidate with most votes)
max_known_votes = 0
max_known_candidate = None

# Iterate through dict and calculate total votes, as well as winner
for candidate, votes in candidate_votes.items():
    total_votes = total_votes + votes
    if votes > max_known_votes:
        max_known_votes = votes
        max_known_candidate = candidate

print ("Election Results")
print ("-----------------------")
print(f'Total Votes: {total_votes}') 
print ("-----------------------")

for candidate, votes in candidate_votes.items():
    percentage_votes = round(votes / total_votes * 100, 3)
    print(f'{candidate}: {percentage_votes}% ({votes})')

   
print ("-----------------------")
print(f'Winner: {max_known_candidate}')

print ("-----------------------")

# The function below will export to a text file 
with open(OUTPUT_TXT_PATH, 'w') as file:
    # Write the results to the file

    file.write ("Election Results\n")
    file.write ("-----------------------\n")
    file.write (f'Total Votes: {total_votes}\n')

    for candidate, votes in candidate_votes.items():
        percentage_votes = round(votes / total_votes * 100, 3)
        file.write(f'{candidate}: {percentage_votes}% ({votes})\n')
       


    file.write ("-----------------------\n")
    file.write (f'Winner: {max_known_candidate}\n')
    file.write ("-----------------------")