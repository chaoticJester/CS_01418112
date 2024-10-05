x = int(input())
n = int(input())

if n > 31 or x > 31 or x < 1 or n < 1 or x > 7:
    print("ERROR")
else :
    if (n - x) % 7 == 0:
        print("Sunday")
    elif (n - (x + 1)) % 7 == 0:
        print("Monday")
    elif (n - (x + 2)) % 7 == 0:
        print("Tuesday")
    elif (n - (x + 3)) % 7 == 0:
        print("Wednesday")
    elif (n - (x + 4)) % 7 == 0:
        print("Thursday")
    elif (n - (x + 5)) % 7 == 0:
        print("Friday")
    elif (n - (x + 6)) % 7 == 0:
        print("Saturday")


    


