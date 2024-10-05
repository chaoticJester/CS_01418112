num = str(input())
product = 1

for i in num:
    if int(i) % 2 == 0:
        product = product * int(i)
    else:
        product = product + 0

if product == 1:
    product = -1

print(product)