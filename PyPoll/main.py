import csv
import os

candidates=[]
unique_list=[]
name_list=[]
percentage_list=[]
winner=0

Khan_votes=0
Correy_votes=0
Li_votes=0
OTooley_votes=0
total_votes=0
khan_percentage=0
Correy_perecentage=0
Li_percentage=0
OTooley_percentage=0


#compiles list of candidate names
def unique(candidates): 
    list_set = set(candidates) 
    unique_list = (list(list_set))
    return(unique_list)


#opens csv file
polling_path= ('election_data.csv')
with open (polling_path, newline="") as file:
    csvreader=csv.reader(file, delimiter=',')
    next(csvreader)    

#iterates through csvreader (total votes)
    for i in csvreader:
        total_votes+=1
        candidates.append(i[2])
        
        if i[2]=="O'Tooley":
            OTooley_votes+=1
            OTooley_percentage=round(((OTooley_votes/total_votes)*100.0),2)
        elif i[2]=="Li":
            Li_votes+=1
            Li_percentage=round(((Li_votes/total_votes)*100.0),2)
        elif i[2]=="Correy":
            Correy_votes+=1
            Correy_percentage=round(((Correy_votes/total_votes)*100.0),2)
        else:
            Khan_votes+=1
            Khan_percentage=round(((Khan_votes/total_votes)*100.0),2)

    name_list.append("Khan")
    percentage_list.append(Khan_percentage)
    name_list.append("Correy")
    percentage_list.append(Correy_percentage)
    name_list.append("Li")
    percentage_list.append(Li_percentage)
    name_list.append("O'Tooley")
    percentage_list.append(OTooley_percentage)

    #determines winner based on a dictionary of candidate:percentage_of_votes
    results=dict(zip(name_list, percentage_list))
    def find_winner(val):
        for key, value in results.items():
            if val == max(percentage_list):
                return key
                

    winner=find_winner(max(percentage_list))

    unique(candidates)   
    
    #print(results)
    
    print("Total votes: " + str(total_votes)) 
    print("Correy: " + str(Correy_percentage) + "%" + " (" + str(Correy_votes) + ")")
    print("Khan: " + str(Khan_percentage) + "%" + " (" + str(Khan_votes) + ")")
    print("O'Tooley: " + str(OTooley_percentage) + "%" + " (" + str(OTooley_votes) + ")")
    print("Li: " + str(Li_percentage) + "%" + " (" + str(Li_votes) + ")")
    print("Winner: " + find_winner(max(percentage_list)))

    key_list=["Total Votes", "Correy", "Khan", "O'Tooley", "Li", "Winner"]
    value_list=[total_votes, (Correy_percentage, Correy_votes), (Khan_percentage, Khan_votes), (OTooley_percentage, OTooley_votes), (Li_percentage, Li_votes), winner ]
    report=zip(key_list,value_list)
    
    output_path = os.path.join("election_results.csv")
    with open(output_path, 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Candidate", "Percentage of Votes and Total Votes"])
        writer.writerows(report)
