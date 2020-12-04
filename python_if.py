



num1 = 12
key = False 


if num1 == 12:
    if key:
        print('num1 is equal to 12 and they have the key')
    else:
        print('num1 is equal to 12 and they do not have the key')  
elif num1 < 12:
    print('num1 is less than 12')
else:
    print('num1 is not equal to 12')



a = 100
b = 50

if a > b:
    print('A is bigger than b')
elif a == b:
    print('A and B are equal')
else:
    print('B is bigger than a')


#Nested statement 
x = 60

if x > 40:
    print('x is bigger than 40')
    if x > 50:
        print('Its not 50 so it must be 60!')
    else:
        print('number is bigger than 60')


print(bool('Hello'))


print(isinstance(x,int))


i = 0
while i < 12 :
	print("{} iteration through the loop.".format(i))
	if i == 6:
            i += 1


while i < 10:
	print(i)
	if i == 5:
		break
	i += 1


while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("hello")
