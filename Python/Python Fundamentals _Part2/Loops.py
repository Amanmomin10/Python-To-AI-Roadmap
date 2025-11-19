#While, For
#While Loop Runs until codition become true
#For Loop : to travel each sequence of characters is all we do in for loop

'''
-------------------------------------------------
count = 5
while (count>=1):
    print("Count :",count)
    count-=1

i = int(input("Enter Number : ")) 
j = 1
while (j<=10):
    print (int(i * j))
    j+=1

i = 0
while (i<10):
    i+=1
    if (i % 2 == 0):
        continue
    print (i)

Name = "artificial"
Count = 0
for i in Name:
    if (i == "u" or
        i == "o" or
        i == "i" or
        i == "e" or
        i == "a" or
        i == "s"):
        Count +=1
print(Count)
'''

sum = 0 

for i in range (1,6):
    sum += i
print (sum)


    