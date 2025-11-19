'''
fruits = ['apple','banana','mango']
for fruit in fruits:
    print(fruit)

number = 1
for number in range(1,21):
    print(number)

char = 'PYTHON'
for var in char:
    print(var)

total = 0
for i in range (1,101):
    total += i
print ("Total is :",total)

#Print only even numbers from 1 to 30 (use continue)
for i in range(1, 31):
    if i % 2 != 0:  # If number is ODD
        continue  # Skip to next iteration
    print(i)  # Print only EVEN numbers

string = "programming"
count = 0
for i in string:
    if i in "aeious":
        print(i)
        count+=1
print("total vowel : ",count)

name = input("Enter username : ")
reversename = ""

for i in name:
    reversename = i + reversename
print(reversename)

#8. Find the largest number in a list

num = [2,4,6,8,10]
largest = num[0]
for i in num:
    if (i > largest):
        largest = i
print (largest)

'''

Salary = int(input("Enter the salary : "))
if (Salary < 30,000):
    print("5% tax")
elif(Salary >30,000 and Salary<70,000):
    print("15% tax")
elif (Salary > 70,000):
    print("25% tax")
