n = int(input())
count = 0

while True:
    if n == 0 and count != 0: 
        break
    if n <= 0 and count == 0:
        print("ERROR")
        break
    print(n % 10)
    n = n // 10
    count += 1