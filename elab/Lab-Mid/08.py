n = int(input())
l = 1
p = 1
sumn = 0

while l <= n:
    while p < n:
        if l*p == n:
            if sumn == 0:
                sumn = l+p
            elif l+p < sumn:
                sumn = l+p
        p += 1
    p = 0
    l += 1
    
print(sumn)
