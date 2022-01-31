import csv

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)         

for record in customer_file:
    print(record)
    print('first name:',record[1])
    '''record is a list, put the number in the [] to select the list number'''
    print('last name:',record[2])
    print('City:',record[3])
    print('Country:',record[4])
    print('Phone:',record[5])

    input() 
    '''Waits for use to enter something'''
    




