import csv
import os

candidates=[]
unique_list=[]

Khan_votes=0
Correy_votes=0
Li_votes=0
OTooley_votes=0
total_votes=0

#compiles list of candidate names
def unique(candidates): 
    list_set = set(candidates) 
    unique_list = (list(list_set))
    print(unique_list)

#opens csv file
polling_path= ('election_data.csv')
with open (polling_path, newline='') as file:
    csvreader=csv.reader(file, delimiter=',')
    next(csvreader)    

#iterates through csvreader (total votes)
    for i in csvreader:
        total_votes+=1
        candidates.append(i[2])
        


        if i[2]=="O'Tooley":
            OTooley_votes+=1
        elif i[2]=="Li":
            Li_votes+=1
        elif i[2]=="Correy":
            Correy_votes+=1
        else:
            Khan_votes+=1

    unique(candidates)
    print(total_votes)    
    print("Correy: " + str(Correy_votes))
    print("Khan: " + str(Khan_votes))
    print("O'Tooley: " + str(OTooley_votes))
    print("Li: " + str(Li_votes))