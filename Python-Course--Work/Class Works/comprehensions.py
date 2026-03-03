#list comprehensions

l=[]
for i in range(1,11):
    l.append(i)
print(l)

lc=[i for i in range(1,11)]
print(lc)

res=[]
for i in range(1,11):
    if i%2==0:
        res.append(i)

resl =  [i for i in range(1,11) if i%2==0]
print(res,resl)

names=[]
for i in range(5):
    names.append(input("Enter the name: "))
print(names)

namesl= [input("Enter the name: ") for i in range(5)]
print(namesl)

s='Python Programming'
v='aeiouAEIOU'
r= [i if i in v else 0 for i in s]
print(r)


#set comprehensions
s='Python programming Language'
r=tuple(i for i in s)
print(r)

d={}
for i in range(1,6):
    d[i]=i*i
dl= {i:i*i for i in range(1,21)}
print(dl)

dl= {i:i*i for i in range(1,6)}
print(dl)

dl= {i:input("Enter the item") for i in range(1,6)}
print(dl)

dl= {("Enter the product: "): input("Enter the price: ") for i in range(1,6)}
print(dl)


