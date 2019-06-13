# Dependancies
import os
import csv

from collections import OrderedDict
from operator import itemgetter

# To load
csvpath = os.path.join('..', 'PythonHome', 'election_data.csv')

# Output:
output_path = os.path.join('..', 'PythonHome', 'results.txt')

# Variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
 
# Determine total number of votes cast by getting the list of candidates and votes received    
    for row in csvreader:
        votes = votes + 1
        total_candidates = row[2] 
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
             
# Percentage
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

# Outcome
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

# Output Files
with open(output_path, "w") as txt_file:  
    txt_file.write("Election Results")
    txt_file.write("\n")    
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")    
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
