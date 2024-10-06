n = int(input())
ls = []
for i in range(n):
    ch = str(input())
    ls.append(ch)
maxxor = 0
major = ''
for ch in ls:
    if ls.count(ch) > (n // 2):
        if ls.count(ch) > maxxor:
            maxxor = ls.count(ch)
            major = ch
if maxxor:
    print(major)
else:
    print(0)