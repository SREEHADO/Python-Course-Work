n=int(input("Enter the size"))
for i in range(n):
    if i<=n//2:
        print('* '* (i+1))
    else:
        print('* '* (n-1))
'''

'''n=int(input("Enter the size"))
for i in range(n):
    for j in range (n):
        if j==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input("Enter the size"))
for i in range(n):
    for j in range (n):
        if j==0 or i==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input("Enter the size"))
for i in range(n):
    for j in range (n):
        if i==0 or j==0 or j==n-1 or i==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input("Enter the size"))
for row in range(n):
    for coln in range (n):
        if row==0 or coln==0 or (row==n-1 and coln<=n//2) or (coln==n//2 and row>=n//2) or (row==n//2 and coln>=n//2) or (coln==n-1 and row>=n//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n = [2000, 500, 100, 50, 10]
amount = int(input("Enter the amount: "))
for i in n:
    if amount>=i:
        t = amount//i
        amount %= i
        print(f'{t} * {i}')'''

'''n=int(int(input("Enter the num: ")))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=1

if sum==n:
    print("Perfect Number")
else:
    print("Not Perfect Number")



    
















