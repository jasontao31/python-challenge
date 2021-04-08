import os
import csv

csvpath = os.path.join('/Users/jasonlei/election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

    khan_percent = (khan/total_votes) * 100
    correy_percent = (correy/total_votes) * 100
    li_percent = (li/total_votes) * 100
    otooley_percent = (otooley/total_votes) * 100

    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    elif otooley_percent > max(khan_percent, li_percent, correy_percent):
        winner = "O'Tooley"

output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"Khan: {khan_percent:.3f}% ({khan})\n"
    f"Correy: {correy_percent:.3f}% ({correy})\n"
    f"Li: {li_percent:.3f}% ({correy})\n"
    f"O'Tooley: {otooley_percent:.3f}% ({otooley})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

print(output)
    
results_output = os.path.join('/Users/jasonlei/python-challenge/PyPoll/Analysis/election_result.txt')
with open(results_output, "w") as txt_file:
    for result in output:
        txt_file.write(result)
    

