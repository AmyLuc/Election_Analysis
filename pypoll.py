#Import dependencies.
import csv
import numpy as np
import os

#Initialize paths to relevent files.
file_to_load = 'election_results.csv'
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Set necessary variables, lists, dictionaries, etc.
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

counties = []
county_turnout = {}
highest_turnout = 0
populous = ""
largest_percentage = 0 

#Open file with data. 
with open(file_to_load) as elec_data:
    file_reader = csv.reader(elec_data)
    headers = next(file_reader)
    #count rows for votes.
    for row in file_reader:
        total_votes += 1
        #get rows for candidates and counties
        candidate_name = row[2]
        county_name = row[1]
      

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

        if county_name not in counties:
            counties.append(county_name)
            county_turnout[county_name] = 0
        county_turnout[county_name] += 1


    #Write our results to a text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
       
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Make a list of unique counties.
    for county_name in county_turnout:
        turnout = county_turnout[county_name]
        #Find the number of votes from each country and the percentage of votes that each county
        #contributed.
        turnout_percentage = float(turnout)/ float(total_votes)* 100
        print(f"{county_name}: contributed {turnout_percentage:.1f}% to the total voter turnout")

        county_results = (f"{county_name}: {turnout_percentage:.1f}% ({turnout:,})\n")
        #Write results to a text file.
        txt_file.write(county_results)

        #Find and print county with largest voter turnout. State the numbers and percentages.
        if (turnout > highest_turnout) and (turnout_percentage > largest_percentage):
            highest_turnout = turnout
            largest_percentage = turnout_percentage
            populous = county_name
    turnout_summary = (
        f"-------------------------\n"
        f"County with largest voter turnout: {populous}\n"
        f"{populous}'s turnout: {highest_turnout:,}\n"
        f"{populous}'s contribution to total voter turnout: {largest_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(turnout_summary)

    #The code bellow does the same thing as the code above, just with the data from the candidates row,
    #instead of the counties row.
    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/ float(total_votes)*100
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

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
    txt_file.write(winning_candidate_summary)
               

print(candidate_options)
print(candidate_votes)
#Ta da!

