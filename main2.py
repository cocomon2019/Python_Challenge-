#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv

#creat the csv path
csvpath = os.path.join('election_data1.csv')


#set the variables
total_votes = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# Open the csv file and read
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    firstrow = next(csvreader)

 #Loop through the data
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

for key, value in candidates.items():
    candidates_percent[key] = round((value/total_votes)*100,2)

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

##compute results and write to output text file
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

output = open("pollresults.txt", "w")

#export the text file
output.write("Election Results \n")
output.write("------------------------------------- \n")
output.write("Total Votes: " + str(total_votes) + "\n")
output.write("------------------------------------- \n")

for key, value in candidates.items():
    output.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    output.write("------------------------------------- \n")
    output.write("Winner: " + winner + "\n")
    output.write("------------------------------------- \n")







