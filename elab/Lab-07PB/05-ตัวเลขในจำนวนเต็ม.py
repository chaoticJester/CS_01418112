num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
count = 0

if num < 0 and (digit < 0 or digit > 9): 
    print("Invalid number.")
    print("Invalid digit.")   
elif num < 0 :
    print("Invalid number.")
elif digit < 0 or digit > 9:
    print("Invalid digit.")
else : 
    while True:
        if str(num) == "0":
            break
        checkNum = num % 10
        num = num // 10

        if checkNum == digit:
            count += 1

    if count == 1:
        print(f"Digit {digit} occurs 1 time.")
    else:
        print(f"Digit {digit} occurs {count} times.")

