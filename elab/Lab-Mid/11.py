num = int(input())
product = 1

while True:
    check_num = num % 10
    num = num // 10
    if check_num % 2 == 0:
        product *= check_num
    else :
        product += 0
    if num == 0:
        break

if product == 1:
    product = -1

print(product)