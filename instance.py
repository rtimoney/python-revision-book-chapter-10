# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 129
# COPYING INSTANCES - Bird exapmle

# make the features of the Bird class file available to this class 
from Bird import *

# display the document string for the Bird class
print ('\nClass instances of:\n', Bird.__doc__)

# create an instance of the class then add a new attribute with an assigned value using dot notation
chick = Bird('Cheep, cheep!')
chick.age = '1 week'

# display the values in both variable attributes
print('\nChick says:', chick.talk())
print('Chick age:', chick.age)

# modify the age attribute using dot notation and display the new value
chick.age = '2 weeks'
print('\nChick now:', chick.age)

# modify the age attribute again using a built in function
setattr(chick , 'age', '3 weeks')

# display a list of all non-private insurance attributes and their respective values using a built-in function
print('\nChick attributes...')
for attrib in dir(chick) :
    if attrib[0] != '_' :
        print(attrib , ':', getattr(chick,attrib))

# remove the age attribute
delattr(chick , 'age')
# confirm its removal using a built-in function
print('Chick age attribute? :', hasattr(chick,'age'))



