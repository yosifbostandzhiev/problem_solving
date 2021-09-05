# 10.Write a program that inputs an integer and checks whether it is a prime number.

n = int(input("Enter your number: "))
i = 0
count = 0
while i < n:
    i+=1
    if n % i == 0:
        count+=1
if count > 2 or count == 1:
    print("Your number is not prime")
else:
    print("Your number is prime")
