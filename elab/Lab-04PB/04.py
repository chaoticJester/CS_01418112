buffet_choice = str(input("Enter your buffet choice: "))
price = 0

if buffet_choice == "Korean":
    price = 1500
    weds_or_not = str(input("Is today Wednesday (yes/no)? "))
    
    if weds_or_not == "yes":
        discount = price * 0.15
    elif weds_or_not == "no":
        discount = price * 0

    payment = price - discount
    print(f"Your payment is {payment:.2f} Baht.")
elif buffet_choice == "Japanese":
    price = 1000
    weds_or_not = str(input("Is today Wednesday (yes/no)? "))

    if weds_or_not == "yes":
        discount = price * 0.15
    elif weds_or_not == "no":
        discount = price * 0

    payment = price - discount
    print(f"Your payment is {payment:.2f} Baht.")
else :
    print(f"Sorry, there is no {buffet_choice} buffet.")


    


