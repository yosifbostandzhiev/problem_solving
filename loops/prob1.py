# 1.    Write a program that inputs a positive integer N and outputs the factorial of 2N

n = 3
n = 2 * n
n_fact = 1

for i in range(1, n):
    n_fact = n_fact + n_fact*i
print(n_fact)