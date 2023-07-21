import os 
import csv 

csvpath = os.path.join('Resources', 'budget_data.csv' )

date = []
profit_losses = []
counter = 0
total = 0
list = []
greatest_increase=["",-9999]
greatest_decrease=["",0]
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

    csvheader=next(csvfile)
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    
    for row in csvreader:

    #total number of months in dataset 
        counter += 1
        date.append(row[0])
        print("total months",counter)
    #net total amount of Profit/losses 
        total += int(row[1])
        #total.append(row[1])
        profit_losses.append(row[1])
        print("Total",total)
        print(profit_losses)

    #change in profit/losses and average of changes 
         
       # average += average(row[1])
        #average.append(row[1])
        netchange = int(row[1]) - prev_net
        print(netchange)
        list.append(netchange)
        if netchange > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=netchange
        if  netchange < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=netchange  
print(greatest_increase)
print(greatest_decrease)
average = sum(list) / len(list)
print(average)

   



 
   