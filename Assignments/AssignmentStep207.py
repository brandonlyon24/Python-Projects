#
#   POLYMORPHISM:   Assignment
#
#   Each child should have at least two of their own attributes
#   The parent class should have at least one method (function)
#   Both child classes should utilize polymorphism on the parent class method
#
#   Author:  Brandon Lyon



# Parent class
class Driver:
    name = "Brandon"
    number = '24'
    car = 'Subaru'

    def getDriverInfo(self):
        driver_name = input("Please enter the drivers name: ")
        driver_number = input("Please enter the drivers number: ")
        driver_car = input("Please enter the modle of the car: ")
        if (driver_name == Driver.name and driver_number == Driver.number and driver_car == Driver.car):
            print(" This is {}, He drives a {} and is number {}.".format(driver_name,driver_car,driver_number))
        else:
            print("Ooops! Didnt reconize the driver")
    
# Child class
class Tracks(Driver):
    track_loc = 'Lebanon Oregon Speed way'
    win = "10"
    loss = "4"
    driverId = "24"

    def getDriverInfo(self):
        driver_name = input("Please enter the drivers name: ")
        driver_number = input("Please enter the drivers number: ")
        driver_Id = input("Please enter the driver ID: ")
        if (driver_name == Driver.name and driver_number == Driver.number and driver_Id == self.driverId):
            print(" This is {}, He drives a subaru and is number {}. He has {} wins at {}".format(driver_name,driver_number,self.win,self.track_loc))
        else:
            print("Ooops! Didnt reconize the driver")
# Child class
class raceType(Driver):
    rally = '3'
    circleTrack = '10'
    nascar = '1'
    motocross = '20'

    def getDriverInfo(self):
        driver_name = input("Please enter the drivers name: ")
        driver_number = input("Please enter the drivers number: ")
        driver_car = input("Please enter the modle of the car: ")
        if (driver_name == Driver.name and driver_number == Driver.number and driver_car == Driver.car):
            print("{} drives a {} and is Number {} he has\n{} Rally Wins\n{} Circle Track Wins\n{} Nascar Wins\n{} MotoCross Wins ".format(driver_name,driver_car,driver_number,self.rally,self.circleTrack,self.nascar,self.motocross))
        else:
            print("Ooops! Didnt reconize the driver")
    

 

search = raceType()
search.getDriverInfo()


#search = Driver()
#search.getDriverInfo()

#manager = Tracks()
#manager.getDriverInfo()
