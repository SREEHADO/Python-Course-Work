
def wish(name):
    return f"Welcome to Python Course {name}!!"

wish1 = lambda name: f"Welcome to Python Course {name}!!"

print(wish1("dhanush"))
print(wish1("Harsha"))

def greatest(a,b):
    if a>b:
        return a
    else:
        return b 

greatest1 = lambda a,b: a if a>b else b

print(greatest(19,12))
print(greatest(15,20))

def greatest(a,b,c):
    return a+b+c

suml = lambda a,b,c: a+b+c

print(suml(33,55,44))
print(suml(15,20,23))

#all codes in a single lambda code
#lambda is short form of all codes to run in 1-2 lines
#Map, Filter, Reduce







