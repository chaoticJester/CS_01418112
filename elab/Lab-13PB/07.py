def horizontal(x,y,ls):
    count = 0 
    if x == 0 :
        if ls[y][x+1] == '*':
            count += 1
    elif x == len(ls[y]) - 1:
        if ls[y][x-1] == '*':
            count += 1
    else:
        if ls[y][x+1] == '*':
            count += 1
        if ls[y][x-1] == '*':
            count += 1
    return count

def vertical(x,y,ls):
    count = 0
    if y == 0:
        if ls[y+1][x] == '*':
            count += 1
    elif y == len(ls) - 1 :
        if ls[y-1][x] == '*':
            count += 1
    else:
        if ls[y+1][x] == '*':
            count += 1
        if ls[y-1][x] == '*':
            count += 1
    return count

def เฉียง(x,y,ls):
    count = 0
    if y == 0 and x == 0:
        if ls[y+1][x+1] == '*':
            count += 1
    elif y == 0 and x == len(ls[y]) - 1:
        if ls[y+1][x-1] == '*':
            count += 1
    elif y == 0  and 0 < x < len(ls[y]) - 1:
        if ls[y+1][x+1] == '*':
            count += 1
        if ls[y+1][x-1] == '*':
            count += 1
    elif y == len(ls) - 1 and x == 0:
        if ls[y-1][x+1] == '*':
            count += 1
    elif y == len(ls) - 1 and x == len(ls[y]) - 1:
        if ls[y-1][x-1] == '*': 
            count += 1
    elif y == len(ls) - 1 and 0 < x < len(ls[y]) - 1:
        if ls[y-1][x+1] == '*':
            count += 1
        if ls[y-1][x-1] == '*': 
            count += 1
    elif 0 < y < len(ls)-1 and x == 0:
        if ls[y-1][x+1] == '*':
            count += 1
    elif 0 < y < len(ls)-1 and x == len(ls[y]) - 1:
        if ls[y-1][x-1] == '*': 
            count += 1
        if ls[y+1][x-1] == '*':
            count += 1
    elif 0 < y < len(ls)-1:
        if ls[y+1][x+1] == '*':
            count += 1
        if ls[y+1][x-1] == '*':
            count += 1
        if ls[y-1][x+1] == '*':
            count += 1
        if ls[y-1][x-1] == '*': 
            count += 1
    return count

#main
RxC = str(input()).split('x')
table = []
for i in range(int(RxC[0])):
    table.append(['0'] * int(RxC[1]))

total_b = int(input())
for i in range(total_b):
    coordinate = str(input()).split(',')
    table[int(coordinate[0])][int(coordinate[1])] = '*'

for y in range(len(table)):
    for x in range(len(table[y])):
        boomboom = 0
        if table[y][x] != '*':
            boomboom += horizontal(x,y,table) + vertical(x,y,table) + เฉียง(x,y,table)
            table[y][x] = str(boomboom)

for row in table:
    for e in row:
        print(e, end='')
    print('')