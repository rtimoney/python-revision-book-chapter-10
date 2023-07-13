# CHAPTER 10 - PROGRAMMING OBJECTS
# PAGE 129
# COPYING INSTANCES - Bird exapmle

from Bird import *

print ('\nClass instances of:\n', Bird.__doc__)

polly = Bird('Squawk, squawk!')
print('\nNumber of Birds:', Bird.count)
print('Polly says:', polly.talk())

harry = Bird('Tweet, tweet!')
print('\nNumber of Birds:', Bird.count)
print('Harry says:', harry.talk())

