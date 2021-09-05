# 7.Write a program that outputs the following triangle(height=11):.
# Image of rectangle: https://ibb.co/B2HgfVL


for row in range(1, 9):
    for space in range(0, row):
        print(" ",end=" ")
    for num in range(1, 10-row):
        print(num, end=" ")
    print()