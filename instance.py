# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 129
# COPYING INSTANCES - Bird exapmle

# make the features of the Bird class file available to this class 
from Bird import *

# display the document string for the Bird class
print ('\nClass instances of:\n', Bird.__doc__)

# create an instance of Bird and pass a string argument to its variable
polly = Bird('Squawk, squawk!')

# display the variable value and call the class method to display the common class variable value
print('\nNumber of Birds:', Bird.count)
print('Polly says:', polly.talk())

# create a second instance of the class passing a different string argument value to its variable
harry = Bird('Tweet, tweet!')

# display this variable value and call the class method to display the common class variable value
print('\nNumber of Birds:', Bird.count)
print('Harry says:', harry.talk())

