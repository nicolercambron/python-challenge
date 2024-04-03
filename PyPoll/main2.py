import os
import csv

# Path to collect data from the Resources folder + create text file with results
election_csv_path = os.path.join('Resources', 'election_data.csv')
output_file_path = "financial_analysis_2.txt"

#Find Total Votes

# Open the CSV file
with open(election_csv_path, 'r') as file:
    election_csv_reader = csv.reader(file)

    # Skip the header row
    next(election_csv_reader)

    # Initialize variable to store total number of cells under Ballot ID column
    ballot_count = 0

    # Iterate over each row in the CSV file
    for row in election_csv_reader:
        # Check if the row has enough cells
        if row[0]:
            # Count the cell under the Ballot ID column
            ballot_count += 1

#Make list of candidates, votes, and percentage of vote

#Dictionary
candidate_votes = {}

# Open the CSV file
with open(election_csv_path, 'r') as file:
    election_csv_reader = csv.reader(file)

# Skip the header row
    next(election_csv_reader)

    # Initialize variable to store total number of cells under Ballot ID column
    ballot_count = 0

    # Iterate over each row in the CSV file
    for row in election_csv_reader:
        # Check if the row has enough cells
        if row:
            # Count the cell under the Date column
            ballot_count += 1

            # Extract candidate name from the row in Candidate column
            candidate_name = row[2]

            # Add the candidate to the dictionary if not already present
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0

            # Increment the count for the candidate
            candidate_votes[candidate_name] += 1

#Print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {ballot_count}")
print(f"----------------------------")
for candidate, count in candidate_votes.items():
    vote_percentage = (count / ballot_count) * 100 #Percentage
    print(f"{candidate}: {vote_percentage:.3f}% ({count})")
print(f"----------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print(f"----------------------------")

#Write results to text file
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Election Results\n")
    output_file.write(f"----------------------------\n")
    output_file.write(f"Total Votes: {ballot_count}\n")
    output_file.write(f"----------------------------\n")
    for candidate, count in candidate_votes.items():
        vote_percentage = (count / ballot_count) * 100  # Calculate vote percentage for each candidate
        output_file.write(f"{candidate}: {vote_percentage:.3f}% ({count})\n")
    output_file.write(f"----------------------------\n")
    winner = max(candidate_votes, key=candidate_votes.get)
    output_file.write(f"Winner: {winner}\n")
    output_file.write(f"----------------------------\n")