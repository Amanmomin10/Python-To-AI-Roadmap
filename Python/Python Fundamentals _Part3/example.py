#tup = (1,2,3,4,3,3,3,3,5)
#print (tup.count(3))

'''
info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

unique_courses = set()

for tup in info:
    unique_courses.add(tup[1])
    
print(unique_courses)
---------------------------------------------------------------
info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

unique_courses = set()

for tup in info:
    if(tup[1] == "English"):
        print ((tup[0]),tup)

'''


info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

dict = {}

for name, course in info:
    if (dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
