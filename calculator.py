#making changes
def add():
    c = a + b
    return c

def sub():
    d = a - b
    return d

def multi():
    e = a*b
    return e

def div():
    f = a/b
    return f

def mod():
    g=a%b
    return g

print("Please enter numbers below")
a = int(input("Number 1:"))
b = int(input("Number 2:"))
print("Select the operation you want to perform")
o = int(input("1 to add\n2 to subtract\n3 to multiply\n4 to divide\n5 to mod\n:"))

if o==1:
    print(add())

elif o==2:
    print(sub())

elif o==3:
    print(multi())

elif o==4:
    print(div())

elif o==5:
    print(mod())
    
else:
    print("enter valid operator")
