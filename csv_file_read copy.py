import csv

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

customersWrite = open("Customers_Country.csv","w")

count = 0

#to skip a line if the file contains a header record
next(customer_file)         

for record in customer_file:
    customersWrite.write(record[1]+","+record[2]+","+record[4]+"\n")
    count+=1

customersWrite.close()

print ("There are",count,"customers in the CSV file.")

    




