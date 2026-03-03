#positive or negative
num = float(input("Enter a number: "))
if num >= 0:
    print("Positive number")
else:   
    print("Negative number")

#Even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:    
    print("Even number")
else:
    print("Odd number")


#Divisible by 5
num = int(input("Enter a number: "))
if num % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")


#Divisible by 5 and 11
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")  

#Leap year 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#check pass or fail  
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


#check if number is 3-digit
num = int(input("Enter a number: "))
if 100 <= num <= 999:
    print(num, "is a 3-digit number")
else:
    print(num, "is not a 3-digit number")