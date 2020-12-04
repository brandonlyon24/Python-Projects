#u
####   Python: 3.6.4
#   
####   Author: Brandon Lyon
#
####   Purpose: 
#


####def start():
####    print("Hello {}".format(get_name()))
##
##
##
####def get_name():
####    name = input("What is your name?")
####    return name




def start():
    f_name = "Brandon"
    l_name = "Lyon"
    age = 22
    gender = "Male"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} yearold {}.".format(f_name,l_name,age,gender))
    





if __name__ == "__main__":
    start()
