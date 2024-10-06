hour = int(input("Enter number of hours: "))
minute = int(input("Enter number of minutes: "))

hm = hour*60 + minute

if minute > 59 or minute < 0 or hour < 0:
    print("Input Error!")
else :  
    if hm <= 15:
        price = 0
        print("No charge, thanks.")
    elif hm > 15 and hm <= 120:
        price = 10 
        print(f"Total amount due is {price} Bahts.")
    elif hm > 120 and minute == 0:
        price = (((hm // 60)- 2 ) * 10) + 10
        print(f"Total amount due is {price} Bahts.")
    elif hm > 120 and minute > 0:
        price = (((hm//60) - 2) * 10) + 10 + 10    
        print(f"Total amount due is {price} Bahts.")