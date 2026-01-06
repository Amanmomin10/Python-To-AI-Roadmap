'''
s = input("enter a palindrome : ").strip()

if s == s[::-1]:
    print(f"its a palindrome : {s}")
else:
    print(f"its not a palindrome : {s}")
--------------------------------------------------------

nums = input("Enter numbers separated by space: ").split()

# convert each item to integer
nums = [int(x) for x in nums]

if len(nums) == 0:
    print("No numbers provided.")
else:
    avg = sum(nums) / len(nums)
    print("Average:", avg)
------------------------------------------------------------------------------
Input two lists of integers from the user. Merge them into one list and sort the 
result.
list1 = [1, 2, 7],
list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]

list1 = [int(x) for x in input("enter a input :").split()]
list2 = [int(x) for x in input("enter a input :").split()]

merged = list1 + list2
result = sorted(merged)

print(result)
print(merged)
------------------------------------------------------------

 Given a tuple of integers, create:
 • A tuple of all even numbers
 • A tuple of all odd numbers

 tuple = (1,2,3,4,5,6,7,8,9)

even = ()
odd = ()

for num in tuple:
    if (num % 2 == 0 ):
        even = even + (num,)
    else :
        odd = odd + (num,)
print("Tuple of even numbers:", even)
print("Tuple of odd numbers:", odd)
------------------------------------------------------
Create a dictionary where: 
• Keys = student names 
• Values = marks (integer) 
Write a menu-based program where user presses a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the dictionary: 
1.A - Add a student 
2.B - Update marks 
3.C - Search for a student 
4.D - Display all students and marks


words = ["apple", "banana", "kiwi", "cherry", "mango"]

result = {}

for var in words:
    result[var] = len(var)
print(result)

s = input("enter names :")
space = s.count(" ")
print (space)
    

'''
list1 = [1,2,3,4]
list2 = [5,6,7,8]

set1 = set(list1)
set2 = set(list2)


print



