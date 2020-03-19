#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[6]:


#open the csv path
csvpath = os.path.join('budget_data.csv')

#import the csv
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
    months=0
    revenue=0
    
    rows=[r for r in csvreader]
    
    change_revenue=int(rows[1][1])
    max = rows[1]
    min=rows[1]
    
for i in range(1,len(rows)):
        
    months=months+1
    row=rows[i]
    revenue= int(row[1]) + revenue
        
#Not include the header
    if i > 1:
        change_revenue=change_revenue + int(row[1])-int(rows[i-1][1])
        
#Find the Max Revenue
    if int(max[1]) < int(row[1]):
        max=row
        
#Find the Min Revenue
    if int(min[1]) > int(row[1]):
         min=row
#Find the average change in revenue 
average= int(revenue /months)
average_change_revenue=int(change_revenue/months)


#Print the output
print("Financial Analysis")
print("------------------")
print(f"Total Months: " + str(months))
print(f"Total Revenue: " +"$" +str(revenue))       
print(f"Average Revenue Change: " +"$"+ str(average))
print(f"Average Change in Revenue Change: " +"$"+ str(average_change_revenue))
print(f"Greatest Increase in Revenue:"  + str(max[0])+" ($" + str(max[1])+")")
print(f"Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")

#export to text file
output = open("output.txt", "w")

output.write('Financial Analysis')
output.write('\n---------------------')
output.write('-------------------------')
output.write('\nTotal Months: '+ str(months))
output.write('\nAverage Revenue Change: ' +"$"+ str(average))
output.write('\nAverage Change in Revenue Change: '+"$"+ str(average_change_revenue))
output.write('\nGreatest Increase in Revenue:'  + str(max[0])+" ($" + str(max[1])+")")
output.write('\nGreatest Decrease in Revenue:' + str(min[0])+" ($" + str(min[1])+")")





