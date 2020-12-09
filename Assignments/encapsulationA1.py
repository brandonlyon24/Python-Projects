#
#   Encapsulation Assignment
#1. This class should make use of a private attribute or function.
#2. This class should make use of a protected attribute or function.
#3. Create an object that makes use of protected and private.
#4. Add comments throughout your Python explaining your code.
# Author:   Brandon Lyon
#


class Protected:
    def __init__(self):
        self.__privateVar = 10
        self._protectedVar = 5

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

    def getProtected(self):
        print(self._protectedVar)

    def setProtected(self, protected):
        self._protectedVar = protected




        

obj = Protected()   # shortens the name 
obj.getPrivate()    # gets the private number 
obj.setPrivate(23)  # Sets the value to a new value 
obj.getPrivate()    # Gets that new value 
obj.getProtected()
