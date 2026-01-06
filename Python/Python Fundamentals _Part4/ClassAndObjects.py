'''
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("aman",23)

print(p1.name)
print(p1.age)
--------------------------------------------------------------------------
class Student:
    college = "ABC college"

stu1 = Student()  # class attribute  
print(stu1.college) 
print(Student.college) # class attribute can also be accessed with class name
----------------------------------------------------------------------------

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

class Student:  
    def init  (self, name, marks):  
        self.name = name  
        self. marks = marks  
    def display(self):   # Instance method  
        print(f"Name: {self.name}, Marks: {self.marks}")

class person:
    def __init__(self,name):
        self.name = name 
    def greet(self):
        print("hello ", self.name) 
p1 = person("aman")
p1.greet()
----------------------------------------------------------------
class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name 

    def getinto(self):
        print(f"{self.price}{self.name}")

p1 = Product(1000,"OG")
p2 = Product(2000,"rge")
p3 = Product(3000,"vs")
p4 = Product(4000,"ge")

p1.getinto()
p2.getinto()
p3.getinto()
p4.getinto()
----------------------------------------------------------------
Create a class Employee with:
name
salary
Methods:
apply_bonus() → adds 10% bonus
show_details()
🔍 Logic Hint
Bonus = salary * 0.10
New salary = salary + bonus
----------------------------------------------
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,newBalance):
        self.__balance = newBalance

acc1  = BankAccount("Rahul kumar", 100_000)

acc1.set_balance(200_000)
print(acc1.name, acc1._BankAccount__balance)
'''
class Employee:
    start_time = "10 am"
    stop_time = "6 pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Math")
t1.change_time("5 pm")

print(t1.subject , t1.start_time , t1.stop_time)
        