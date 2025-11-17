#Type conversion is when we convert(cast) variables from one type to another.
#1.Type conversion - Implicit, done automatically by Python.
a = 5  
b = 3.0  
print(a + b) # Python converts answer in float by default

#2.Type Casting - Explicitly, done by the programmer.
x = 10        # int  
y = float(x)  # convert to float 
z = str(x)    # convert to string 
print(x)
print(y)
print(z)

#int(), float(), str(), bool(), list(), tuple() are common type conversion functions
 
#We use the function to take input from user while the program is running. 
#Whatever the user types in input prompt is returned as a string.
username = input("Enter your name : ")
print (username, type(username)) #type is string 

a = int(input("Enter number1 :" ))
b = int(input("Enter number2 :" ))
sum = a + b
print(sum)

x = float(input("Enter number1 :" ))
y = float(input("Enter number2 :" ))
sum = x + y
print(sum)

a = float(input("Enter A :")) #Average of two number
b = float(input("Enter B :"))
Avg = (a+b)/2
print(Avg)