# 4.    Write a program that calculates and outputs the first N even Fibonacci numbers, separated
# by comma and space. N is entered from the standard input.

n = int(input("Please input the desired number of first even Fibonacci numbers: "))
i = 1
fib = []
first = 0
second = 1
while i < n:
    first, second = second, first+second
    if second % 2 == 0:
        fib.append(str(second))
        print(", ".join(fib))
        i += 1

