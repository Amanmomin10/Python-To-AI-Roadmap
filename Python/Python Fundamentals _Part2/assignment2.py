'''
Salary = int(input("Enter the salary : "))
if (Salary < 30,000):
    print("5% tax")
elif(Salary >30,000 and Salary<70,000):
    print("15% tax")
elif (Salary > 70,000):
    print("25% tax")

def num(a,b):
    for i in range(a,b+1):
        if (i % 2 == 0):
            print(i)
    return
print(num(2,20))

def print_digits(n):
    # Step 1: store digits in a list (reverse order)
    digits = []

    while n > 0:
        last_digit = n % 10      # extract rightmost digit
        digits.append(last_digit)
        n = n // 10              # remove rightmost digit

    # Step 2: reverse the list because digits were collected backwards
    digits.reverse()

    # Step 3: print each digit
    for d in digits:
        print(d)

# Example
print_digits(312)

#number = 1
for i in range(1,100+1):
    if (i % 3 == 0 and  i % 5 == 0):
        print ("number divide by 3 and 5 : ",i)
        i+=1
---------------------------------------------
'''
n = int(input("Enter a number : "))

if (n>0):
    print("num is posittive")
elif (n<0):
    print("num is negative")
elif(n == "quit"):
    print ("program has ended")

