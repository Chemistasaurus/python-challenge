#import the os and csv modules.

import os
import csv

#Set the path for the csv
csvpath=os.path.join('Resources','budget_data.csv')

#Set variables for Column Count (the number of months) and the total profits.
column_count=0
total_net=0

#Start a list for the net change from month to month.
change_net=[]

#Set variables for greatest profit increase and greatest profit decrease to zero, so we have something to compare the change values to.
max_profit=0
max_loss=0

#open the csv and read the data
with open(csvpath)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

#Separate out the header and the first row we want to start with.
    header=next(csvreader)
    first_row=next(csvreader)

#Have the column count and total profit start with the first row values.
    column_count+=1
    total_net+=int(first_row[1])

#Define and store a variable with the profit for the first row so that we can calculate the change in profit. 
#The first row would not have a change, since there is no month to compare it to.
    initial_net=int(first_row[1])

#Start looping through each row and add 1 to column count, add the profit value to the total, and calculate the profit change from the previous value.
    for row in csvreader:
        column_count+=1
        total_net+=int(row[1])
        change_profit=int(row[1])-initial_net

#Compare the change in profit to the previous highest profit change and store the month, year, and profit change if the current value is the new highest profit change.        
        if change_profit > max_profit:
            max_profit=change_profit
            max_profit_id=row[0]

#If the values is not the highest profit change, do the same check, but with the highest loss and store the respective values for highest loss.
        elif change_profit < max_loss:
            max_loss=change_profit
            max_loss_id=row[0]
      
#Replace the previous initial net value with the current value before moving to the next row.    
        initial_net=int(row[1])

#Add the current row's change in profit to the running total of the change in profit, so we get the total and calculate the average later.
        change_net+=[change_profit]

#Find the sum of the profit changes.
sum_change=sum(change_net)

#Define new variable for the number of values in the change net list which is the number of profit changes calculated which is the number of months, minus one.
change_columns=column_count-1

#Calculate the average profit change by taking the total profit change and dividing it by the number of values in the change net list.
average_change=sum_change//change_columns


#printing everything in the order it asked for it.
print("Financial Analysis"
      
      "----------------------------")
      
print("Total Months: ", column_count)

print("Total: $",total_net)

print("Average Change : $", average_change)
#greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ",max_profit_id,"($",max_profit,")")

#greatest decrease in profits (date and amount) over the entire period.
print("Greatest Decrease in Profits: ",max_loss_id,"($",max_loss,")")

#Set the output path for the new file.
output_path=os.path.join('Analysis','Analysis.txt')

#Keeping the file open, write the data into the txt file.
with open (output_path,'w') as txtfile:
        txtfile.write('Financial Analysis') 
        txtfile.write('\n')
        txtfile.write('----------------------------')
        txtfile.write('\n')
        txtfile.write('Total Months: ')
        txtfile.write(str(column_count))
        txtfile.write('\n')
        txtfile.write('Total: ')
        txtfile.write(str(total_net))
        txtfile.write('\n')
        txtfile.write('Average Change: ')
        txtfile.write(str(average_change))
        txtfile.write('\n')
        txtfile.write('Greatest Increase in Profits: ')
        txtfile.write(str(max_profit_id))
        txtfile.write(' ')
        txtfile.write(str(max_profit))
        txtfile.write('\n')
        txtfile.write('Greatest Decrease in Profits: ')
        txtfile.write(str(max_loss_id))
        txtfile.write(' ')
        txtfile.write(str(max_loss))
