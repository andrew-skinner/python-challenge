import os
import csv

path = os.path.join('Resources', 'election_data.csv')

with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        #//empty dictionary to put all candidates in
    #candidates = set()
    #//Go through each row of the csv to determine who received votes
    #for row in csvreader:
       #candidates.add(row[2])    
    #print(f"candidates receiving votes were: {candidates}   ")
    #based on output create variables
    totalvotes = 0
    can1 = "Khan"
    can2 = "Li"
    can3 = "O'Tooley"
    can4 = "Correy"
    khan = 0
    li = 0
    otooley = 0
    correy = 0
    for row in csvreader:
        totalvotes += 1
        if row[2] == can1:
            khan += 1
        elif row[2] == can2:
            li += 1
        elif row[2] == can3:
            otooley += 1
        elif row[2] == can4:
            correy =+ 1
    can1percent = round(((khan/totalvotes)*100),3)
    can2percent = round(((li/totalvotes)*100), 3)
    can3percent = round(((otooley/totalvotes)*100), 3)
    can4percent = round(((correy/totalvotes)*100), 3)
    if khan > li and khan > otooley and khan> correy:
        winner = can1
    elif li > khan and li > otooley and li > correy:
        winner = can2
    elif otooley > khan and otooley > li and otooley > correy:
        winner = can3
    elif correy > khan and correy > li and correy > otooley:
        winner = can4

    print(f"Total Votes: {totalvotes}   ")
    print(f"THE RESULTS ARE IN!!!! *Khan:({can1percent}%) with {khan} votes, Li:({can2percent}%) with {li} votes, O'Tooley:({can3percent}%) with {otooley} votes, Correy:({can4percent}%) with {correy} votes.")
    print(f"Winner: {winner}")
    output = open("PollResults.txt", "w+")
    output.write(f"THE RESULTS ARE IN!!!! *Khan:({can1percent}%) with {khan} votes, Li:({can2percent}%) with {li} votes, O'Tooley:({can3percent}%) with {otooley} votes, Correy:({can4percent}%) with {correy} votes.")
    output.write(f"Winner: {winner}")
