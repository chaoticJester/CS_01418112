target = 72

num = int(input("Enter your guess (0 - 100): "))

if num < 0 or num > 100 :
    print("Sorry, out of range, try again later.")
elif num == target:
    print("Congratulations, your guess is correct.")
elif num > target :
    print("Sorry, your guess is too high, try again later.")
elif num < target : 
    print("Sorry, your guess is too low, try again later.")