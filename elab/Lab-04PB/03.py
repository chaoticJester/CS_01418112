TV = int(input("How many TVs? ")) 
DVD = int(input("How many DVD players? "))
AUDIO = int(input("How many Audio Systems? "))

price = (6000 * TV) + (1500 * DVD) + (3000 * AUDIO)

print(f"Total price is {price:.2f} baht.")

if price < 24000:
    discount = price * 0
    payment = price - discount
elif price >= 24000:
    discount = price * 0.2
    print(f"You've got a discount of {discount:.2f} baht.")
    payment = price - discount

print(f"Your payment is {payment:.2f} baht. Thank you!") 