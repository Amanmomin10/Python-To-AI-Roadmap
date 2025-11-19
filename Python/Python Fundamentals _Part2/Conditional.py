#IF, ELIF, ELSE , Match
'''
---------------------------------------------
age = int(input("Enter a age : "))

if age < 13:
    print("child")
elif age >= 13 and age <= 18:
    print("teenager")
elif age > 18:
    print("Adult")
-----------------------------------------------
Username = (input("Enter a Username : "))
Password = (input("Enter a Password : "))


if Username == "Admin" and Password == "Pass":
    print("Logged in") 
else :
    print("Wrong login pass")
-----------------------------------------------
a = int(input("Enter a num : "))

if a % 5 == 0:
    print("yes its multiple of 5")
else :
    print ("No its ot multiple of 5")
-----------------------------------------------
a = int(input("Enter a num : "))

if a % 2 == 0:
    print("yes its even")
else :
    print ("No its odd")
-----------------------------------------------
Username = (input("Enter a Username : "))
Password = (input("Enter a Password : "))


if Username == "Admin" and Password == "Pass":
    print("Logged in") 
else :
    if (Username != "Admin" ):
        print("Wrong User")
    else :
        print ("Wrong pass")
--------------------------------------------------
number = int(input("Enter a num : ")) 

match number:
    case 1 :
        print("ek")
    case 2 :
        print("DO")
    case 3 :
        print("teen")
    case 4 :
        print("Char")
    case _ :
        print("NO number")
----------------------------------------------------
'''