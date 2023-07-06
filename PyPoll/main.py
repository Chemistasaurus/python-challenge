#import libraries
import os
import csv

#Establish path.
csvpath=os.path.join('Resources','election_data.csv')

#Start editing/open the csv file
with open(csvpath)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)


#Sequester the header, establish a list called candidate list, set candidate count to zero, set total votes and all candidate votes to zero
    header=next(csvreader)
    candidate_list=[]
    total_votes=0
    first_candidate_votes=0
    second_candidate_votes=0
    third_candidate_votes=0


#Start the loop. Have it check if the candidate's name is in the candidate list, if it is not, add the candidate to the list and add one to the vote count, if it is, add one to the vote counter.
    for row in csvreader:
      if row[2] not in candidate_list:
            candidate_list+=[row[2]]
            total_votes+=1
      elif row[2] in candidate_list:
            total_votes+=1 

#Start looping through the rows and compare the candidate name to the index position of the candidate and add a vote to whichever candidate's name matches.
      if row[2]==candidate_list[0]:
           first_candidate_votes+=1
      elif row[2]==candidate_list[1]:
           second_candidate_votes+=1
      elif row[2]==candidate_list[2]:
            third_candidate_votes+=1

#Count how many candidates are in the candidate list.
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
      election_winner=candidate_list[0]
elif winner==second_candidate_votes:
      print("Winner: ",candidate_list[1])
      election_winner=candidate_list[1]
elif winner==third_candidate_votes:
      print("Winner: ",candidate_list[2])
      election_winner=candidate_list[2]


with open (output_path,'w') as txtfile:
        txtfile.write(txtfile)
        txtfile.write(['Election Results'])\n
        txtfile.write(['----------------------------'])\n
        txtfile.write(['Total Votes: ', total_votes])\n
        txtfile.write(['----------------------------'])\n
        txtfile.write([candidate_list[0],': ',percent_first,'% (',first_candidate_votes,')'])\n
        txtfile.write([candidate_list[1],': ',percent_second,'% (',second_candidate_votes,')'])\n
        txtfile.write([candidate_list[2],': ',percent_third,'% (',third_candidate_votes,')'])\n
        txtfile.write(['----------------------------'])\n
        txtfile.write(["Winner: ",election_winner])\n
        txtfile.write(['----------------------------'])\n
