Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myTuple = ("green", "blue", "red")
>>> print(myTuple)
('green', 'blue', 'red')
>>> for x in myTuple:
	print(x)

	
green
blue
red
>>> X = myTuple.count
>>> print(X)
<built-in method count of tuple object at 0x033C8588>
>>> myset = {"Engine", "Transmission", "Body
	 
SyntaxError: EOL while scanning string literal
>>> myset = {"Engine", "Transmission", "Body"}
>>> print(myset)
{'Transmission', 'Engine', 'Body'}
>>> myset.add("Wheels")
>>> print(myset)
{'Transmission', 'Engine', 'Body', 'Wheels'}
>>> myset.remove("Wheels")
>>> print(myset)
{'Transmission', 'Engine', 'Body'}
>>> myset2 = {"Driver", "Turbo", "Steering Wheel"}
>>> y = myset.difference(myset2)
>>> print(y)
{'Transmission', 'Engine', 'Body'}
>>> myset.add("Driver")
>>> y = myset.difference(myset2)
>>> print(y)
{'Transmission', 'Engine', 'Body'}
>>> myset2.add("Engine")
>>> print(y)
{'Transmission', 'Engine', 'Body'}
>>> print(y)

             
