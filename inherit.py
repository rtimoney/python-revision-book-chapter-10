# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 133
# DERIVING CLASSES - Shape example 

from Rectangle import *
from Triangle import *

# create an instance of each derived class
rect = Rectangle()
trey = Triangle()

# call the class method inherited from the base class, passing arguments to assign to the class variables
rect.set_values(4,5)
trey.set_values(4,5)

# display the result of manipulating the class variables inherited from the base class 
print('Rectangle area : ' , rect.area())
print('Triangle area : ' , trey.area())
