import os
import csv

csvpath=os.path.join('Resources','election_data.csv')
candidate_count=0
total_votes=0

with open(csvpath)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)

    header=next(csvreader)
    candidate_list=[]
    candidate_count+=1
    total_votes=0
    first_candidate_votes=0
    second_candidate_votes=0
    third_candidate_votes=0


    for row in csvreader:
      if row[2] not in candidate_list:
            candidate_list+=[row[2]]
            candidate_count+=1
            total_votes+=1
      elif row[2] in candidate_list:
            candidate_count+=1
            total_votes+=1 
            
      if row[2]==candidate_list[0]:
           first_candidate_votes+=1
      elif row[2]==candidate_list[1]:
           second_candidate_votes+=1
      elif row[2]==candidate_list[2]:
            third_candidate_votes+=1

print(len(candidate_list))
candidate_votes={candidate_list[0]:first_candidate_votes,candidate_list[1]:second_candidate_votes,candidate_list[2]:third_candidate_votes}


def percent(number):
     return (number/total_votes)*100

percent_first=round(percent(first_candidate_votes),3)
percent_second=round(percent(second_candidate_votes),3)
percent_third=round(percent(third_candidate_votes),3)

print('Election Results'
      )
print("Total Votes: ",total_votes
      )

print(candidate_list[0],': ',percent_first,"%","(",first_candidate_votes,")")
print(
     candidate_list[1],': ',percent_second,"%","(",second_candidate_votes,")")
print(
     candidate_list[2],': ',percent_third,"%","(",third_candidate_votes,")"
     )

winner=max(first_candidate_votes,second_candidate_votes,third_candidate_votes)

if winner==first_candidate_votes:
      print("Winner: ",candidate_list[0])
elif winner==second_candidate_votes:
      print("Winner: ",candidate_list[1])
elif winner==third_candidate_votes:
      print("Winner: ",candidate_list[2])


