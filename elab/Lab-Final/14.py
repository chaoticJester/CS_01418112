import math
ls = []
while True:
    num = int(input())
    if num == 0:
        break
    ls.append(num)

m = -math.inf
for i in range(len(ls)):
    for j in range(len(ls), i ,-1):
        if sum(ls[i:j]) > m :
            m = sum(ls[i:j])
print(m)