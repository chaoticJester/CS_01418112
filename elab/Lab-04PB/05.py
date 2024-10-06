age = int(input("Enter your age: "))
net_income = int(input("Enter your net income: "))

if age < 15 or age > 60:
    print("Invalid age.")
elif net_income < 1 or net_income > 79999:
    print("Invalid income.")
else:
    nega_tax = (net_income * 0.2)
    if net_income > 30000:
        nega_tax = (30000 * 0.2 ) - (net_income - 30000) * 0.12 
    print(f"Your negative income tax is {nega_tax:.2f} Baht.")
   
