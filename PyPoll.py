#Find the total of votes cast.

#Make a complete list of candidates who received votes.

#List how many votes each candiddate recieved.

#Find percentage of votes each cadidate won.

#State the winner based on the results.

#cd Desktop/Data_Class/Class_Work/other_HW/Module3/Election_Analysis

#python3

import csv
import numpy as np
import os

file_to_load = 'election_results.csv'
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the with statement open the file as a text file.
with open(file_to_load) as elec_data:
    file_reader = csv.reader(elec_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]


#Cand.Options is an empty list. Candidate names are the third (0,1,2) 
#category in the csv. This adds any name it finds that hasn't been added
#to the empty list and adds it.

#The second part of the if statement (Cand.Votes) adds each unique name
#to a dictionary and gives each one a blank spot for votes.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
#this next line is moved out of the if statement
#so that it actually iterates through the names and counts them.
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/ float(total_votes)*100
    #!!!!! fix this from 3.4.11 so that the percentages aren't ridiculous to read
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

print(candidate_options)
print(candidate_votes)

