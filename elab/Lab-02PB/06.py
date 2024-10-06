n = int(input())
s1 = str(input())
s2 = str(input())

output = (s1 + s2) * (n // 2) + s1 *(n % 2)
print(output)