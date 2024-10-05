target = 72
count = 0 
while True:
    guess_input = int(input("Enter your guess: "))

    count += 1

    if 0 <= guess_input <= 100 :
        if guess_input == target:
            print("Congratulations, your guess is correct.")
            print(f"Total number of guesses is {count}.")
            break
        elif guess_input < target :
            print("Sorry, your guess is too low.")
            continue
        elif guess_input > target :
            print("Sorry, your guess is too high.")
            continue
    else:
        print("Sorry, your guess is out of range.")
        continue
