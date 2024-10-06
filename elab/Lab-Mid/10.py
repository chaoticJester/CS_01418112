num = int(input())
sumx = 0
while True:
    check_num = num % 10
    num = num // 10
    if check_num % 2 == 1:
        sumx += check_num
    if num == 0:
        break

if sumx == 0:
    sumx = -1

print(sumx)