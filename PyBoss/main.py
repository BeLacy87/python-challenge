import csv
import os
import re
import itertools

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

Employee_ID=[]

name=[]
first_name=[]
last_name=[]

birthday=[]
birth_year=[]
birth_month=[]
birth_day=[]
new_date=[]
mdy=[]

SS=[]
SS_list=[]
states=[]
abbrev=[]

budget_path= os.path.join('../..' , 'employee_data.csv')
with open (budget_path, newline='') as file:
    csvreader=csv.reader(file, delimiter=',')
    next(csvreader)

    #splits main file into 5 lists
    for row in csvreader:
        Employee_ID.append(row[0])
        name.append(row[1])
        birthday.append(row[2])
        SS.append(row[3])
        states.append(row[4])

    #makes two new lists, first name and last name
    for full in name:
        first=full.split()[0]
        first_name.append(first)
        last=full.split()[1]
        last_name.append(last)

    #reassembles birthday to 'mm','dd','yyyy'
    for date in birthday:
        year=date.split("-")[0]
        birth_year.append(year)
        month=date.split("-")[1]
        birth_month.append(month)
        day=date.split("-")[2]
        birth_day.append(day)
        formated_date=str(month) + "/" + str(day) + "/" + str(year)
        mdy.append(formated_date)     
       
    #swap state names with abbreviations
    for state in states:
        abbrev.append(us_state_abbrev[state])   
        
    for number in SS:
        formated_SS='***-**-' + number[-4:]
        SS_list.append(formated_SS)
    
    report=zip(Employee_ID, first_name, last_name, mdy, SS_list, abbrev)
    print(list(report))
    

   
   
        


    
