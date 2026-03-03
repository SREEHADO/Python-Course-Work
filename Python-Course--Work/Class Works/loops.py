i=1
while i<=10:
    print(i)
    i+=1

l=[1,2,3,4,5,6]
i=0
while i<=5:
    print(l[i])
    i+=1
l[0]
l[1]
l[2]
l[3]
l[4]
l[5]

l=(1,2,3,4,5,6, 3535,5235,553.68686)
i=0
while i<=5:
    print(l[1])
    i+=1


for i in range(10):
    pass


for i in range(12):
    if i==7:
        break
    print(i)

for i in range(12):
    if i==8:
        continue
    print(i)

#candy crush example
moves=25

winning_point=int(input("Enter the winning point: "))

while moves>0:
    moves-=1
    if moves==winning_point:
        print("Sugar Sugar Crush!!!!!")
        break

    print(f'{moves} left')

chances=5
stored_pin="12345"

while chances>0:
    pin=input("Enter the pin:  ")
    if pin==stored_pin:
        print("login sucessful")
        break
    else:
        print("Incorrect pin")
    chances-=1

else:
    print("Try Again!! After 30 secs") 
    #if else is used break will not work in code


chances=10
stored_pin="12345 456789"

while chances>0:
    pin=input("Enter the pin:  ")
    if pin==stored_pin:
        print("login sucessful")
        break
    else:
        print("Incorrect pin")
    chances-=1

else:
    print("Try Again!! After 30 secs") 


products= ['iphone','headset','smartwatch','tv','ac']

product = input("Enter the product: ").strip()
for i in products:
    if i==product:
        print(f"{i} is found. You can buy it.")
        break


products= ['iphone','headset','smartwatch','tv','ac']

product = input("Enter the product: ").strip()
for i in products:
    if i==product:
        print(f"{i} is found. You can buy it.")
        break

else:
    print(f"{product} is not found")


