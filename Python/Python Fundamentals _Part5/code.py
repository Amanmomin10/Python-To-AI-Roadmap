'''
f = open("sample.txt", "r")  #File Object

data = f.read()
print(data)

data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()

f = open("sample.txt","w")
f.write("text to overwrite \n the complete data")

f.close()
'''
data = True
line = 1
with open ("sample.txt","r") as f:
    while data:
        data = f.readline()

        if ("Python" in data ):
            print(f"word found at line {line}")
            break

        line += 1

    
