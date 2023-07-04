#import the os and csv modules.

import os
import csv

#Set the path for the csv
csvpath=os.path.join('Resources','budget_data.csv')
column_count=0
total_net=0
change_net=[]
max_profit=0
max_loss=0
#open the csv and read the data
with open(csvpath)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)

    header=next(csvreader)
    first_row=next(csvreader)

    column_count+=1
    total_net+=int(first_row[1])
    print(first_row[1])
    initial_net=int(first_row[1])
    for row in csvreader:
        column_count+=1
        total_net+=int(row[1])
        change_profit=int(row[1])-initial_net
        if change_profit > max_profit:
            max_profit=change_profit
            max_profit_id=row[0]
        elif change_profit < max_loss:
            max_loss=change_profit
            max_loss_id=row[0]
      
    
        initial_net=int(row[1])
        change_net+=[change_profit]

print(change_net)
print("Total: $",total_net)
sum_change=sum(change_net)
print("sum change ",sum_change)
print("column count ",column_count)
change_columns=column_count-1
average_change=sum_change//change_columns
print(average_change)

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

output_path=os.path.join('Resources','budget_data_stats.csv')
with open (output_path,'w') as csvfile:
        csvwriter=csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Total Months', column_count])
        csvwriter.writerow(['Total', total_net])
        csvwriter.writerow(['Average Change',average_change])
        csvwriter.writerow(['Greatest Increase in Profits',max_profit_id,max_profit])
        csvwriter.writerow(['Greatest Decrease in Profits',max_loss_id,max_loss])
