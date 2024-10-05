num = int(input())
total = 0

while True:
    total += num % 10
    
    num = num // 10

    if num == 0 and total < 10:
        print(total)
        break
    elif num == 0 and total > 9 :
        num = total 
        total = 0