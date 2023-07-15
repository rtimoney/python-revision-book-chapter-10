# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 128
# COPYING INSTANCES - Bird exapmle

class Bird :
    "A class to define bird properties."

    count = 0

    def __init__(self , chat) :
        self.sound = chat
        
        Bird.count += 1


    def talk(self) :
        return self.sound










