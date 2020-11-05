# the dta we need to retrieve
# 1. The total number of votes
# 2. a complete list of candidates who recieved votes
# 3. The total number of votes each candidate recieved
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on the popular vote
# 
# Add our dependencies.
import csv
import os
# Assign a variable load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize atotal vote counter.
total_votes = 0

# Candidate options 
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # assign candidate names to variable
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Iterate through the candidate list.
for candidate_name in candidate_options:
    # Retrieve number of votes for a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage=float(votes)/float(total_votes) * 100
    # Print each candidate's name, vout count and percentage of votes.
    print(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if votes > winning_count:
        # If true then set winning_count=votes and winning_percent=vote_percentage
        # and winning_candidate equal to the candidate's name
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
