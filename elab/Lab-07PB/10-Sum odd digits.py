num = str(input())
sum = 0

for i in num:
    if int(i) % 2 == 1:
        sum = sum + int(i)

if sum == 0:
    sum = -1

print(sum)