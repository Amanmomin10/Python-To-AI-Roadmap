a = 10
b = 5

#Arithematic Operators - used to perform math operations.
print(a + b)    #Addition
print(a - b)    #Substration
print(a * b)    #Multiplication
print(a / b)    #Division
print(a % b)    #Modulo(Remainder)
print(a ** b)   #a^b

#Relational or conditional operator - used to perform math operations.
print(a == b)   #Equals To
print(a > b)    #Greater than
print(a < b)    #Less Than
print(a >= b)   #Greater than or Equals To
print(a <= b)   #Less Than or Equals To
print(a != b)   #Not Equals To

#Assignment Operators - used to assign values to variables.
a += 5
print(a)    # a = a+5 ==> a = 10+5 ==> 15
a -= 5
print(a)    # a = a-5 ==> a = 15-5 ==> 10
a *= 5
print(a)    # a = a*5 ==> a = 10*5 ==> 50
a /= 5
print(a)    # a = a/5 ==> a = 50/5 ==> 10.0
a %= 5
print(a)    # a = a%5 ==> a = 10%5 ==> 0
a **= 5
print(a)    # a = a**5 ==> a = 0.0**5 ==> 0.0

# ==============================================================================================
#                  LOGICAL OPERATORS TRUTH TABLE - used to combine boolean values.
# ==============================================================================================
# val1   val2         And          |    val1   val2         0R         |    val1       Not
# ----------------------------------------------------------------------------------------------
# True   True        True          |    True   True        True        |    True      False
# True   False       False         |    True   False       True        |    False     True
# False  True        False         |    False  True        True        |
# False  False       False         |    False  False       False       |
# ==============================================================================================

x = 5
y = 10
z = 15

print (not (x>y)) #True ==> In NOT it basically reverse(True ka false, False ka true) the value.
print (not (x<y)) #False

print ((z>y) and (y>x)) #True ==> In AND if both are True then True otherwise all False.
print ((z>y) and (y<x)) #False
print ((y>z) and (y>x)) #False
print ((x>y) and (y>z)) #False

print ((z>y) or (y>x)) #True ==> In OR if both are False then False otherwise all True.
print ((z>y) or (y<x)) #True
print ((y>z) or (y>x)) #True
print ((x>y) or (y>z)) #False

'''
Operator Precendence 
Operators have a priority i.e there is a specific order in which operations are to be performed.
In Case We have same Precendence E.g.*, / .Then we Go from Left to Right 
↓   ()   ==>  Parentheses (highest priority)
↓   **   ==> Exponent
↓   *, /,%  ==> Multiplication, division, modulus 
↓   +,-     ==> Addition, subtraction 
↓   ==, !=, >, >=, <, <=    ==> Comparison operators 
↓   not   
↓   and   
↓   or    

'''