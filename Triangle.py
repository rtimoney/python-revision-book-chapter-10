# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 133
# DERIVING CLASSES - Shape example 

from Polygon import *

# declare a derived class with a method to return manipulated class variable values
class Triangle(Polygon) :
    "A class to define Triangle properties."

    def area(self) :
       return(self.width * self.height)/2
       
