phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
#Prints everything in the dictionary

print(len(phonebook))
#Prints the number of elements

print(type(phonebook))
#Prints the type of objects in dictionary

myDictionary = dict(m=8,n=9)
#Another way to create a dictionary - simply using dict function and m and n are the keys and 8 and 9 are the values

chris_phone = phonebook["Chris"]
#Assigns the corresponding Chris phone number to the variable

print(chris_phone)


print(myDictionary)


"""
print()
print('*****  end section 1 ********')
print()








print()
print('*****  start section 2 - search dictionary ********')
print()






print()
print('*****  end section 2 ********')
print()

name = 'Chris'

if name in phonebook:
    print(phonebook[name])
else:
    print(name,"was not found in the phonebook")





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

#The keys in the dictionary cannot be changed, the values however can be changed - mutable vs immutable

phonebook['Joe'] = '555-0123' #This key and value will be added since it could not be found in the dict
phonebook['Chris'] = '555-4444' # This will update value to the current key

#Key cannot be changed in dictionary, it can be deleted however.





print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


del phonebook['Chris'] #This will delete the whole Chris element (Chris and his phone number)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

#This iterates through keys (its the default method)
for key in phonebook:
    print(phonebook[key]) #This will just give us values, not the key names
    print(key) #This will print out everything



print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()

for value in phonebook.values(): #values here is a method, it is unique to a variable
    print(value)

print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()


for phonebook_tuple in phonebook.items(): #items method returns a tuple
    print(phonebook_tuple)
    print(type(phonebook_tuple))

for key,value in phonebook.items():
    print(key)
    print(value)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using get and clear methods********')
print()

#get method will try to pull the key, if it doesn't find it, it will return a default value

phone = phonebook.get('Chris','key not found')

print(phone)

phonebook.clear() #Deletes everything in the dictionary - an empty dictionary
print(phonebook)

print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using pop and popitem methods ********')
print()

a = phonebook.popitem()
#similar to the pop method, just picks one key and value at random (not really random, it will pick the same random key-value pair)
print(a)

print(phonebook)

remove = phonebook.pop('Chris','not found')
#This is different from delete method it deletes the thing from dictionary and store it into the variable remove

print(remove)

print(phonebook)

print()
print('*****  end section 9 ********')
print()


'''

import random #importing the random is prerequisite

print()
print('*****  start section 10 - using random and converting to list ********')
print()

randomKeys = list(phonebook) #names of all the people (keys)

choice = random.choice(randomKeys) #this will randomly pick from the list

print(phonebook[choice])



print()
print('*****  end section 10 ********')
print()


'''
'''



