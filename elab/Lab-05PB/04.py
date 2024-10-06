n = int(input())
symbol = str(input())
row = n
mul = 1

while row > 0:
    print(symbol*mul)
    row -= 1
    mul += 1 