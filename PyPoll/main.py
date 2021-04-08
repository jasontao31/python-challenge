import os
import csv

csvpath = os.path.join('/Users/jasonlei/python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    