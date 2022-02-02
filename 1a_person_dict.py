person = {}
person['fname'] = 'Joe'
person['lname'] = 'Fonebone' 
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey'] #A dictionary can be a  collection of lists
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'} #or a collection of dictionaries



#How to get it to print Joey in the Children list
print(person)

print(type(person['children']))


print(person['children'][2])

#Printing the elements in a dictionary
print(person['pets']['cat'])

#i here is every list element
for i in person['children']:
     print(i)

for i,j in person['pets'].items():
     print(i)
     




                      
