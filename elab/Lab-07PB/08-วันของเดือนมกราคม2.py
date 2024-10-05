first_day = str(input())
t_day = int(input())

if t_day < 1 or t_day > 31:
    print("ERROR")
else:
    if first_day == "Sunday":
        if (t_day - 1) % 7 == 0: 
            print("Sunday")
        elif (t_day - 2) % 7 == 0:
            print("Monday")
        elif (t_day - 3) % 7 == 0:
            print("Tuesday")
        elif (t_day - 4) % 7 == 0:
            print("Wednesday")
        elif (t_day - 5) % 7 == 0:
            print("Thursday") 
        elif (t_day - 6) % 7 == 0:
            print("Friday")
        elif (t_day + 1) % 7 == 0:
            print("Saturday")
    elif first_day == "Monday":
        if (t_day - 1) % 7 == 0: 
            print("Monday")
        elif (t_day - 2) % 7 == 0:
            print("Tuesday")
        elif (t_day - 3) % 7 == 0:
            print("Wednesday")
        elif (t_day - 4) % 7 == 0:
            print("Thursday")
        elif (t_day - 5) % 7 == 0:
            print("Friday") 
        elif (t_day - 6) % 7 == 0:
            print("Saturday")
        elif t_day % 7 == 0:
            print("Sunday")
    elif first_day =="Tuesday":
        if (t_day - 1) % 7 == 0: 
            print("Tuesday")
        elif (t_day - 2) % 7 == 0:
            print("Wednesday")
        elif (t_day - 3) % 7 == 0:
            print("Thursday")
        elif (t_day - 4) % 7 == 0:
            print("Friday")
        elif (t_day - 5) % 7 == 0:
            print("Saturday") 
        elif (t_day - 6) % 7 == 0:
            print("Sunday")
        elif (t_day + 1) % 7 == 0:
            print("Monday")
    elif first_day == "Wednesday":
        if (t_day - 1) % 7 == 0: 
            print("Wednesday")
        elif (t_day - 2) % 7 == 0:
            print("Thursday")
        elif (t_day - 3) % 7 == 0:
            print("Friday")
        elif (t_day - 4) % 7 == 0:
            print("Saturday")
        elif (t_day - 5) % 7 == 0:
            print("Sunday") 
        elif (t_day - 6) % 7 == 0:
            print("Monday")
        elif (t_day + 1) % 7 == 0:
            print("Tuesday")
    elif first_day == "Thursday":
        if (t_day - 1) % 7 == 0: 
            print("Thursday")
        elif (t_day - 2) % 7 == 0:
            print("Friday")
        elif (t_day - 3) % 7 == 0:
            print("Saturday")
        elif (t_day - 4) % 7 == 0:
            print("Sunday")
        elif (t_day - 5) % 7 == 0:
            print("Monday") 
        elif (t_day - 6) % 7 == 0:
            print("Tuesday")
        elif (t_day + 1) % 7 == 0:
            print("Wednesday")
    elif first_day == "Friday":
        if (t_day - 1) % 7 == 0: 
            print("Friday")
        elif (t_day - 2) % 7 == 0:
            print("Saturday")
        elif (t_day - 3) % 7 == 0:
            print("Sunday")
        elif (t_day - 4) % 7 == 0:
            print("Monday")
        elif (t_day - 5) % 7 == 0:
            print("Tuesday") 
        elif (t_day - 6) % 7 == 0:
            print("Wednesday")
        elif (t_day + 1) % 7 == 0:
            print("Thursday")
    elif first_day == "Saturday":
        if (t_day - 1) % 7 == 0: 
            print("Saturday")
        elif (t_day - 2) % 7 == 0:
            print("Sunday")
        elif (t_day - 3) % 7 == 0:
            print("Monday")
        elif (t_day - 4) % 7 == 0:
            print("Tuesday")
        elif (t_day - 5) % 7 == 0:
            print("Wednesday") 
        elif (t_day - 6) % 7 == 0:
            print("Thursday")
        elif (t_day + 1) % 7 == 0:
            print("Friday")
    else:
        print("ERROR")