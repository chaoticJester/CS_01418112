n = int(input())
l = 0

for i in range(1, n+1):
    for j in range(n):
        if i*j == n:
            if l == 0:
                l = i+j
            elif i+j < l:
                l = i+j
    
print(l)
