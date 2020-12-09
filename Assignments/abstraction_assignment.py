#   Purpose:    Create a class that utilizes the concept of abstraction.
#   1. Your class should contain at least one abstract method and one regular method.
#   2. Create a child class that defines the implementation of its parents abstract method.
#   3. Create an object that utilizes both the parent and child methods.
#   4. Add comments throughout your Python explaining your code.
#
#   Author:     Brandon Lyon

from abc import ABC, abstractmethod

class carPrice(ABC):
    def paySlip(self, amount):
        print("The Price of this car is: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass

class DebitcardPayment(carPrice):
    def payment(self, amount):
        print('The car you want to buy is {}, do you have enough for a down payment?'.format(amount))


obj = DebitcardPayment()
obj.paySlip("$50,000")
obj.payment("$50,000")
