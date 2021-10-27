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
o = input("operator:")

if o=="+":
    print(add())

elif o=="-":
    print(sub())

elif o=="*":
    print(multi())

elif o=="/":
    print(div())

elif o=="%":
    print(mod())
    
else:
    print("enter valid operator")
