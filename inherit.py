# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 133
# DERIVING CLASSES - Shape example 

from Rectangle import *
from Triangle import *

# create an instance of each derived class
rect = Rectangle()
trey = Triangle()

rect.set_values(4,5)
trey.set_values(4,5)

print('Rectangle area : ' , rect.area())
print('Triangle area : ' , trey.area())
