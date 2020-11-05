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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)