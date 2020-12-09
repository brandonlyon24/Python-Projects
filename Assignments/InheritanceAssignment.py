#
#
#   Assignment: Create two classes that inherit from another class.
#               Each child should have at least two of their own attributes.
#
#   Author: Brandon Lyon
#   Date:   12-6-20
#


class Driver:
    name = 'No name provided'
    email = ' '
    password = '1234abcd'
    driver_wins = 1

class Car(Driver):
    car_make = 'Subaru'
    car_number = 24

class Track(Driver):
    track_loc = ' '
    win_loss = True

print(Driver)


