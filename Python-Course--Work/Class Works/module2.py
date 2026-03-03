# Modules : Group of functions, Group of Variables is called modules

from ATM import login,checkbalance,deposit,withdraw,viewTransactions
u_pin= int(input("Enter the pin: "))

if login(u_pin):

    while True:
        print('\n\n\n')
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("0. Exit")

        ch = int(input("Enter the choice: "))
        if ch==1:
            checkbalance(u_pin)
        elif ch==2:
            deposit(u_pin)
        elif ch==3:
            withdraw(u_pin)
        elif ch==4:
            viewTransactions(u_pin)
        elif ch==0:
            print("Thankyou")
            break
        else:
            print("Invalid choice")

import random

random.seed(1000)
print(random.randint(22,44))

#uniform is for float value

print(random.uniform(88,66))
names= ['harsha', 'dhanush', 'abhinov', 'rohan', 'vijay']
print(random.choice(names))
print(random.choices(names, k=3))
random.shuffle(names)
print(names)
