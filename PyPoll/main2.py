import os 
import csv 

total = []
counter = 0
candidate = []
vote = []
Charles_Casper_Stockham = 0
Diana_DeGette = 0
Raymon_Anthony_Doane = 0


csvpath = os.path.join('Resources', 'election_data.csv' )
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

 
    csvheader=next(csvfile)
    for row in csvreader:
# sum of all votes 
        counter += 1
        total.append(row[0])
        if row[2] not in candidate:
            candidate.append(row[2])
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham += 1 
        Charles_Casper_Stockham_percent = (Charles_Casper_Stockham/counter) * 100
        if row[2] == "Diana DeGette":
            Diana_DeGette += 1 
        Diana_DeGette_percent = (Diana_DeGette/counter) * 100
        if row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony_Doane += 1 
        Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane/counter) * 100 



    print ("Charles Casper Stockham", Charles_Casper_Stockham, Charles_Casper_Stockham_percent,"%") 
    print ( "Diana DeGette", Diana_DeGette, Diana_DeGette_percent,"%")
    print ("Raymon Anthony Doane", Raymon_Anthony_Doane, Raymon_Anthony_Doane_percent,"%")




        


        

                    







