

import app


def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    #The following is calling code from within this script
    print("I am running code form {}".format(print_app2()))

    #The following is calling code from theimported app.py
    print("I am running code form {}".format(app.print_app()))
