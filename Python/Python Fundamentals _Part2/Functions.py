#Funtion is reusable blocks of code that perform a specific task.
'''
def hellow():
    print ("Hello World")

hellow()
------------------------------------------------------
def sum(a,b):
    c = a + b
    return c
print (sum(3,4))
------------------------------------------------------
def Avg(a,b,c):
    average = int((a+b+c)/3)
    return average
print (Avg(2,2,2))
------------------------------------------------------
def sum(a,b=1):
    return a +b 
print(sum(5))
'''
def p_fact (n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    return fact
n = int(input("Enter number : "))
print(p_fact(n))
 