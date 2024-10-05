total_roll = 0
sum_die = 0
result = None

while True:
    die1 = int(input())
    die2 = int(input())
    if die1 < 1 or die1 > 6 or die2 < 1 or die2 > 6:
        print("ERROR")
        continue
    
    total_roll += 1

    if total_roll == 1:
            if die1 + die2 == 7 or die1 + die2 == 11 :
                result = "W"
            elif total_roll == 1 and (die1 + die2 == 2 or die1 + die2 == 3 or die1 + die2 == 12) :
                result = "L"
            else :
                target_die = die1 + die2
                while True:
                    die1 = int(input())
                    die2 = int(input())
                    total_roll += 1
                    if die1 < 1 or die1 > 6 or die2 < 1 or die2 > 6:
                        print("ERROR")
                        total_roll -= 1
                        continue
                    if die1 + die2 == target_die:
                        result = "W"
                        break
                    elif die1 + die2 == 7:
                        result = "L"
                        break

    sum_die = die1 + die2
    if result:
        break
    
print(f"{total_roll} {sum_die} {result}")
