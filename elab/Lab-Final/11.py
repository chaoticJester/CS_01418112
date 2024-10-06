target = [i for i in str(input())]
guess = [i for i in str(input())]

result = [0, 0]

i = 0
while i < len(guess):
    if guess[i] == target[i]:
        result[0] += 1
        target[i] = '-'
        guess[i] = '-'
    i += 1

j = 0
while j < len(guess):
    if guess[j] != '-' and guess[j] in target:
        result[1] += 1
        target[target.index(guess[j])] = '-'
        guess[j] = '-'
    j += 1

print(f"{result[0]}-{result[1]}")

