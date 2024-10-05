target_input = int(input("Enter a target (4-digit integer): "))
guess_input = int(input("Enter your guess (4-digit integer): "))

position = 0
digit = 0
count = 0
target_loop = target_input

while True:
    if count == 4:
        break
    
    if target_input == guess_input:
        position = 4
        digit = 4
        break

    target_str = str(target_input)
    guess_str = str(guess_input % 10)

    if guess_input % 10 == target_loop % 10:
        position += 1
    elif guess_str in target_str:
            digit += 1
            if guess_input % 10 == target_loop % 10:
                position += 1
                digit -= 1

    target_loop = target_loop // 10
    guess_input = guess_input // 10
    count += 1
    
print_p = ''
print_d = ''

if position == 0:
    print_p = "No positions"
elif position == 1:
    print_p = "One position"
elif position == 2:
    print_p = "Two positions"
elif position == 3:
    print_p = "Three positions"
elif position == 4:
    print_p = "Four positions"

if digit == 0:
    print_d = "no digits"
elif digit == 1:
    print_d = "one digit"
elif digit == 2:
    print_d = "two digits"
elif digit == 3:
    print_d = "three digits"
elif digit == 4:
    print_d = "four digits"

if position == 4 and digit == 4:
    print("Congratulations, you just mastered my mind!!")
else : 
    print(f"{print_p} correct, {print_d} correct")