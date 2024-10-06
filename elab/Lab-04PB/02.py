price = 0

print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")

choice1 = input("Enter your choice: ")

if choice1 in 'Bb' :
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    sub_choice = input("Enter your choice: ")
    if sub_choice in 'Rr':
        price += 60
        menu = "Regular Burger"
        print(f"Your {menu} is {price} Baht.")
    elif sub_choice in 'Cc':
        price += 75
        menu = "Cheese Burger"
        print(f"Your {menu} is {price} Baht.")
    elif sub_choice in 'Dd':
        price += 90
        menu = "Double Cheese Burger"
        print(f"Your {menu} is {price} Baht.")
    else:
        print("Invalid sub menu choice.")
elif choice1 in 'Cc':

    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")

    sub_choice = input("Enter your choice: ")

    if sub_choice in 'Ff':
        price += 120
        menu = "Fried Chicken"
        print(f"Your {menu} is {price} Baht.")
    elif sub_choice in 'Gg':
        price += 150
        menu = "Grilled Chicken"
        print(f"Your {menu} is {price} Baht.")
    elif sub_choice in 'Cc':
        price += 180
        menu = "Chef's Chicken"
        print(f"Your {menu} is {price} Baht.")
    else : 
        print("Invalid sub menu choice.")
elif choice1 in 'Pp':

    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")

    sub_choice = input("Enter your choice: ")

    if sub_choice in 'Ss':
        price += 90
        menu = "Spaghetti de Italiano"
        print(f"Your {menu} is {price} Baht.")
    elif sub_choice in 'Ll':
        price += 120
        menu = "Lasagna Supreme"
        print(f"Your {menu} is {price} Baht.")
    elif sub_choice in 'Mm':
        price += 100
        menu = "Macaroni Special"
        print(f"Your {menu} is {price} Baht.")
    else : 
        print("Invalid sub menu choice.")
else :
    print("Invalid main menu choice.")


