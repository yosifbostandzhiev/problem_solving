#5.    Write a program that calculates and outputs the sum of the digits of N factorial (N!).

n = int(input("Enter the desired number: "))
n_fact = 1
i = 0

while i < n:
    n_fact = n_fact + n_fact * i
    i+=1

sum = 0
str_fact = str(n_fact)
print(str_fact)

for _ in str_fact:
    sum = sum + int(_)
print(f"The sum of {n}! is: {sum}")
