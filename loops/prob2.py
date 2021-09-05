# 2.    Write a program that counts and outputs the number of digits in Nth Fibonacci number
# •    Example:
# Please input a positive integer: 13
# Number of digits in F5 is: 3

n = int(input("Please input a positive integer:"))
i = 2
first, second = 0,1


while i < n:
    first, second = second, first+second
    answer = str(second)
    i+=1
print(f"Number of digits F{n} is:", len(answer))


