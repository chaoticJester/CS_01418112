hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

fee = 0

if (hours + 1 > 20 and minutes > 0 ) or (hours > 20 and minutes == 0) or hours < 0 or minutes > 59 or minutes < 0:
    print("Invalid time.")
else :
    if minutes > 0 and hours >= 2:
        hours += 1
        
    if hours <= 4:
        fee += (hours - 2) * 20
        if buyAmt >= 300 and buyAmt <= 3000:
            fee -= 40
        elif buyAmt > 3000 :
            fee = 0     
    elif hours > 4:
        fee += (hours - 4) * 50 + 40
        if buyAmt >= 300 and buyAmt <= 3000:
            fee -= 40
        elif buyAmt > 3000 :
            fee = 0
        else :
            fee -= 0
        
    if fee <= 0:
        print("No charge, thank you.")
    else :
        print(f"Total amount due is {fee} Baht, thank you.")