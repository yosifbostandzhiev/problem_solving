# 9.Write a program that outputs the first N natural numbers in a rectangle with a given width (W).
# The width is the number of symbols ( not numbers) in a line! Numbers are printed in
# ascending order sequentially in horizontal direction until line is complete and the
# sequence continues on the next line, etc.No spaces.The text on the console shall look as a
# rectangular block (the last line may be incomplete).N and W are entered by the user.


rows = int(input())
columns = int(input())

for row in range(rows):
    for column in range(columns+1):
        print(column, end=" ")
    print()

l = [[y for y in range(columns+1)] for x in range(rows)]
print(l)