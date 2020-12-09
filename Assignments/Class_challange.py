
# __init__() function

class Sports_cars:
    def __init__(self, make, modle):
        self.make = make
        self.modle = modle

    def myfunc(self):
        print("This is a " + self.make,self.modle) 

       
c1 = Sports_cars("Mercedes-Benz", "Amg")

c1.myfunc()


