import math

minB4due = int(input("Minutes before due: "))
temp= float(input("Temperature: "))
raining = str(input("Is it raining (y/n)? "))

if minB4due == 720:
    due_date = math.ceil(minB4due / 1440)
else :
    due_date = round(minB4due / 1440)

if due_date < 2 :
    print(f">>> {due_date} days before due.")
    print(">>> I will do the assignment.")
elif due_date > 5:
    print(f">>> {due_date} days before due.")
    print(">>> I will not do the assignment.")
else:
    if temp > 40 :
        print(f">>> {due_date} days before due.")
        print(">>> I will not do the assignment.")
    elif temp > 25 and raining in 'Yy':
        print(f">>> {due_date} days before due.")
        print(">>> I will not do the assignment.")
    else:
        print(f">>> {due_date} days before due.")
        print(">>> I will do the assignment.")
