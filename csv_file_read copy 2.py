import csv

employees = open('EmployeePay.csv','r')

employee_file = csv.reader(employees, delimiter=',')

employeesWrite = open("EmployeePayWithBonus.csv","w")

count = 0

#to skip a line if the file contains a header record
next(employee_file)         

for record in employee_file:
    salary = float(record[3])
    bonus = float(record[4])+1
    overallSalary = str(format((salary*bonus),".2f"))
    employeesWrite.write(record[1]+","+record[2]+","+overallSalary+"\n")

employeesWrite.close()





