odd_count = 0

while True:
    user_input = int(input("Enter number: "))

    if user_input < 0:
        break

    if user_input % 2 != 0:
        odd_count += 1

print(f"Received {odd_count} odd numbers")